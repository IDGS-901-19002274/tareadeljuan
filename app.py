from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", page_name = "Inicio")

@app.route('/comprar', methods=['GET'])
def comprar():
    return render_template("comprar.html", page_name = "Comprar")

@app.route('/nosotros', methods=['GET'])
def nosotros():
    return render_template("nosotros.html", page_name = "Nosotros")

@app.route('/contacto', methods=['GET'])
def contacto():
    return render_template("contacto.html", page_name = "Contacto")

@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html", page_name = "Login")

@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html", page_name = "Register")

if __name__ == "__main__":
    app.run(debug = True, port=3000)