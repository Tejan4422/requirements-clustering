from requirements_clustering import RequirementsAnalyzer

def main():
    # Initialize analyzer with credentials file
    credentials_path = 'path/to/your/credentials.json'
    analyzer = RequirementsAnalyzer(credentials_path)
    
    # Process requirements
    file_id = 'your_google_drive_file_id'
    output_path = 'output/clustered_requirements.xlsx'
    
    df_pca = analyzer.process_requirements(file_id, output_path)
    print(f"Processing complete. Results saved to {output_path}")
    
if __name__ == "__main__":
    main() 