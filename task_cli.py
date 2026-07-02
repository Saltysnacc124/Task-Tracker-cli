import sys
import json
import os
from datetime import datetime

def save_tasks(task_list):
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)

def add_task(task_list, description):
    if len(task_list)==0:
        task_id=1
    else:
        task_id= task_list[-1]["id"] + 1
    current_time=datetime.now().isoformat()
    new_task={
        "id":task_id,
        "description":description,
        "status":"todo",
        "createdAt":current_time,
        "updatedAt":current_time

    }   
    task_list.append(new_task)   
    save_tasks(task_list)
    print(f"Task added successfully (ID:{task_id})")

def update_task(task_list, task_id, new_description):
     found=False

     for task in task_list:
          if task["id"]==task_id:
               task["description"]= new_description
               task["updatedAt"]=datetime.now().isoformat()
               found=True
               break
     if not found:
          print("Task not found")
          return
     save_tasks(task_list)
     print("Task updated successfully.")                 

def delete_task(task_list, task_id):
     found=False
     for task in task_list:
          if task["id"]==task_id:
              
              task_list.remove(task)
              found=True
              break
     if not found:
          print("Task not found")
          return
     save_tasks(task_list)
     print("Task deleted successfully")   

def mark_task(task_list, task_id, status):
         found= False
         for task in task_list:
              if task["id"]==task_id:
                   task["status"]=status
                   task["updatedAt"]= datetime.now().isoformat()
                   found=True
                   break
         if not found:
              print("Task not found.")
              return
         
         save_tasks(task_list)
         print(f"Task marked as {status}.")

     
     
def list_tasks(task_list, status=None):

    if len(task_list) == 0:
        print("No tasks found.")
        return

    for task in task_list:
        if status is not None and task["status"] != status:
             continue
               
        print("-" * 40)
        print(f"ID          : {task['id']}")
        print(f"Description : {task['description']}")
        print(f"Status      : {task['status']}")
        print(f"Created At  : {task['createdAt']}")
        print(f"Updated At  : {task['updatedAt']}")
        
    print("-" * 40)          

def load_tasks():

    if not os.path.exists("tasks.json"):
        with open("tasks.json","w") as file:
            json.dump([], file)

    with open("tasks.json","r") as file:
        return json.load(file)

task_list = load_tasks()

if len(sys.argv)<2:
    print("Please provide a command.")
    sys.exit()
command=sys.argv[1]

#Add
if command=="add":
    if len(sys.argv)<3:
        print("Please provide a task description.")
        sys.exit()
    description=sys.argv[2]
    add_task(task_list, description)

elif command=="list":
     if len(sys.argv)==3:
          status= sys.argv[2]
          list_tasks(task_list, status)

     else:
          list_tasks(task_list)     
          
    

elif command=="update":
     if len(sys.argv)<4:
          print("Usage: update <id> <description>")
          sys.exit()

     try:
        task_id = int(sys.argv[2])
     except ValueError:
         print("Task ID must be a number.")
         sys.exit()
     new_description=sys.argv[3]

     update_task(task_list, task_id, new_description)  

elif command=="delete":
     if len(sys.argv)<3:
          print("Usage: delete <id>")
          sys.exit()

     task_id = int(sys.argv[2])
     delete_task(task_list, task_id)   

elif command=="mark-done":
       if len(sys.argv)<3: 
            print("Usage: mark-done <id>")
            sys.exit()
       task_id=int(sys.argv[2])
       mark_task(task_list, task_id, "done")

elif command== "mark-in-progress":
         if len(sys.argv)<3:
              print("Usage: mark-in-progress <id>")
              sys.exit()
         task_id= int(sys.argv[2])
         
         mark_task(task_list, task_id, "in-progress")

else:
     print("Unknown command.")

        
            

              


