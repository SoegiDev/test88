from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/test")
def hello_tst():
    return "<h1 style='color:red'>Tes Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')