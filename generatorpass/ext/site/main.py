from flask import request, render_template
from flask import Blueprint

bp = Blueprint("site", __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    info = None
    if request.method == 'POST':
        conta = request.form['conta']
        user = request.form['user']
        length = int(request.form['num_caracteres'])
        info = "Dados enviados com sucesso!"
        print(f"{conta}-{user}={length}")
    return render_template("index.html", var=info)

@bp.route('/senhas')
def senhas():
    return render_template("senhas.html")

@bp.route('/about')
def about():
    return render_template("about.html")
