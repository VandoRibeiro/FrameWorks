from flask import Flask, render_template # type: ignore

app = Flask(__name__)

teste = [ 
    {
        "Nome": "ABC",
        "Imagem": "https://w0.peakpx.com/wallpaper/659/699/HD-wallpaper-python-amoled-coding-coding-dark-dark-programming-python-sky-universe.jpg"
    },
    {
        "Nome": "ABC",
        "Imagem": "URL"
    },
    {
        "Nome": "ABC",
        "Imagem": "URL"
    }

]
@app.route('/')
def index():
    return render_template('index.html', a=teste)

app.run()