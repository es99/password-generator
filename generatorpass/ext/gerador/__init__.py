import random
from datetime import datetime
from generatorpass.ext.db import db
from generatorpass.ext.db.models import Senhas


def embaralha(t):
    abc = "abcdefghijklmnopqrstuvwxyz"
    ABC = abc.upper()
    numeros = "1234567890"
    mistura = abc + numeros + ABC
    password = ""
    for i in range(t):
        c = random.choice(mistura)
        password += c

    return password


def generate(conta_app, user_email, tam):
    data_raw = datetime.now()
    passwd = embaralha(tam)
    try:
        entrada = Senhas(
            conta_app=conta_app,
            user_email=user_email,
            passwd=passwd,
            data_raw=data_raw,
        )
        db.session.add(entrada)
        db.session.commit()
        return True
    except:
        return False
