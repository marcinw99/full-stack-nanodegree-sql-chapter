import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

  def __repr__(self):
      return f'<User {self.id}, {self.name}>'


db.create_all()


@app.route('/')
def index():
    q1 = User.query.filter_by(name='Amy').all()
    q2 = User.query.filter(User.name.like('%b%')).all()
    q3 = User.query.filter(User.name.like('%b%')).limit(5).all()
    q4 = User.query.filter(User.name.ilike('%b%')).all()
    q5 = User.query.filter(User.name=='Bob').count()
    return str(q5)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')