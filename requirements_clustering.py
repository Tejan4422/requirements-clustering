import pandas as pd
import numpy as np
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

class RequirementsAnalyzer:
    def __init__(self, credentials_path):
        """Initialize with Google Drive API credentials"""
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=['https://www.googleapis.com/auth/drive.readonly']
        )
        self.service = build('drive', 'v3', credentials=self.credentials)
    
    def read_drive_file(self, file_id):
        """Read XLSX file from Google Drive"""
        request = self.service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        file.seek(0)
        return pd.read_excel(file)

    def preprocess_data(self, df):
        """Clean and preprocess the requirements data"""
        # Remove rows with missing values
        df = df.dropna(subset=['Requirement Description', 'Region'])
        
        # Basic text cleaning
        df['Cleaned_Description'] = df['Requirement Description'].str.lower()
        
        # Convert text to TF-IDF features
        vectorizer = TfidfVectorizer(
            stop_words=stopwords.words('english'),
            max_features=1000
        )
        text_features = vectorizer.fit_transform(df['Cleaned_Description'])
        
        # Create dummy variables for regions
        region_dummies = pd.get_dummies(df['Region'], prefix='region')
        
        # Combine features
        features = np.hstack([
            text_features.toarray(),
            region_dummies.values
        ])
        
        return df, features

    def apply_knn_clustering(self, features, n_clusters=5):
        """Apply KNN clustering to the features"""
        # Scale features
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        
        # Apply KNN
        knn = NearestNeighbors(n_neighbors=n_clusters)
        knn.fit(scaled_features)
        
        # Get distances and indices
        distances, indices = knn.kneighbors(scaled_features)
        
        # Assign clusters based on nearest neighbors
        clusters = np.argmin(distances, axis=1)
        
        return clusters

    def apply_pca(self, features):
        """Apply PCA for dimensionality reduction"""
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(features)
        return pca_result

    def create_final_dataframe(self, original_df, pca_result, clusters):
        """Create final DataFrame with PCA components and clusters"""
        df_pca = pd.DataFrame({
            'PCA1': pca_result[:, 0],
            'PCA2': pca_result[:, 1],
            'Region': original_df['Region'],
            'Cluster': clusters
        })
        return df_pca

    def process_requirements(self, file_id, output_path):
        """Main processing pipeline"""
        # Read data
        df = self.read_drive_file(file_id)
        
        # Preprocess
        df_cleaned, features = self.preprocess_data(df)
        
        # Apply clustering
        clusters = self.apply_knn_clustering(features)
        
        # Apply PCA
        pca_result = self.apply_pca(features)
        
        # Create final DataFrame
        df_pca = self.create_final_dataframe(df_cleaned, pca_result, clusters)
        
        # Export to Excel
        df_pca.to_excel(output_path, index=False)
        
        return df_pca 