from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1.html', methods=['GET', 'POST'])
def ejercicio1():

    res = None
    if request.method == 'POST':
        nombre = request.form.get("nombre", "").strip()
        edad = int(request.form.get('edad', 0))
        cantidad = int(request.form.get('cantidad', 0))
        precio_tarro = 9000
        total_s_d = cantidad * precio_tarro
        desc = 0

        if (18 <= edad <= 30):
            desc = 0.15
        elif (edad > 30):
            desc = 0.25

        total = total_s_d * (1 - desc)
        res = f"""Nombre del Cliente: {nombre}
         
             Total sin descuento: ${total_s_d:.2f} 
                  
             El descuento es: ${total_s_d * desc:.2f} 
                  
             El total a pagar es de: ${total:.2f}"""



    return render_template('ejercicio1.html', res=res)

@app.route('/ejercicio2.html', methods=['GET', 'POST'])
def ejercicio2():

    res = None
    if request.method == 'POST':
        nombre = request.form.get("nombre", "").strip()
        contraseña = request.form.get("contraseña","").strip()

        if (nombre == "Juan" and contraseña == "admin"):
            res = f"Bienvenido administrador {nombre}"

        elif (nombre == "Pepe" and contraseña == "user"):
            res = f"Bienvenido usuario {nombre}"

        else:
            res = f"Usuario o Contraseña Incorrectos"

    return render_template('ejercicio2.html', res=res)

if __name__ == '__main__':
    app.run(debug= True)

