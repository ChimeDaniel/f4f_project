# # create constraint url
# AIRFLOW_VERSION=3.1.3
# PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
# CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# # use url to pip install airflow
# pip install "apache-airflow[celery]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# set working directory
export AIRFLOW_HOME=$(pwd)/airflow
mkdir -p $AIRFLOW_HOME  

# initialize airflow
airflow standalone

# run this to connect Airflow to our Postgres database
airflow connections add "f4f_db" \
  --conn-uri "postgresql://postgres:password@localhost:5432/f4f_db"
