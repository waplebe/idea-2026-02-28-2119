from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///tasks.db')
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Task {self.title}>'

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = []
    for task in tasks:
        task_list.append({'id': task.id, 'title': task.title, 'description': task.description})
    return jsonify(task_list)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify({'id': task.id, 'title': task.title, 'description': task.description})

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title:
        abort(400, description="Title is required")

    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'id': new_task.id, 'title': new_task.title, 'description': new_task.description}), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)

    db.session.commit()

    return jsonify({'id': task.id, 'title': task.title, 'description': task.description})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task deleted'})

@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({'message': str(e)}), e.code

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)