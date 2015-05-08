psql -h localhost postgres -W -f dropAndCreate.sql postgres


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

./manage.py shell < poblacion.py