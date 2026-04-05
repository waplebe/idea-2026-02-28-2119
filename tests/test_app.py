import pytest
from app import app, db
from models import Task

@pytest.fixture
def test_db(app):
    db.drop_all()
    db.create_all()
    return db

def test_get_tasks(test_db):
    with app.test_request_context():
        Task.create_many([
            Task(title='Task 1', description='Description 1'),
            Task(title='Task 2', description='Description 2')
        ])
        response = app.get('/tasks')
        assert response.status_code == 200
        tasks = response.get_json()
        assert len(tasks) == 2
        assert tasks[0]['title'] == 'Task 1'
        assert tasks[1]['title'] == 'Task 2'

def test_get_task(test_db):
    with app.test_request_context():
        task = Task.create(title='Test Task', description='Test Description')
        response = app.get(f'/tasks/{task.id}')
        assert response.status_code == 200
        task_data = response.get_json()
        assert task_data['title'] == 'Test Task'
        assert task_data['description'] == 'Test Description'

def test_create_task(test_db):
    with app.test_request_context():
        data = {'title': 'New Task', 'description': 'New Description'}
        response = app.post('/tasks', data=jsonify(data))
        assert response.status_code == 201
        task = Task.query.get(data['title'])
        assert task is not None
        assert task.title == 'New Task'
        assert task.description == 'New Description'

def test_update_task(test_db):
    with app.test_request_context():
        task = Task.create(title='Original Task', description='Original Description')
        data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = app.put(f'/tasks/{task.id}', data=jsonify(data))
        assert response.status_code == 200
        updated_task = Task.query.get(task.title)
        assert updated_task is not None
        assert updated_task.title == 'Updated Task'
        assert updated_task.description == 'Updated Description'

def test_delete_task(test_db):
    with app.test_request_context():
        task = Task.create(title='Delete Task', description='Delete Description')
        response = app.delete(f'/tasks/{task.id}')
        assert response.status_code == 200
        deleted_task = Task.query.get(task.title)
        assert deleted_task is None