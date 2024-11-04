# Requirements Clustering Analysis

This project analyzes requirements data from Excel files stored in Google Drive using machine learning techniques. It performs text preprocessing, clustering analysis using K-Nearest Neighbors (KNN), and dimensionality reduction using Principal Component Analysis (PCA).

## Features

- Google Drive integration for reading XLSX files
- Text preprocessing and cleaning
- K-Nearest Neighbors (KNN) clustering
- Principal Component Analysis (PCA) for dimensionality reduction
- Export results to Excel for visualization in Looker Studio

## Prerequisites

- Python 3.8+
- Google Cloud Project with Drive API enabled
- Service account credentials from Google Cloud Console

## Installation

1. Clone the repository: 

bash
git clone https://github.com/Tejan4422/requirements-clustering.git
cd requirements-clustering

2. Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install required packages:

bash
pip install -r requirements.txt

4. Set up Google Drive credentials:
   - Create a project in Google Cloud Console
   - Enable the Google Drive API
   - Create a service account and download the credentials JSON file
   - Place the credentials file in the project root as `credentials.json`

## Usage

1. Configure the input parameters in `config.yaml`:
```yaml
google_drive:
  folder_id: "your_folder_id"
  file_pattern: "*.xlsx"

preprocessing:
  min_words: 3
  max_words: 100
  remove_stopwords: true
  
clustering:
  n_neighbors: 5
  algorithm: "auto"
  metric: "cosine"
```

2. Run the main analysis script:
```bash
python src/main.py
```

3. Find the results in the `output` directory:
   - `clustered_requirements.xlsx`: Requirements with assigned clusters
   - `cluster_statistics.xlsx`: Statistical analysis of clusters
   - `visualization_data.csv`: Data prepared for Looker Studio



## Configuration

The `config.yaml` file allows you to customize:
- Google Drive integration settings
- Text preprocessing parameters
- Clustering algorithm parameters
- Output file locations and formats

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Testing

Run the test suite:
```bash
pytest tests/
```

## Troubleshooting

Common issues and solutions:

1. Google Drive API Authentication:
   - Ensure credentials.json is in the correct location
   - Verify API is enabled in Google Cloud Console
   - Check file permissions in Google Drive

2. Clustering Results:
   - Adjust n_neighbors parameter for different cluster sizes
   - Try different distance metrics (euclidean, manhattan, cosine)
   - Experiment with text preprocessing parameters

3. Memory Issues:
   - Reduce batch size in config.yaml
   - Use chunked processing for large datasets
   - Enable memory monitoring in logging

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- scikit-learn documentation and community
- Google Drive API documentation
- NLTK documentation and tutorials

## Contact

email: tejan.4422@gmail.com
Project Link: [https://github.com/Tejan4422/requirements-clustering](https://github.com/Tejan4422/requirements-clustering)
```

