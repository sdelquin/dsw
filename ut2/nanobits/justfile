# I ❤️ just
# https://github.com/casey/just

# Run development server.
runserver: kill-runservers
    ./manage.py runserver

# Open a Django interactive shell.
sh:
    ./manage.py shell

# Check Django project
check:
    ./manage.py check

alias mm := mmigrate

# Generate migrations
mmigrate app="":
    ./manage.py makemigrations {{ app }}

alias m := migrate

# Migrate models
migrate app="":
    ./manage.py migrate {{ app }}

# https://medium.com/@mustahibmajgaonkar/how-to-reset-django-migrations-6787b2a1e723
# https://stackoverflow.com/a/76300128
# Remove migrations and database. Reset DB artefacts.
[confirm("⚠️ All migrations and database will be removed. Continue? [yN]:")]
reset-db:
    #!/usr/bin/env bash
    find . -path "*/migrations/*.py" ! -path "./.venv/*" ! -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc" ! -path "./.venv/*" -delete
    rm -f db.sqlite3
    ./manage.py makemigrations
    ./manage.py migrate
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | ./manage.py shell
    echo
    echo "Creating superuser → admin:admin ... OK"

# Reset admin (admin user must exist!)
@reset-admin password="admin":
    echo "from django.contrib.auth.models import User; u = User.objects.get(username='admin'); u.set_password('{{ password }}'); u.save()" | ./manage.py shell
    echo "✔ Reseted admin account with password '{{ password }}'"

# Download teacher's code and sync with changes.
[confirm("⚠️ Sync with teacher. All your changes will be discarded. Continue? [yN]:")]
sync:
    ghget -o . https://github.com/sdelquin/dsw/tree/main/ut2/nanobits

# Open sqlite project database
db:
    sqlite3 db.sqlite3

# Show sqlite DB schema for given table
@schema table:
    sqlite3 db.sqlite3 '.schema --indent {{ table }}'

# Kill existent Django "runservers"
[unix]
kill-runservers:
    #!/usr/bin/env bash
    for pid in $(ps aux | grep '[Pp]ython.*manage.py runserver' | awk '{ print $2 }')
    do
        kill -9 $pid
    done
