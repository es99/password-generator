from generatorpass.ext.db import db


class Senhas(db.Model):
    __tablename__ = "senhas"
    id = db.Column("id", db.Integer, primary_key=True)
    conta_app = db.Column("conta_app", db.String(50), unique=True)
    user_email = db.Column("user_email", db.Unicode)
    passwd = db.Column("passwd", db.Unicode)
    data_raw = db.Column("data_raw", db.DateTime)

    def __repr__(self):
        return "%r. <%r>" % (self.id, self.user_email)
    
class Servidores(db.Model):
    __tablename__ = "servidores"
    id = db.Column("id", db.Integer, primary_key=True)
    servidor = db.Column("server", db.String(50))
    ip = db.Column("ip", db.String(50))
    user = db.Column("user", db.String(50))
    password = db.Column("password", db.Unicode)
    data_raw = db.Column("data_cadastro", db.DateTime)
    
    def __repr__(self):
        return "%r - %r" % (self.ip, self.servidor)
