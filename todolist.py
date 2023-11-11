todos=[]

def removeTask(num):
    todos.pop(num)

def updateTask(num):
    print('Current task:',todos[num])
    newTask = input('Enter a task to be replace : ')
    todos[num] = newTask
    print("Replaced Sucessfully ! ")

def listTasks():
    for i in range(len(todos)):
        print (f'|   {i+1}. {todos[i]}   |')

while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. List the task")
    print("5. Exit")
    print("-"*30)
    option = int(input("Enter a option from above : "))
    if(option == 1):
        print("type 'END' to stop")
        while True:
            task = input("Enter your task :  ")
            if task == 'END':
                break
            todos.append(task)

    if(option == 2):
        listTasks()
        n = int(input("Enter a number to remove : "))
        removeTask(n-1)

    if(option == 3):
        listTasks()
        n = int(input("Enter a num to update : "))
        updateTask(n-1)

    if(option == 4):
        print("-"*30)
        print(" These are pending Tasks to do ! ")
        print("    ")
        listTasks()
        print("-"*30)
    
    if(option == 5):
        break
