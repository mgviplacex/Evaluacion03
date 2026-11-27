from flask import Flask, render_template, request
app = Flask(__name__)

# Agregamos la ruta y el menu con 2 botones
@app.route('/')
def index():
    return render_template('index.html')

# Ruta Ejercicio01 para formulario de notas y % asistencia
@app.route('/ejercicio01', methods=['GET', 'POST'])
def ejercicio01():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template(
            'ejercicio01.html', promedio=promedio, estado=estado )

    return render_template('ejercicio01.html')

# Ruta Ejercicio 2 para formulario de nombres
@app.route('/ejercicio02', methods=['GET', 'POST'])
def ejercicio02():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        if len(nombre1) >= len(nombre2) and len(nombre1) >= len(nombre3):
            nombre_mayor = nombre1
            cantidad = len(nombre1)
        elif len(nombre2) >= len(nombre1) and len(nombre2) >= len(nombre3):
            nombre_mayor = nombre2
            cantidad = len(nombre2)
        else:
            nombre_mayor = nombre3
            cantidad = len(nombre3)
        return render_template('ejercicio02.html', nombre_mayor=nombre_mayor, cantidad=cantidad)

    return render_template('ejercicio02.html')

if __name__ == '__main__':
    app.run(debug=True)