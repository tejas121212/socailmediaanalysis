import pandas as pd
import matplotlib.pyplot as plt

def instagram():
    # Load the dataset
    file_path = "D:/SEM 2/Social media data set project/2023-07/instagram_top_50_2023-07-03.csv"  # Update with your actual file path
    df = pd.read_csv(file_path)
    print("Column Names:", df.columns)
    print(df.head())

    # Calculate engagement rate
    df['engagement_rate'] = (df['comments']) / df['followers']
    print(df[['date', 'engagement_rate']].head())

    # Plot engagement rate over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['engagement_rate'], marker='o', label='Instagram')
    plt.xlabel('Date')
    plt.ylabel('Engagement Rate')
    plt.title('Instagram Engagement Rate Over Time')
    plt.legend()
    plt.show()

def tiktok():
    # Load the dataset
    file_path = "D:/SEM 2/Social media data set project/2023-07/tiktok_top_50_2023-07-03.csv"  # Update with your actual file path
    df2 = pd.read_csv(file_path)
    print("TikTok Dataset Columns:", df2.columns)
    print(df2.head())

    # Calculate engagement rate
    df2['engagement_rate'] = (df2['comments']) / df2['followers']
    print(df2[['date', 'engagement_rate']].head())

    # Plot engagement rate over time
    plt.figure(figsize=(10, 6))
    plt.plot(df2['date'], df2['engagement_rate'], marker='x', label='TikTok')
    plt.xlabel('Date')
    plt.ylabel('Engagement Rate')
    plt.title('TikTok Engagement Rate Over Time')
    plt.legend()
    plt.show()

def twitter():
    # Load the dataset
    file_path = "D:/SEM 2/Social media data set project/2023-07/twitter_top_50_2023-07-03.csv"  # Update with your actual file path
    df3 = pd.read_csv(file_path)
    print("Twitter Dataset Columns:", df3.columns)
    print(df3.head())

    # Calculate engagement rate
    df3['engagement_rate'] = (df3['comments']) / df3['followers']
    print(df3[['date', 'engagement_rate']].head())

    # Plot engagement rate over time
    plt.figure(figsize=(10, 6))
    plt.plot(df3['date'], df3['engagement_rate'], marker='s', label='Twitter')
    plt.xlabel('Date')
    plt.ylabel('Engagement Rate')
    plt.title('Twitter Engagement Rate Over Time')
    plt.legend()
    plt.show()

def youtube():
    # Load the dataset
    file_path = "D:/SEM 2/Social media data set project/2023-07/youtube_top_50_2023-07-03.csv"  # Update with your actual file path
    df4 = pd.read_csv(file_path)
    print("YouTube Dataset Columns:", df4.columns)
    print(df4.head())

    # Calculate engagement rate
    df4['engagement_rate'] = (df4['comments']) / df4['followers']
    print(df4[['date', 'engagement_rate']].head())

    # Plot engagement rate over time
    plt.figure(figsize=(10, 6))
    plt.plot(df4['date'], df4['engagement_rate'], marker='^', label='YouTube')
    plt.xlabel('Date')
    plt.ylabel('Engagement Rate')
    plt.title('YouTube Engagement Rate Over Time')
    plt.legend()
    plt.show()

# Call the functions to execute the calculations and visualizations
instagram()
tiktok()
twitter()
youtube()
