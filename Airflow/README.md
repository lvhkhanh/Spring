# Airflow
## Docker
### .env
`cp .env /Users/<username>/.env`
`sudo chmod -R 777 ./config`
`docker compose up airflow-init`
`docker compose run airflow-worker airflow info`
`curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.1.8/airflow.sh'
chmod +x airflow.sh`
### Cleanup
`docker compose down --volumes --remove-orphans`
`docker compose down --volumes --rmi all`