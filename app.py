from flask import Flask, request, render_template, send_file, abort
import csv
import os
import pandas as pd
import requests

app = Flask(__name__)

# Ruta del archivo CSV donde se guardan los datos
ARCHIVO_DATOS = 'datos.csv'

# Clave para acceder a las rutas protegidas
CLAVE_SEGURA = "icaito_54321"  # cámbiala por seguridad

# Token y chat_id de Telegram (tus datos)
TOKEN_TELEGRAM = '7722250896:AAEf90ynAy-eCVaberP50cDLvQ4qhNHi1DQ'
CHAT_ID_TELEGRAM = '1528882748'

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form.get('telefono', '')
    asunto = request.form.get('asunto', '')
    preferencia = request.form.get('preferencia', '')
    novedades = 'Sí' if request.form.get('novedades') else 'No'
    mensaje = request.form['mensaje']

    guardar_datos_csv(nombre, correo, telefono, asunto, preferencia, novedades, mensaje)
    enviar_telegram(nombre, correo, telefono, asunto, preferencia, novedades, mensaje)

    return f"""
    <h2>Datos Recibidos</h2>
    <p><strong>Nombre:</strong> {nombre}</p>
    <p><strong>Correo:</strong> {correo}</p>
    <p><strong>Teléfono:</strong> {telefono}</p>
    <p><strong>Asunto:</strong> {asunto}</p>
    <p><strong>Preferencia:</strong> {preferencia}</p>
    <p><strong>Recibe novedades:</strong> {novedades}</p>
    <p><strong>Mensaje:</strong> {mensaje}</p>
    <a href="/">Volver al formulario</a>
    """

def guardar_datos_csv(nombre, correo, telefono, asunto, preferencia, novedades, mensaje):
    nuevo_archivo = not os.path.exists(ARCHIVO_DATOS)
    with open(ARCHIVO_DATOS, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        if nuevo_archivo:
            escritor.writerow(['Nombre', 'Correo', 'Teléfono', 'Asunto', 'Preferencia', 'Novedades', 'Mensaje'])
        escritor.writerow([nombre, correo, telefono, asunto, preferencia, novedades, mensaje])

def enviar_telegram(nombre, correo, telefono, asunto, preferencia, novedades, mensaje):
    texto = f"""
📩 Nuevo formulario recibido:

👤 Nombre: {nombre}
📧 Correo: {correo}
📞 Teléfono: {telefono}
📝 Asunto: {asunto}
📋 Preferencia: {preferencia}
🔔 Novedades: {novedades}
💬 Mensaje: {mensaje}
"""
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    payload = {
        'chat_id': CHAT_ID_TELEGRAM,
        'text': texto
    }
    requests.post(url, data=payload)

@app.route('/ver-datos')
def ver_datos():
    clave = request.args.get("clave")
    if clave != CLAVE_SEGURA:
        return abort(403)

    if not os.path.exists(ARCHIVO_DATOS):
        return "<p>No hay datos aún.</p>"

    df = pd.read_csv(ARCHIVO_DATOS)
    tabla_html = df.to_html(index=False)
    return f"""
    <h2>Datos Recibidos</h2>
    {tabla_html}
    <a href="/descargar-datos?clave={CLAVE_SEGURA}">Descargar CSV</a><br>
    <a href="/">Volver al formulario</a>
    """

@app.route('/descargar-datos')
def descargar_datos():
    clave = request.args.get("clave")
    if clave != CLAVE_SEGURA:
        return abort(403)

    if not os.path.exists(ARCHIVO_DATOS):
        return "<p>No hay datos para descargar.</p>"

    return send_file(ARCHIVO_DATOS, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

