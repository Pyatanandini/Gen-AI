#1. Contact List: Create a dictionary to store contacts. Each key should be a name, and the value should be another dictionary with phone' and 'email'. Write code to add a new contact and retrieve an existing one.
contacts={'nandini':{'email':'nandini11@gmail.com','phone' : 7534559384}}
contacts['teena']={'email':'teena44@gmail.com','phone': 643198279}
contacts['riya']={'email':'riya77@gmail.com','phone': 875684559}
contacts['chari']={'phone': 65486879, 'email': 'technology.com'}
contacts['pranay']={'phone': 86765664987, 'email': "technology3.com"}
contacts['aryan']={'phone': 97642456787, 'email': "technology5.com"}
print(contacts)
name = input()
print(name)
if name in contacts:
    print('email:',contacts[name]['email'])
    print('phone:',contacts[name]['phone'])
else:
    print('record not found')






#2. Data Deduplication: Given a list of emails with duplicates, use a set to create a list containing only unique emails. 
l = ["nandini11@gmail.com", "teena44@gmail.com", "riya88@gmail.com", "nandini11@gmail.com", "pranay33@gmail.com"]
l = set(l)
l = list(l)
print(l)


#3. List Manipulation: Create a to-do list. Write functions to add a task, remove a task by index, and print all tasks todo list

task =[]
def addTask(task_):
    task.append(task_)

def removeTask(ind):
    task_poped = task.pop(ind)
    return task_poped

addTask({"time":12, "work": "login"})
addTask({"time":13, "work": "start working"})
addTask({"time":14, "work": "Take a break"})
print(task)
print(f"removed task {removeTask(1)}")
print(task)