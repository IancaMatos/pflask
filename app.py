from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sobre') # nova rota para a página sobre
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run(debug=True)
