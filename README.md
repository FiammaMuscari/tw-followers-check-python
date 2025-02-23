# Twitter Basic Stats Bot

Este bot, desarrollado en Python con la librería Tweepy, permite obtener información básica sobre tu cuenta de Twitter, incluyendo:

- Estadísticas generales de la cuenta
- Lista de usuarios que sigues pero no te siguen de vuelta

## Requisitos

1. Tener una cuenta de desarrollador en Twitter y obtener las claves de API.
2. Python 3.12 o superior instalado en tu sistema.
3. Instalar las dependencias necesarias con `pip install -r requirements.txt`.

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/twitter-basic-stats.git
   cd twitter-basic-stats
   ```
2. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configurar las credenciales de la API de Twitter:
   - Crear un archivo `.env` en la carpeta principal del proyecto.
   - Agregar las siguientes variables:
     ```ini
     API_KEY=tu_api_key
     API_SECRET=tu_api_secret
     ACCESS_TOKEN=tu_access_token
     ACCESS_SECRET=tu_access_secret
     ```

## Uso

Ejecuta el bot con el siguiente comando:

```bash
python main.py
```

El bot realizará las siguientes acciones:

1. Autenticarse en Twitter.
2. Obtener las estadísticas básicas de la cuenta.
3. Identificar usuarios que sigues pero que no te siguen de vuelta.
4. Guardar los resultados en archivos JSON (`twitter_stats.json` y `non_followers.json`).
5. Mostrar los resultados en la consola.

## Archivos generados

- `twitter_stats.json`: Contiene información básica de la cuenta.
- `non_followers.json`: Lista de usuarios que no te siguen de vuelta.

## Posibles errores y soluciones

### 401 Unauthorized: Could not authenticate you

- Verifica que las credenciales en `.env` sean correctas.
- Asegúrate de que tu aplicación de Twitter tenga permisos para leer la información de tu cuenta.
- Si sigues teniendo problemas, regenera las claves de acceso en el portal de desarrolladores de Twitter.

### Otros errores

Si encuentras errores adicionales, revisa la salida de la consola y asegúrate de que la API de Twitter esté funcionando correctamente.

![imagen](https://github.com/user-attachments/assets/8bd15b53-cd21-44f6-b138-1dbef231a704)

