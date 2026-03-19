import pytest
from app import app, db
from flask_sqlalchemy import SQLAlchemy

@pytest.fixture
def app_context():
    with app.test_request_context():
        yield app

@pytest.fixture
def db():
    db.init_app(app)
    with app.test_request_context():
        db.drop_all()
        db.create_all()
        return db

def test_get_tasks():
    with app_context():
        Task.query.delete()
        task1 = Task(title='Task 1', description='Description 1')
        task2 = Task(title='Task 2', description='Description 2')
        db.session.add(task1)
        db.session.add(task2)
        db.session.commit()
        tasks = app.get_route('/tasks').run_test()
        assert isinstance(tasks, list)
        assert len(tasks) == 2
        assert tasks[0]['title'] == 'Task 1'
        assert tasks[1]['title'] == 'Task 2'

def test_get_task():
    with app_context():
        Task.query.delete()
        task1 = Task(title='Task 1', description='Description 1')
        db.session.add(task1)
        db.session.commit()
        task = app.get_route('/tasks/1').run_test()
        assert isinstance(task, dict)
        assert task['id'] == 1
        assert task['title'] == 'Task 1'
        assert task['description'] == 'Description 1'

def test_create_task():
    with app_context():
        task = app.post_route('/tasks').run_test()
        assert isinstance(task, dict)
        db.session.commit()
        assert task['title'] == 'Grocery Shopping'
        assert task['description'] == 'Buy milk, eggs, and bread'

def test_update_task():
    with app_context():
        Task.query.delete()
        task1 = Task(title='Task 1', description='Description 1')
        db.session.add(task1)
        db.session.commit()
        updated_task = app.put_route('/tasks/1').run_test()
        assert isinstance(updated_task, dict)
        assert updated_task['title'] == 'Updated Task'
        assert updated_task['description'] == 'Updated Description'

def test_delete_task():
    with app_context():
        Task.query.delete()
        task1 = Task(title='Task 1', description='Description 1')
        db.session.add(task1)
        db.session.commit()
        app.delete_route('/tasks/1').run_test()
        db.session.commit()
        tasks = Task.query.all()
        assert len(tasks) == 0