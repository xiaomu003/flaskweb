from flask import Flask, render_template
from login import login


app = Flask(__name__)
app.secret_key = 'any random string'
urls = [login]
for url in urls:
    app.register_blueprint(url)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=2020, host="127.0.0.1", debug=True)
