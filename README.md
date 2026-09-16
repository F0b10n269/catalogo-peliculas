#  Catálogo de peliculas - Prueba Formativa Django

Este proyecto corresponde a la **Prueba Formativa: mi primer sitio en Django** para la asignatura **TI3041 Programación Back End**. Consiste en una aplicación web básica construida desde cero que despliega un catálogo de elementos estáticos mediante el uso de vistas basadas en funciones, enrutamiento con parámetros, herencia de plantillas y archivos estáticos, prescindiendo totalmente de modelos o bases de datos relacionales.

---

##  Stack Tecnológico
* **Python 3.13**
* **Django 5.2**
* **Git & GitHub**

---

##  Instrucciones de Instalación y Ejecución

Sigue estos pasos detallados para clonar el repositorio y levantar el servidor de desarrollo local en tu equipo:

### 1. Clonar el repositorio
Abre una terminal en tu equipo, posiciónate en la carpeta que desees y ejecuta:
```bash
git clone https://github.com
cd TU_REPOSITORIO
```

### 2. Crear y activar el entorno virtual `.venv`
* **En macOS/Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
* **En Windows (Command Prompt / PowerShell):**
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```

### 3. Instalar las dependencias del proyecto
Asegúrate de que tu entorno virtual esté activo (verás un `(.venv)` al inicio de la línea de comandos) e instala los paquetes necesarios registrados en el archivo de requerimientos:
```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones iniciales de Django
Aunque este proyecto no utiliza modelos propios ni bases de datos personalizadas, es necesario correr las migraciones del sistema base de Django (sesiones, autenticación interna, etc.):
```bash
python manage.py migrate
```

### 5. Iniciar el servidor de desarrollo
Levanta el servidor local con el siguiente comando:
```bash
python manage.py runserver
```

Una vez iniciado, abre tu navegador web favorito e ingresa a la dirección local de desarrollo:  
 **[http://127.0.0](http://127.0.0)**

---

##  Declaración de Uso de IA
*De acuerdo con la sección 6 de las reglas del proyecto:*  
**Uso de IA:** Se utilizó un asistente de IA para estructurar el esqueleto inicial de los archivos de vistas (`views.py`) y plantillas de herencia HTML, modificando posteriormente las rutas internas, los textos de los elementos del catálogo y aplicando estilos CSS personalizados propios.
