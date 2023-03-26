# Data Pipeline with Airflow and Python

This project is an example of how to implement a data pipeline in Python using Airflow as a scheduler. The pipeline scrapes posts from the Python subreddit every 4 hours and exports the results to a CSV file with a timestamp in the filename.

Getting Started
To use this project, you will need to have Docker and Docker Compose installed on your machine.

1. Clone this repository to your local machine: 

```shell
git clone https://github.com/your-username/data-pipeline-airflow.git
```

2. Change into the project directory:

```shell
cd data-pipeline-airflow
```

3. Build the Docker image:

```shell
docker-compose build
```

4. Run the Docker container:
```shell
docker-compose up
```


### Customizing the Pipeline
If you want to customize the pipeline to scrape a different subreddit or change the schedule interval, follow these steps:

1. Modify the scrape_posts.py script to use the PRAW library to scrape posts from the desired subreddit. You can also modify the script to scrape comments instead of posts if desired.

2. Modify the schedule_interval argument in the Airflow DAG to change the frequency of the pipeline. The default schedule interval is set to '0 */4 * * *', which runs the pipeline every 4 hours.

3. Since we've changed the script name, make sure to rename the file scrape_tweets.py to scrape_posts.py.

4. Build the Docker image and run the Docker container using the same commands as before


### Exporting the Results
The results of each pipeline execution are exported to a CSV file with a timestamp in the filename. The filename format is reddit_posts_YYYY-MM-DD_HH-MM-SS.csv, where YYYY-MM-DD is the date and HH-MM-SS is the time of the execution.

The CSV files are stored in the data directory inside the Docker container. To access the CSV files on your local machine, you can use the following command:


```shell
docker cp <container_id>:/app/data /path/on/local/machine
```
Replace <container_id> with the ID of the Docker container and /path/on/local/machine with the path to the directory where you want to copy the CSV files.


### Conclusion
This project demonstrates how to build a simple data pipeline in Python using Airflow as a scheduler. By customizing the scrape_posts.py script and the Airflow DAG, you can adapt this pipeline to scrape data from a variety of sources and schedule it to run at any interval you choose.
