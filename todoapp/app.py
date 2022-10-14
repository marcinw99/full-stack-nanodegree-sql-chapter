from os import abort
from flask import Flask, jsonify, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@127.0.0.1:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())

@app.route('/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        newTodo = Todo(description=description, completed=False)
        db.session.add(newTodo)
        db.session.commit()
        body['description'] = newTodo.description
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()
        if error:
            abort()
        else:
            return jsonify(body)

@app.route('/toggle-completed', methods=['POST'])
def toggle_todo():
    try:
        id = request.get_json()['id']
        completed = request.get_json()['completed']
        todo = Todo.query.filter_by(id=id).first()
        todo.completed = completed
        db.session.commit()
        return Response(status=201, mimetype='application/json')
    except:
        db.session.rollback()
        return Response(status=400, mimetype='application/json')
    finally:
        db.session.close()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)