import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path, encoding='Windows-1252')
    df['Upload_date'] = pd.to_datetime(df['Upload_date'])
    le = LabelEncoder()
    df['Search_key_encoded'] = le.fit_transform(df['Search_Key'])
    df.fillna(0, inplace=True)
    df['popularity_score'] = df['Views'] + (df['Likes'] * 10) + (df['Comment']*50)
    return df, le

def train_model(df):
    X = df[['Views', 'Likes', 'Comment', 'Search_key_encoded']]
    y = df['popularity_score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    df['predicted_popularity_score'] = model.predict(X)
    return df, model
