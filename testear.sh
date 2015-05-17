echo 'Ejecutando test de US'
coverage run manage.py test us -v 2

echo 'Ejecutanto test de Clientes'
coverage run manage.py test clientes -v 2


echo 'Ejecutando test de  Usuarios'

coverage run manage.py test usuarios -v 2

echo 'Ejecutando test de Proyectos'

coverage run manage.py test proyectos -v 2

echo 'Ejecutando test de  Sprint'

coverage run manage.py test sprint -v 2


echo 'Ejecutando test de Flujos'

coverage run manage.py test flujos -v 2

echo 'Ejecutando test de Miembros'
coverage run manage.py test miembros -v 2