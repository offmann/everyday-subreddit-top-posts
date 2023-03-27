import praw
import pandas as pd
from datetime import datetime


# Authenticate with the Reddit API
client_id = os.environ['REDDIT_CLIENT_ID']
client_secret = os.environ['REDDIT_CLIENT_SECRET']

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='your_user_agent')

# Define the subreddit to search for
subreddit_name = 'Cryptocurrency'
subreddit = reddit.subreddit(subreddit_name)

# Scrape the top 50 posts from the subreddit
posts = subreddit.top(limit=50)

# Convert the post data into a Pandas DataFrame
data = []
for post in posts:
    data.append([post.created_utc, post.author, post.title, post.selftext, post.score, post.num_comments])

columns = ['created_utc','author','title','selftext','score','num_comments']    
df = pd.DataFrame(data, columns=columns).sort_values(by='score', ascending=False)

# Generate the filename with timestamp
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f'reddit_posts_{timestamp}.csv'

# Export the DataFrame to a CSV file with the timestamp in the filename
df.to_csv(filename, index=False)
