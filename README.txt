This is a Python Django framework project.

It requires python3 and MySQL installed on the machine.
Follow the below steps to run it locally.

1. git clone master branch.
git clone https://github.com/ravina-mestry/x21120501_scp_project_propertylisting_web_app.git

2. Update below sections in propertylisting/settings.py
- Enable Debug on local machine.
DEBUG = True

- MySQL DB Configuration.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database_name>',
        'USER': '<mysql_user_name>',
        'PASSWORD': '<mysql_user_password>',
        'HOST': '<hostname>',
        'PORT': '3306',
    }
}

- Receipt API config
RECEIPT_API_URL = '<url>'
RECEIPT_API_TOKEN = '<api token>'

3. Create virtual environment.
cd x21120501_scp_project_propertylisting_web_app

pytho n -m venv propertylisting_web_app_venv
source propertylisting_web_app_venv/bin/activate

pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

4. Populate database
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

5. Run local server
python manage.py runserver 8080
