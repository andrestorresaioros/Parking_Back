# Parking_Back
# Proyecto de Parqueadero

Este es un proyecto de sistema de gestión de parqueadero desarrollado con Django. Permite la administración de clientes, vehículos, contratos y recibos en un parqueadero.

## Descripción

El proyecto de Parqueadero es una aplicación web que permite gestionar de manera eficiente y automatizada las operaciones diarias de un parqueadero. Proporciona un conjunto de funcionalidades para el registro de clientes, vehículos, contratos de alquiler y generación de recibos.

Con esta aplicación, los administradores del parqueadero pueden realizar las siguientes acciones:

- Registrar y gestionar clientes: Se pueden añadir nuevos clientes al sistema, especificando su nombre, teléfono e identificación. Además, se puede ver y actualizar la información de los clientes existentes.

- Registrar y gestionar vehículos: Se pueden añadir vehículos al sistema, proporcionando información como color, placa, marca, modelo y tipo. Los vehículos se asocian a los clientes correspondientes para llevar un registro preciso.

- Crear contratos de alquiler: Se pueden generar contratos de alquiler para los clientes, definiendo la duración del contrato (por minuto, día, semana, mes o año). Esto permite un control eficiente del tiempo de estacionamiento y cálculo automático del costo correspondiente.

- Generar recibos de estacionamiento: Se registran las entradas y salidas de los vehículos en el parqueadero, generando automáticamente los recibos correspondientes. Los recibos contienen información detallada como la fecha de entrada y salida, ubicación, costo y cliente asociado.

## Requisitos del Sistema

Antes de comenzar, asegúrate de tener los siguientes requisitos en tu sistema:

- Python 3.8 o superior
- Django 3.0 o superior

## Instalación

Sigue estos pasos para instalar y configurar el proyecto:

1. Clona este repositorio en tu máquina local.
2. Crea y activa un entorno virtual para el proyecto.
3. Instala las dependencias del proyecto ejecutando el siguiente comando: `pip install -r requirements.txt`.
4. Realiza las migraciones de la base de datos con el comando: `python manage.py migrate`.
5. Configura cualquier otra configuración específica del proyecto, como claves secretas u otras variables de entorno.

## Uso
Para ejecutar el proyecto localmente, sigue estos pasos:

1. Asegúrate de tener el entorno virtual activado.
2. Ejecuta el servidor de desarrollo de Django con el comando: `python manage.py runserver`.
3. Abre tu navegador web y ve a la dirección: `http://localhost:8000/` para acceder al proyecto.

## Contribución

Si deseas contribuir a este proyecto, sigue los siguientes pasos:

1. Haz un fork de este repositorio.
2. Crea una rama nueva para tu contribución: `git checkout -b nombre-de-la-rama`.
3. Realiza los cambios y añade tus mejoras.
4. Realiza un commit con tus cambios: `git commit -m "Descripción de tus cambios"`.
5. Realiza un push a tu repositorio fork: `git push origin nombre-de-la-rama`.
6. Abre una Pull Request en este repositorio original y describe tus cambios.

## Autor

- Nombre: César Andrés Torres Bernal
- Contacto: cesarandrestorresbernal@gmail.com


