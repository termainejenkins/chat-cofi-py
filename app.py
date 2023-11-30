from flask import Flask, render_template
from flask_vue import Vue

app = Flask(__name__)
Vue(app)

@app.route('/')
def index():
    return render_template('index_vue.html')

if __name__ == '__main__':
    app.run(debug=True)
