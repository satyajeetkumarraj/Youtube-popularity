from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load and preprocess data
file_path = "C:\\Users\\HP\\OneDrive\\Documents\\Project Report youtube\\Finaldataset.csv"
df = pd.read_csv(file_path, encoding='Windows-1252')
df['Upload_date'] = pd.to_datetime(df['Upload_date'])
le = LabelEncoder()
df['Search_key_encoded'] = le.fit_transform(df['Search_Key'])
df.fillna(0, inplace=True)
df['popularity_score'] = df['Views'] + (df['Likes'] * 10) + df['Comment']

X = df[['Views', 'Likes', 'Comment', 'Search_key_encoded']]
y = df['popularity_score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
df['predicted_popularity_score'] = model.predict(X)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    search_key = request.args.get('search_key')
    if search_key is not None:
        try:
            search_key_encoded = le.transform([search_key])[0]
            filtered_data = df[df['Search_key_encoded'] == search_key_encoded]
            if not filtered_data.empty:
                most_popular_index = filtered_data['predicted_popularity_score'].idxmax()
                most_popular_video = filtered_data.loc[most_popular_index]
                
                # Convert to JSON-serializable format
                result = {
                    'title': most_popular_video['Titles'],
                    'predicted_score': int(most_popular_video['predicted_popularity_score'])  # Convert to int
                }
                return jsonify(result)
        except ValueError:
            return jsonify({'error': 'Search key not found in the dataset.'})
    return jsonify({'error': 'No search key provided.'})

if __name__ == '__main__':
    app.run(debug=True)
