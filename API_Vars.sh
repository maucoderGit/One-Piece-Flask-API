source venv/bin/activate
pip install -r requirements.txt

export FLASK_APP="main:app"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"

flask run
