from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

def teste():
    return "<p>Teste 1</p>"
app.add_url_rule("/teste", "teste",teste)

def teste2():
    return "<h1>Teste 2</h1>"
app.add_url_rule("/teste2","teste2", teste2)

if __name__ == '__main__':
    app.run(debug=True, port="3000")