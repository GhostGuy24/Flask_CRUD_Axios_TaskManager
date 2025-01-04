from flask import Flask , render_template, request, redirect, url_for
import datetime


app= Flask(__name__)
tasks = [
    {
        "id": 1,
        "name": "Complete Flask Project",
        "description": "Finalize the CRUD functionality and integrate Axios for API requests.",
        "deadline": "2025-01-2",
        "completed": False
    },
    {
        "id": 2,
        "name": "Create",
        "description": "use Create functionality",
        "deadline": "2025-01-3",
        "completed": False
    },
    {
        "id": 3,
        "name": "Add",
        "description": "use Add functionality",
        "deadline": "2025-01-4",
        "completed": False
    },
    {
        "id": 4,
        "name": "Delete",
        "description": "use Delete functionality",
        "deadline": "2025-01-5",
        "completed": False
    },
    {
        "id": 5,
        "name": "Update",
        "description": "use Update functionality",
        "deadline": "2025-01-6",
        "completed": False
    },
    {
        "id": 6,
        "name": "Mark as complete",
        "description": "change task status using a button",
        "deadline": "2025-01-7",
        "completed": False
    }
]

# R - read completed
@app.route("/")
def home():
    return render_template("index.html",tasks=tasks)

# C - create  completed
@app.route("/add", methods=['GET' , 'POST'])
def add_task():
    if request.method == 'GET':
        return render_template("add.html")
    else: #POST
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        deadline = data.get('deadline')
        tasks.append({"id": len(tasks) +1, "name": name, "description":description, "deadline":deadline,"completed": False })
        return render_template("index.html", tasks=tasks)

            
# D - delete  completed
@app.route("/del/<id>", methods=['GET' , 'DELETE'])
def del_task(id=0):
    task_to_delete = next((task for task in tasks if task['id'] == int(id)),None)
    if task_to_delete: tasks.remove(task_to_delete)
    return render_template('index.html', tasks=tasks) 

# U - update(also mark as completed)  completed
@app.route("/upd/<int:id>", methods=['GET', 'PUT'])
def edit_task(id=0):
    task_to_update = next((task for task in tasks if task["id"] == id), None)

    if request.method == "PUT":
        data = request.get_json()  
        name = data.get("name")
        description = data.get("description")
        deadline = data.get("deadline")
        completed = data.get("completed") 


        task_to_update['name'] = name
        task_to_update['description'] = description
        task_to_update['deadline'] = deadline
        task_to_update['completed'] = completed

    return render_template("edit.html", task=task_to_update)















