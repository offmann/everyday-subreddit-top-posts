# Data Pipeline with Airflow and Python

This project was built using ChatGPT, a large language model trained by OpenAI, based on the GPT-3.5 architecture. The prompts and responses used to create this project were generated entirely by ChatGPT.

### Prompt  
```
I want to implement a project of a data pipeline in Python.   
I want to scrape posts from a subreddit every day and export the results to a CSV file.   
I want to use Airflow as a scheduler and Dockerize the whole thing. Can you help me get started?
```


### Getting Started  
To use this project, you will need to have Docker and Docker Compose installed on your machine.

1. Clone this repository to your local machine: 

```shell
git clone https://github.com/your-username/data-pipeline-airflow.git
```

2. Change into the project directory:

```shell
cd data-pipeline-airflow
```

3. Build the Docker image using the Dockerfile. You can use the following command to build the Docker image in the directory containing the Dockerfile:

```shell
docker build -t <image_name> .
```
Replace image_name with a name of your choice.

4. Set your Reddit authentication credentials as environment variables when running the Docker container. You can use the following command to run the Docker container with environment variables:
```shell
docker run -e REDDIT_CLIENT_ID=<your client ID> -e REDDIT_CLIENT_SECRET=<your client secret> -e REDDIT_USERNAME=<your Reddit username> -e REDDIT_PASSWORD=<your Reddit password> -v /path/to/export/directory:/app/export <image_name>
```

Replace your client ID, your client secret, your Reddit username, and your Reddit password with your actual Reddit authentication credentials. Replace /path/to/export/directory with the path to the directory on your local machine where you want to export the CSV files. Replace image_name with the name you chose in step 3.

The script will be executed every day according to the Airflow scheduler. The CSV files will be exported to the ```/path/to/export/directory``` directory on your local machine.
  
 Make sure to include any additional setup or configuration steps that may be necessary, such as setting up the Airflow scheduler or installing any required Python packages


### Customizing the Pipeline
If you want to customize the pipeline to scrape a different subreddit or change the schedule interval, follow these steps:

1. Modify the scrape_posts.py script to use the PRAW library to scrape posts from the desired subreddit. You can also modify the script to scrape comments instead of posts if desired.

2. Modify the schedule_interval argument in the Airflow DAG to change the frequency of the pipeline. The default schedule interval is set to '30 2 * * *', which runs the pipeline every day at 2:30.

3. Since we've changed the script name, make sure to rename the file scrape_tweets.py to scrape_posts.py.

4. Build the Docker image and run the Docker container using the same commands as before


### Exporting the Results
The results of each pipeline execution are exported to a CSV file with a timestamp in the filename. The filename format is ```reddit_posts_YYYY-MM-DD_HH-MM-SS.csv``` where YYYY-MM-DD is the date and HH-MM-SS is the time of the execution.

The CSV files are stored in the data directory inside the Docker container. To access the CSV files on your local machine, you can use the following command:


```shell
docker cp <container_id>:/app/data /path/on/local/machine
```
Replace <container_id> with the ID of the Docker container and /path/on/local/machine with the path to the directory where you want to copy the CSV files.


### Conclusion
This project demonstrates how to build a simple data pipeline in Python using Airflow as a scheduler. By customizing the scrape_posts.py script and the Airflow DAG, you can adapt this pipeline to scrape data from a variety of sources and schedule it to run at any interval you choose.
