runserver:
    python manage.py runserver

check:
    python manage.py check

shell:
    python manage.py shell

clean:
    find . -name '*.pyc' -exec rm {} \;

makemigrations app:
    python manage.py makemigrations {{ app }}

migrate:
    python manage.py migrate

startapp app:
    python manage.py startapp {{ app }}

sql app migration_id:
    python manage.py sqlmigrate {{ app }} {{ migration_id }}

createsu:
    python manage.py createsuperuser

dumpdata output:
    python manage.py dumpdata --indent=2 --output={{ output }}

loaddata input:
    python manage.py loaddata {{ input }}
