from flask import Flask, request, render_template, send_file, abort
import csv
import os
import pandas as pd

app = Flask(__name__)

# Ruta del archivo CSV donde se guardan los datos
ARCHIVO_DATOS = 'datos.csv'

# Clave para acceder a las rutas protegidas
CLAVE_SEGURA = "icaito 54321"  # cámbiala por seguridad

@app.route('/')
def index():
    return render_template('icaito.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    mensaje = request.form['mensaje']

    guardar_datos_csv(nombre, correo, mensaje)

    return f"""
    <h2>Datos Recibidos</h2>
    <p><strong>Nombre:</strong> {nombre}</p>
    <p><strong>Correo:</strong> {correo}</p>
    <p><strong>Mensaje:</strong> {mensaje}</p>
    <a href="/">Volver al formulario</a>
    """

def guardar_datos_csv(nombre, correo, mensaje):
    nuevo_archivo = not os.path.exists(ARCHIVO_DATOS)
    with open(ARCHIVO_DATOS, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        if nuevo_archivo:
            escritor.writerow(['Nombre', 'Correo', 'Mensaje'])
        escritor.writerow([nombre, correo, mensaje])

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


