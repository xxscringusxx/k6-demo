from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def home():
    listRandomNumbers= [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    return render_template('home.html', random_num=listRandomNumbers)

if __name__ == '__main__':
    app.run(debug=True)