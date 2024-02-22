# Mi Proyecto Django

Este proyecto sigue el patrón MVT y utiliza Django para crear un sistema web con las siguientes características:

1. **Orden de Pruebas:**
   - Insertar Datos: Accede a la URL "/insertar/" para ingresar datos a las clases.
   - Buscar Datos: Accede a la URL "/buscar/" para buscar datos en la base de datos.

2. **Funcionalidades:**
   - **Insertar Datos:**
      - URL: /insertar/
      - Formularios disponibles para cliente, envio y producto.


# Ejecución del Proyecto

Para ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio.
2. Crea un entorno virtual.
3. Instala las dependencias con `pip install -r requirements.txt`.
4. Ejecuta las migraciones con `python manage.py migrate`.
5. Inicia el servidor con `python manage.py runserver`.

# Acceso a la Página de Administración

- URL: http://localhost:8000/admin/
- Utiliza las credenciales del superusuario para acceder y verificar los datos ingresados.
