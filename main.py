from flask import Flask, render_template
app = Flask(__name__,
            static_url_path='')
@app.route("/")
def index():
    return render_template("index.html")
app.run()













"""
# проста вигрузка сайту із папки templates без стилів

from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
app.run()
"""


"""
# вигрузка сайту із папки template з стилями
# index знаходиться в templates
# папки і файли до основного index вантажимо до папки static
# прописуємо, де знаходяться статичні адреси (static_url_path='')

from flask import Flask, render_template
app = Flask(__name__,
            static_url_path='')
@app.route("/")
def index():
    return render_template("index.html")
app.run()
"""








"""

app = Flask(__name__,
            static_url_path='')

@app.route("/")

def index():
    return render_template("index.html")


@app.route("/blog")

def blog():



    
    return render_template("site.html")


app.run()
"""
"""
@app.route("/")
def index():
    return "Вітаємо у Вашому сайті"

@app.route("/123")
def index2():
    return "123"
"""
