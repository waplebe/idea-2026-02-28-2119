document.addEventListener('DOMContentLoaded', function() {
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');

    addTaskBtn.addEventListener('click', function() {
        const title = prompt("Enter task title:");
        const description = prompt("Enter task description:");

        if (title && description) {
            fetch('http://localhost:5000/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title: title, description: description })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Task created:', data);
                const taskItem = document.createElement('div');
                taskItem.textContent = `${data.title} - ${data.description}`;
                taskList.appendChild(taskItem);
            })
            .catch(error => {
                console.error('Error creating task:', error);
            });
        }
    });

    fetch('http://localhost:5000/tasks')
        .then(response => response.json())
        .then(tasks => {
            taskList.innerHTML = '';
            tasks.forEach(task => {
                const taskItem = document.createElement('div');
                taskItem.textContent = `${task.title} - ${task.description}`;
                taskList.appendChild(taskItem);
            });
        })
        .catch(error => {
            console.error('Error fetching tasks:', error);
        });
});