from config.bd import db, ma, app

class Articulos (db.Model):
    __tablename__ = "Articulo"

    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(70), unique=True)
    Precio = db.Column(db.Float())

    def __init__(self, Nombre, Precio):
        self.Nombre = Nombre
        self.Precio = Precio
with app.app_context():
    db.create_all()

class ArticuloSchema (ma.Schema):
    class Meta:
        fields = ('id','Nombre','Precio')