from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route("/hello/<nome>")
def hello(nome=""):
    return "<h1>Hello {}</h1>".format(nome)

@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID= -1):
    if postID >= 0:
        return "blogs infos {}".format(postID)
    else:
        return "Blogs todo"

if __name__ == '__main__':
    app.run(debug=True)

