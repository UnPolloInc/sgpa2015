#!/bin/bash

# Verifica si existe la configuracion del sphinx
if [ ! -f source/conf.py ]; then
    echo "Configure Sphinx con Pycharm siguiendo los pasos del archivo Sphinx.txt"
    exit
fi

# Crear archivos .rst sobre los modulos
echo "Creando .rst"
sphinx-apidoc -F -o source/ .

# Cambiar el titulo del archivo modules.rst
cd source/
echo -e "\nArreglando 'index.rst'."
sed -i.bak s/^'\.'$/Modulos/ index.rst
sed -i.bak s/^=$/========/ index.rst

# Crear los archivos html
echo -e "Creando archivos html\n"

make html
sphinx-build -b html -d _build/doctrees   . _build/html

echo "Mostramos la documentacion actual"

firefox _build/html/index.html &
if [ $? -ne 0 ]; then
    firefox _build/html/index.html &
fi
