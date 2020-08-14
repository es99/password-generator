from flask import request, render_template
from flask import Blueprint
from generatorpass.ext.gerador import generate
from generatorpass.ext.db.models import Senhas

bp = Blueprint("site", __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    info = None
    if request.method == 'POST':
        conta = request.form['conta']
        user = request.form['user']
        length = int(request.form['num_caracteres'])
        if generate(conta, user, length):
            info = "Dados enviados com sucesso!"
        else:
            info = "Erro ao salvar no banco de dados"

    return render_template("index.html", var=info)

@bp.route('/senhas')
def senhas():
    items = Senhas.query.all()
    return render_template("senhas.html", items=items)

@bp.route('/about')
def about():
    return render_template("about.html")
