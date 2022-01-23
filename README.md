# dhungeAPI-postgres

Set up postgres db with pg admin

```
// in settings.py inside kanban_app

DATABASES = {
   'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': <dbname>,

        'USER': <db user>,

        'PASSWORD': <db password>,

        'HOST': 'localhost',

        'PORT': '' or '5432' or any port you selected in db,

    }
}

```

```
in root directory: pip install -r requirements.txt
                   cd kanban_app
                   python manage.py makemigrations authapi
                   python manage.py makemigrations boards

```
