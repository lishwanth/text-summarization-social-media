# Text Summarization for Social Media Management

## Project Overview
This project provides an end-to-end solution for summarizing long-form content, such as blog posts or articles, and automatically posting the summaries to social media platforms like Twitter. The project is built using open-source tools and follows object-oriented programming principles for modularity and scalability.

## Features
- **Content Scraping:** Scrape content from the web using BeautifulSoup.
- **Text Summarization:** Summarize long-form content using the T5 model from Hugging Face.
- **Social Media Automation:** Automatically post summaries to Twitter.
- **Logging:** Log all posts to an SQLite database for tracking and auditing.

## Project Structure
```
text-summarization-social-media/
│
├── data/
│   └── raw/
│       └── articles.csv                # Raw data for training
│
├── notebooks/
│   ├── data_preprocessing.ipynb        # Notebook for data preprocessing
│   └── model_training.ipynb            # Notebook for model training
│
├── models/
│   └── summarization_model/            # Trained model will be saved here
│
├── src/
│   ├── content_scraper.py              # Web scraping and content extraction
│   ├── summarizer.py                   # Summarization logic using Hugging Face Transformers
│   ├── social_media_manager.py         # Social media API integration
│   ├── logger.py                       # Logging to SQLite
│   ├── main.py                         # Main script to orchestrate the process
│   └── utils.py                        # Utility functions
│
├── .github/
│   └── workflows/
│       └── main.yml                    # GitHub Actions CI/CD configuration
│
├── Dockerfile                          # Docker configuration for containerization
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
└── LICENSE                             # Open-source license
```

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Docker (for containerization)
- GitHub account (for CI/CD with GitHub Actions)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-summarization-social-media.git
   cd text-summarization-social-media
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables for Twitter API keys in a `.env` file:
   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   ```

4. Run the main script:
   ```bash
   python src/main.py
   ```

## Usage
- **Scrape and Summarize Content:** The script will scrape content from a specified URL, generate a summary, and post it to Twitter.
- **Logging:** All actions are logged into an SQLite database for review.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
