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
