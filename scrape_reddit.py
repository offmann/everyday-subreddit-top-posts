import praw
import pandas as pd

# Authenticate with the Reddit API
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')

# Define the subreddit to search for
subreddit_name = 'cryptocurrency'
subreddit = reddit.subreddit(subreddit_name)

# Scrape the top 100 posts from the subreddit
posts = subreddit.top(limit=50)

# Convert the post data into a Pandas DataFrame
data = []
for post in posts:
    data.append([post.created_utc, post.author.name, post.title, post.selftext])

df = pd.DataFrame(data, columns=['created_utc', 'author', 'title', 'selftext'])

# Export the DataFrame to a CSV file
df.to_csv('reddit_posts.csv', index=False)
