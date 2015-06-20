#!/bin/bash

# Recolectar todos los archivos estaticos
cd ../
echo "----Recolectando archivos del sistema----"
#django-admin.py collectstatic --noinput --pythonpath='../' --settings=sgpa.settings_produccion
#if [ "$?" -ne 0 ]
#then
#    echo -e "ERROR: No se pudo recolectar los archivos estaticos"
#    exit 1
#fi

# Borrar los archivos anteriores
echo -e "\nBorrando archivos antiguos"
sudo rm -r /var/www/sgpa2015/
if [ "$?" -ne 0 ]
then
    echo -e "ERROR: No se pudieron borrar los archivos del directorio /var/www/zarPm/"
    exit 1
fi
echo -e "Archivos borrados\n"

# TODO: Eliminar al desinstalar la aplicacion
# Copiar los archivos al directorio servido por apache2
echo "Copiando archivos"
sudo cp -r /home/chelox/PycharmProjects/sgpa2015/ /var/www/sgpa2015/
if [ "$?" -ne 0 ]
then
    echo -e "ERROR: No se pudo copiar el directorio /home/chelox/PycharmProjects/sgpa2015 a /var/www/sgpa2015"
    exit 1
fi
sudo chown -R www-data:www-data /var/www/*
sudo chmod -R 777 /var/www/*
if [ "$?" -ne 0 ]
then
    echo -e "ERROR: No se pudo cambiar el duenho del directorio /var/www/sgpa2015"
    exit 1
fi
#sudo chgrp -R chelox /var/www
if [ "$?" -ne 0 ]
then
    echo -e "ERROR: No se pudo cambiar el grupo del directorio /var/www/sgpa2015"
    exit 1
fi
echo -e "Archivos copiados\n"

# TODO: Eliminar al desinstalar la aplicacion
echo -e "----Configurando Apache----"
sudo mv /var/www/sgpa2015/conf/sgpa2015.com.conf /etc/apache2/sites-available/
if [ "$?" -ne 0 ]
then
    echo -e "ERROR: No se mover los archivos de configuracion desde /var/www/sgpa2015/conf/ a /etc/apache2/sites-available"
    exit 1
fi
sudo rm -r /var/www/sgpa2015/conf
if [ "$?" -ne 0 ]
then
    echo -e "ERROR: No se pudo borrar el directorio /var/www/sgpa2015/conf/"
    exit 1
fi
echo -e "Activando los sitios [sgpa2015] en Apache"
sudo a2ensite sgpa2015.com.conf
if [ "$?" -ne 0 ]
then
    echo -e "ERROR: No se pudo activar el sitio sgpa2015.com.conf"
    exit 1
fi
#a2ensite staticSgpa2015.com.conf
#if [ "$?" -ne 0 ]
#then
#    echo -e "ERROR: No se pudo activar el sitio staticZarPm.conf"
#    exit 1
#fi

echo -e "Recargando Apache"
sudo service apache2 restart
if [ "$?" -ne 0 ]
then
    echo -e "ERROR: No se pudo recargar el servicio apache2"
    exit 1
fi

# TODO: Verificar si estos datos en /etc/hosts antes de agregarlos, actualmente se agregan cada vez que se ejecuta el archivo
# TODO: Eliminar al desinstalar la aplicacion
sudo echo -e "----Fix[sin DNS]: Agrega el nombre y direccion de la pagina a los hosts conocidos de la maquina.----"
sudo echo "127.0.0.1 sgpa2015.com" >> /etc/hosts
#echo "127.0.0.1 static-zarpm.org" >> /etc/hosts

cd /home/chelox/PycharmProjects/sgpa2015
./scriptPoblacionBd.sh
clear
echo "----Fin----"
exit 0
