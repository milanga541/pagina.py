from flask import Flask
import random

app = Flask(__name__)
facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
            "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
            "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna."]

@app.route("/")
def index():
    return f'<h1>Hola, en esta página puedes aprender un par de cosas interesantes sobre las dependencias tecnológicas.</h1> <a href="/random_fact">Haz click aquí para ver un hecho aleatorio. esto te llevara a una pagina que te dara un dato diferente cada vez que la recargues(hay 4 datos diferentes)</a>'
    return f'<h1>Hola, en esta página puedes aprender un par de cosas interesantes sobre las dependencias tecnológicas.</h1> <a href="/2">tira una moneda al aire y caera cara o cruz de forma aleatoria </a>'
@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/2")
def moneda():
    return f"<p>{random.choice("cara", "cruz")}</p>"
app.run(debug=True)
