from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db=SQLAlchemy(app)

class Asset(db.Model):  #sets the class so we can refer to things as class.thingy
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    genre = db.Column(db.String (150),nullable=False)
    desc = db.Column(db.String (1000), nullable=False)
    stock = db.Column(db.Integer, nullable = False)
    market = db.Column(db.String (100), nullable=True)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return '<Asset %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        asset_title = request.form['title']
        asset_genre = request.form['genre']
        asset_desc = request.form['desc']
        asset_stock = request.form['stock']
        marketing_allowed=request.form['market']

        new_item= Asset(title=asset_title,genre=asset_genre,desc=asset_desc,stock=asset_stock, market=marketing_allowed)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue with adding the item'
    else:
        asset = Asset.query.all()
        return render_template('index.html',asset=asset)

@app.route('/view')
def viewing():
    asset = Asset.query.all()
    return render_template('view.html',asset=asset)


if __name__=="__main__":
    app.run(debug=True)