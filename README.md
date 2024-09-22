<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Popularity Analysis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #eee;
            padding: 2px 5px;
            border-radius: 5px;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>YouTube Popularity Analysis</h1>
    <p>This project analyzes the popularity of YouTube videos using data science techniques. The dataset includes various features such as video titles, descriptions, likes, comment counts, and upload dates. The project aims to predict the most popular videos using machine learning algorithms and visualize the results.</p>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#dataset">Dataset</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#model">Model and Analysis</a></li>
        <li><a href="#visualization">Visualization</a></li>
        <li><a href="#future-work">Future Work</a></li>
        <li><a href="#contributors">Contributors</a></li>
    </ul>

    <h2 id="overview">Overview</h2>
    <p>YouTube has a vast amount of content uploaded daily, and predicting which videos will become popular is a challenging task. This project uses various machine learning techniques to predict the popularity of videos based on factors like views, likes, comments, etc. The analysis is done using Python libraries such as Pandas, Scikit-learn, and Matplotlib.</p>

    <h2 id="features">Features</h2>
    <ul>
        <li>Scrapes YouTube video data using tools like BeautifulSoup, Selenium, and YouTube API.</li>
        <li>Data includes video titles, descriptions, likes, comment counts, and upload dates.</li>
        <li>Predicts video popularity using machine learning models such as <code>RandomForestClassifier</code>.</li>
        <li>Visualizes video popularity predictions with graphs and plots.</li>
    </ul>

    <h2 id="dataset">Dataset</h2>
    <p>The dataset is created by scraping YouTube using multiple tools:</p>
    <ul>
        <li><b>YouTube API</b>: Extracts video details.</li>
        <li><b>BeautifulSoup and Selenium</b>: For scraping additional video data like titles and descriptions.</li>
        <li><b>Microsoft Power Automate</b>: Automated browser actions for data collection.</li>
    </ul>
    <p>Key features in the dataset:</p>
    <ul>
        <li>Video Title</li>
        <li>Channel Name</li>
        <li>Views</li>
        <li>Likes</li>
        <li>Comment Count</li>
        <li>Upload Date</li>
    </ul>

    <h2 id="installation">Installation</h2>
    <p>To run this project locally, follow these steps:</p>

    <pre><code>git clone https://github.com/yourusername/youtube-popularity-analysis.git
cd youtube-popularity-analysis</code></pre>

    <p>Install dependencies: Create a virtual environment (optional) and install the required Python libraries:</p>
    <pre><code>pip install -r requirements.txt</code></pre>
    <p>Requirements include:</p>
    <ul>
        <li>Flask</li>
        <li>Pandas</li>
        <li>Scikit-learn</li>
        <li>Matplotlib</li>
        <li>Selenium</li>
        <li>BeautifulSoup</li>
    </ul>

    <h2 id="usage">Usage</h2>
    <h3>Running the Application</h3>
    <p>To run the Flask app in a local environment, execute:</p>
    <pre><code>python app.py</code></pre>
    <p>Open a browser and navigate to <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a> to access the app's dashboard.</p>

    <h3>Data Scraping</h3>
    <ul>
        <li>Use <code>scraper.py</code> to scrape YouTube data using Selenium and BeautifulSoup.</li>
        <li>Use YouTube API in <code>youtube_analysis.py</code> for extracting video details programmatically.</li>
    </ul>

    <h2 id="model">Model and Analysis</h2>
    <p>The project uses the <code>RandomForestClassifier</code> to predict video popularity. The model is trained on features such as views, likes, and comment count.</p>

    <pre><code>from sklearn.ensemble import RandomForestClassifier

# Example model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predicting popular videos
predictions = model.predict(X_test)
</code></pre>

    <h2 id="visualization">Visualization</h2>
    <p>Visualization of the predictions is done using Matplotlib to generate graphs, plots, and other visual insights.</p>

    <h2 id="future-work">Future Work</h2>
    <p>Further improvements to this project could include using more advanced machine learning techniques, expanding the dataset, and integrating more data sources to enhance prediction accuracy.</p>

    <h2 id="contributors">Contributors</h2>
    <p>Feel free to contribute to this project by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.</p>
</div>

</body>
</html>
