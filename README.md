# 📝 Formulario Web con Flask + CSV + Render

Enlace: https://form-icaito.onrender.com

Este proyecto es una aplicación web simple construida con **Flask** que permite a los usuarios enviar un formulario. Los datos enviados se guardan automáticamente en un archivo **CSV** y pueden ser visualizados o descargados desde rutas protegidas.

---

## 🚀 Funcionalidades

- Formulario web de contacto
- Almacenamiento automático en `datos.csv`
- Visualización de los datos en tabla (HTML)
- Descarga del archivo CSV
- Acceso protegido mediante una clave

---

## 📂 Estructura del proyecto

```
formulario_app/
├── app.py
├── requirements.txt
├── templates/
│   └── formulario.html
└── README.md
```

---

## ▶️ Cómo ejecutar localmente

1. Clona el repositorio:

   ```bash
   git clone https://github.com/TU_USUARIO/formulario-app.git
   cd formulario-app
   ```

2. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la app:

   ```bash
   python app.py
   ```

4. Abre en tu navegador:

   ```
   http://127.0.0.1:5000/
   ```

---

## 🌐 Despliegue en Render

1. Crea una cuenta gratuita en [https://render.com](https://render.com)
2. Sube este repositorio a GitHub
3. En Render:
   - Crea un nuevo **Web Service**
   - Conecta tu GitHub
   - Elige este repositorio
   - Configura:
     - Runtime: Python
     - Build command: `pip install -r requirements.txt`
     - Start command: `gunicorn app:app`
   - Selecciona el plan gratuito y despliega

Render generará una URL pública como:

```
https://formulario-app.onrender.com
```

---

## 🔐 Rutas protegidas

Para ver o descargar los datos se requiere una clave de acceso (definida en `app.py`):

- Ver tabla:
  ```
  /ver-datos?clave=TU_CLAVE
  ```

- Descargar CSV:
  ```
  /descargar-datos?clave=TU_CLAVE
  ```

Cambia la clave en el archivo `app.py`:
```python
CLAVE_SEGURA = "12345"  # cámbiala por seguridad
```

---

## 📦 Requisitos

- Python 3.8+
- Flask
- Pandas

---

## ⏰ Mantener el sitio activo con UptimeRobot (opcional)

Render en el plan gratuito puede "dormir" tu sitio si no recibe visitas por un tiempo. Para evitarlo, puedes usar [UptimeRobot](https://uptimerobot.com):

1. Crea una cuenta gratuita en https://uptimerobot.com
2. Añade un nuevo monitor:
   - Tipo: `HTTP(s)`
   - Nombre: el que prefieras (por ejemplo, "Mi formulario")
   - URL: la URL de tu sitio en Render (por ejemplo `https://formulario-app.onrender.com`)
   - Intervalo: cada 5 minutos
3. Guarda y ¡listo!

Esto mantendrá tu sitio activo automáticamente.

---

## 📃 Licencia

Este proyecto es de uso libre para fines educativos y personales.

---

## ✍️ Autor

Desarrollado por [Ricardo Diosdado icaito-ricodi]
Canal youtube[https://www.youtube.com/@icaito-ricodi-resica]

