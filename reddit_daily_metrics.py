import pandas as pd
from datetime import datetime, timedelta
import glob

# Set date range for daily metrics
today = datetime.today().date()
yesterday = today - timedelta(days=1)

# Load all CSV files for the date range
file_pattern = f"reddit_posts_{yesterday.strftime('%Y-%m-%d')}*.csv"
files = glob.glob(file_pattern)

# Concatenate data from all CSV files
df = pd.concat([pd.read_csv(f) for f in files])

# Compute daily metrics
total_posts = len(df)
subreddit_counts = df['subreddit'].value_counts().head(10)
avg_upvotes = df['upvotes'].mean()
avg_comments = df['comments'].mean()
max_upvotes = df.loc[df['upvotes'].idxmax()]
max_comments = df.loc[df['comments'].idxmax()]
avg_score = df['score'].mean()
top_users = df['author'].value_counts().head(10)
post_times = pd.cut(df['created_utc'].dt.hour, bins=[0, 6, 12, 18, 24], labels=['Night', 'Morning', 'Afternoon', 'Evening'])
word_counts = df['title'].str.split(expand=True).stack().value_counts().head(10)

# Create dataframe of daily metrics
metrics = pd.DataFrame({
    'Date': [yesterday],
    'Total Posts': [total_posts],
    'Top Subreddits': [subreddit_counts],
    'Avg Upvotes': [avg_upvotes],
    'Avg Comments': [avg_comments],
    'Most Upvoted Post': [max_upvotes['title']],
    'Most Upvoted Post Author': [max_upvotes['author']],
    'Most Upvoted Post Score': [max_upvotes['score']],
    'Most Commented Post': [max_comments['title']],
    'Most Commented Post Author': [max_comments['author']],
    'Most Commented Post Comments': [max_comments['comments']],
    'Avg Score': [avg_score],
    'Top Users': [top_users],
    'Post Times': [post_times.value_counts()],
    'Top Words': [word_counts]
})

# Save daily metrics to CSV file
filename = f"reddit_daily_metrics_{yesterday.strftime('%Y-%m-%d')}.csv"
metrics.to_csv(filename, index=False)
