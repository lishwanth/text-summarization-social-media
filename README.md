# Text Summarization for Social Media Management

## Project Overview
This project provides an end-to-end solution for automating the summarization of long-form content, such as blog posts or articles, and posting the summaries on social media platforms like Twitter. The project is designed using open-source tools and follows object-oriented programming (OOP) principles to ensure modularity, scalability, and maintainability.

## Features
- **Content Scraping:** Scrape content from websites using `BeautifulSoup` and `requests`.
- **Text Summarization:** Utilize the T5 model from Hugging Face Transformers for summarizing long-form content.
- **Social Media Automation:** Post the generated summaries automatically to Twitter using the `Tweepy` library.
- **Logging:** Record all actions, including posted summaries, in an SQLite database for tracking and auditing.
- **Containerization:** Dockerize the application for easy deployment and scalability.
- **CI/CD:** Implement continuous integration and deployment using GitHub Actions.

## Project Structure

```
text-summarization-social-media/
│
├── data/
│   └── raw/
│       └── articles.csv                # Raw data for training
│
├── notebooks/
│   ├── data_preprocessing.ipynb        # Jupyter Notebook for data preprocessing and exploration
│   └── model_training.ipynb            # Jupyter Notebook for training the summarization model
│
├── models/
│   └── summarization_model/            # Directory where the trained model will be saved
│
├── src/
│   ├── content_scraper.py              # Module for scraping web content
│   ├── summarizer.py                   # Module for summarization using the T5 model
│   ├── social_media_manager.py         # Module for interacting with social media APIs (e.g., Twitter)
│   ├── logger.py                       # Module for logging actions to an SQLite database
│   ├── main.py                         # Main script to orchestrate the entire workflow
│   └── utils.py                        # Utility functions (e.g., directory creation, logging setup)
│
├── .github/
│   └── workflows/
│       └── main.yml                    # GitHub Actions workflow for CI/CD
│
├── Dockerfile                          # Docker configuration for containerizing the application
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
└── LICENSE                             # Open-source license
```

## Tools and Technologies Used

- **Programming Language:** Python 3.8+
- **Content Scraping:**
  - `BeautifulSoup`: A Python library for parsing HTML and extracting data from web pages.
  - `requests`: A Python HTTP library for making requests to web pages.

- **Text Summarization:**
  - `Hugging Face Transformers`: A library for state-of-the-art Natural Language Processing (NLP) models like T5, BERT, GPT, etc.
  - `PyTorch`: A deep learning framework used by the Hugging Face Transformers library for model training.

- **Social Media Integration:**
  - `Tweepy`: A Python library for accessing the Twitter API.

- **Logging:**
  - `SQLite`: A lightweight, disk-based database used for logging actions and tracking posted summaries.

- **Containerization:**
  - `Docker`: A platform used to containerize the application for consistent deployment across different environments.

- **CI/CD:**
  - `GitHub Actions`: A CI/CD platform provided by GitHub to automate testing, building, and deploying applications.

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Docker (for containerization)
- GitHub account (for CI/CD with GitHub Actions)
- Twitter Developer account (for API keys)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/text-summarization-social-media.git
   cd text-summarization-social-media
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add your Twitter API keys:
   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   ```

4. **Run the main script:**
   ```bash
   python src/main.py
   ```

## Usage

- **Scrape and Summarize Content:** The application will scrape content from a specified URL, generate a summary using the trained T5 model, and automatically post it to Twitter.
- **Logging:** All posted summaries and actions are logged into an SQLite database, which can be reviewed later.

## Containerization with Docker

1. **Build the Docker image:**
   ```bash
   docker build -t text-summarization-social-media .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -d --env-file .env text-summarization-social-media
   ```

## CI/CD with GitHub Actions

The project includes a GitHub Actions workflow (`.github/workflows/main.yml`) that automates the process of testing, building, and deploying the application.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please reach out via GitHub or email at lishwanthkumar@gmail.com.
