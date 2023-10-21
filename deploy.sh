#!/bin/bash

# Source environment variables (PROJECT_DIR) from settings_local.py
source GlitchGuru/settings_local.py

# Define project-specific variables
REQUIREMENTS_FILE="${PROJECT_DIR}/requirements.txt"
FIXTURES_FILE="${PROJECT_DIR}/bug_hub/bugs.json"
MANAGE_PY="${PROJECT_DIR}/manage.py"
DJANGO_SETTINGS_MODULE="GlitchGuru.settings"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

# Activate the virtual environment
source "${VENV_DIR}/bin/activate"

# Pull, install
git pull -X theirs origin main
pip install -r $REQUIREMENTS_FILE

# Run
python $MANAGE_PY makemigrations --settings=$DJANGO_SETTINGS_MODULE
python $MANAGE_PY migrate --settings=$DJANGO_SETTINGS_MODULE
python $MANAGE_PY loaddata $FIXTURES_FILE --settings=$DJANGO_SETTINGS_MODULE
python $MANAGE_PY collectstatic --noinput --settings=$DJANGO_SETTINGS_MODULE

# restart server
touch /var/www/your_domain_wsgi.py

python $MANAGE_PY test --settings=$DJANGO_SETTINGS_MODULE

# Perform a health check for the deployment
status_code=$(curl -s -o /dev/null -w "%{http_code}" http://Niloth.pythonanywhere.com)
if [ $status_code -eq 200 ]; then
    echo "Deployment health check: OK"
else
    echo "Deployment health check: Failed (Status Code: $status_code)"
fi

# Implement a rollback mechanism if something goes wrong during deployment
# TODO

# Deactivate the virtual environment to exit cleanly
deactivate
