# YouTube Popularity Analysis

This project analyzes the popularity of YouTube videos using data science techniques. The dataset includes various features such as video titles, descriptions, likes, comment counts, and upload dates. The project aims to predict the most popular videos using machine learning algorithms and visualize the results.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model and Analysis](#model-and-analysis)
- [Visualization](#visualization)
- [Future Work](#future-work)
- [Contributors](#contributors)

## Overview
YouTube has a vast amount of content uploaded daily, and predicting which videos will become popular is a challenging task. This project uses various machine learning techniques to predict the popularity of videos based on factors like views, likes, comments, etc. The analysis is done using Python libraries such as Pandas, Scikit-learn, and Matplotlib.

## Features
- Scrapes YouTube video data using tools like `BeautifulSoup`, `Selenium`, and YouTube API.
- Data includes video titles, descriptions, likes, comment counts, and upload dates.
- Predicts video popularity using machine learning models such as RandomForestClassifier.
- Visualizes video popularity predictions with graphs and plots.

## Dataset
The dataset is created by scraping YouTube using multiple tools:
- **YouTube API**: Extracts video details.
- **BeautifulSoup and Selenium**: For scraping additional video data like titles and descriptions.
- **Microsoft Power Automate**: Automated browser actions for data collection.

### Key features in the dataset:
- Video Title
- Channel Name
- Views
- Likes
- Comment Count
- Upload Date

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/youtube-popularity-analysis.git
    cd youtube-popularity-analysis
    ```

2. **Install dependencies:**
    Create a virtual environment (optional) and install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

    Requirements include:
    - Flask
    - Pandas
    - Scikit-learn
    - Matplotlib
    - Selenium
    - BeautifulSoup

3. **Set up the project:**
    - Configure `app.py` and the templates (`index.html`, `clustering.html`, `wordcloud.html`) as needed.

## Usage

### Running the Application
1. To run the Flask app in a local environment, execute:
    ```bash
    python app.py
    ```
2. Open a browser and navigate to `http://127.0.0.1:5000` to access the app's dashboard.

### Data Scraping
- Use `scraper.py` to scrape YouTube data using Selenium and BeautifulSoup.
- Use YouTube API in `youtube_analysis.py` for extracting video details programmatically.

## Model and Analysis

The project uses the **RandomForestClassifier** to predict video popularity. The model is trained on features such as views, likes, and comment count.

```python
from sklearn.ensemble import RandomForestClassifier

# Example model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predicting popular videos
predictions = model.predict(X_test)
