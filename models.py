from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Website(db.Model):
    __tablename__ = 'websites'
    id_web = db.Column(db.Integer, primary_key=True)
    nama_web = db.Column(db.String(100))
    link_web  = db.Column(db.String(200))
    slug_web  = db.Column(db.String(200))
    pages = db.relationship('Page', backref='website', lazy=True)

class Page(db.Model):
    __tablename__ = 'pages'
    id_page = db.Column(db.Integer, primary_key=True)
    id_web = db.Column(db.Integer, db.ForeignKey('websites.id_web'), nullable=False)
    halaman_web = db.Column(db.String(100))
    
