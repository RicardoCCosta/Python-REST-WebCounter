
from flask import Flask, render_template


app = Flask(__name__)

# Contador inicial
counter = 0
@app.route('/')
def index():
    global counter
    counter += 1
    return render_template('index.html', counter=counter)

if __name__ == '__main__':
    app.run(debug=True)