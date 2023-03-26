from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 26),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'scrape_reddit_posts',
    default_args=default_args,
    description='Scrape posts from the cryptocurrency subreddit',
    schedule_interval='30 2 * * *',
)

scrape_posts = BashOperator(
    task_id='scrape_posts',
    bash_command='python /path/to/scrape_posts.py',
    dag=dag,
)

scrape_posts
