from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('icaito.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    mensaje = request.form['mensaje']

    return f"""
    <h2>Datos Recibidos</h2>
    <p><strong>Nombre:</strong> {nombre}</p>
    <p><strong>Correo:</strong> {correo}</p>
    <p><strong>Mensaje:</strong> {mensaje}</p>
    <a href="/">Volver al formulario</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
