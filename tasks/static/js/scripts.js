function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}

function drop(event) {
    event.preventDefault();
    var task_id = event.dataTransfer.getData("text");
    var task_element = document.getElementById(task_id);

    // Determine the new status based on the column where the task is dropped
    var newStatus;
    if (event.target.id === 'not-started' || event.target.closest('#not-started')) {
        newStatus = 'not_started';
    } else if (event.target.id === 'in-progress' || event.target.closest('#in-progress')) {
        newStatus = 'in_progress';
    } else if (event.target.id === 'completed' || event.target.closest('#completed')) {
        newStatus = 'completed';
    } else {
        return; // Exit if not dropping into a valid column
    }

    // Move the task element to the new column
    if (event.target.classList.contains('list-group')) {
        event.target.appendChild(task_element);
    } else if (event.target.closest('.list-group')) {
        event.target.closest('.list-group').appendChild(task_element);
    }

    // Send an AJAX request to update the task's status on the server
    fetch(`/update_task_status/${task_id.split('-')[1]}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'status': newStatus }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Problem with updating task status');
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message);
        task_element.classList.remove('list-group-item');
        task_element.classList.add('updated');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
