# IEB - Test Autenticacion Usuario & Interfaz de Trabajo 

Interfaz de Trabajo con Autenticación de Usuario, El Proyecto se realiza en respuesta a la prueba técnica para desarrollador de Software a la empresa IEB-Ingeniería Especializada, La Aplicación esta construida en Django 4.1 gestionado por PostgreSQL 12.1

## Informacion Preliminar 🚀

IEB-TestProyect es un API de Trabajo con Autenticación de Usuario por lo cual deberá emplear un Usuario autorizado para ingresar a la plataforma de trabajo, a continuación se proporciona una lista de usuarios y superusuario con el cual podrá explorar todas las características del proyecto. 

SuperUsuario📌 
Usuario: ieb
Contraseña: uUET2m19!mC&

Usuario: juan.cobo
Contraseña: Jun@

Usuario: Esmeralda.gutierrez
Contraseña: Es*45

Usuario: Jake.grajales
Contraseña: Jak180

Nota: EL proyecto ha suprimido intencionalmente los validadores de contraseña para adaptarse a las contraseñas de baja seguridad suministradas en la prueba, si desea activar los validadores deberá restaurar el parámetro AUTH_PASSWORD_VALIDATORS

### PreRequisitos 📋

Los requerimientos básicos para visualizar el proyecto los encontrara en el archivo "requirements.txt" use el administrador de paquetes de python pip para instalar los especificaciones del proyecto, adicional a esto se deberá contar con los siguientes elementos.

-WSL/Linux
-Python 3.8
-PostgreSQL 12.1

### Instalación 🔧

Inicialmente se debe posicionar en el directorio de trabajo, posteriormente se debe crear el entorno de desarrollo y clonar el repositorio de Github, a continuación se describe paso a paso el proceso de Instalación.

Una vez este en el directorio de su preferencia creamos el directorio de trabajo y procedemos configurar el proyecto, la siguiente secuencia de comandos asume Linux o WSL como SO

sudo apt update
sudo apt-get install postgresql postgresql-contrib
psql --version (Verificación Instalación)

sudo service postgresql start
sudo -u postgres psql
    CREATE DATABASE "dbieb";

git clone git@github.com:savelasquezo/IEB.git

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd IEBTestProyect
python3 manage.py makemigrations
python3 manage.py migrate
python3 generate_data.py

python3 manage.py runserver

Importante: EL proyecto ofrece la posibilidad de crear automáticamente los registros en la base de datos especificados en la prueba técnica, para ello deberá emplear "python3 generate_data.py" antes de realizar cualquier registro en la base de datos, este mismo creará un Superusuario con el cual podrá administrar el proyecto. 

### Exploracion 💥

Finalizado el proceso de Instalación, tendremos acceso tanto al panel Administrativo como a la interfaz de Autenticación y Área de Trabajo, para explorar debemos hacer uso de los datos de inicio de sesión previamente suministrados.

Administrador: http://127.0.0.1:8000/ieb/ (Localhost)
Área de Trabajo: http://127.0.0.1:8000/   (Localhost)

## Autor ✒️
* **Simon Velasquez** - [savelasquezo](https://github.com/savelasquezo)
