from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Contador inicial
counter = 0


@app.route('/', methods=['GET', 'POST'])
def index():
    global counter
    counter += 1
    result = None

    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2

    return render_template('index.html', counter=counter, result=result)


if __name__ == '__main__':
    app.run(debug=True)
