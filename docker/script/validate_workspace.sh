validate_version_with_pip() {
  if [[ $(pip3 show "$1" | grep 'Version' | grep -o '[0-9].*') != "$2" ]]
  then
    echo "Validation Error: $1 version $2 expected"
  fi
}

# Check health of airflow webserver
curl --fail http://localhost:8080

# Check health of postgres service
pg_isready -U airflow

# Validate sqlite version
validate_version_with_pip "apache-airflow-providers-sqlite" "3.4.1"

# Validate pandas version
validate_version_with_pip "pandas" "1.5.2"
