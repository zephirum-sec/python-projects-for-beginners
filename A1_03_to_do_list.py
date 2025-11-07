
print('''
  __                 .___         .__  .__          __   
_/  |_  ____       __| _/____     |  | |__| _______/  |_ 
\   __\/  _ \     / __ |/  _ \    |  | |  |/  ___/\   __\\
 |  | (  <_> )   / /_/ (  <_> )   |  |_|  |\___ \  |  |  
 |__|  \____/____\____ |\____/____|____/__/____  > |__|  
           /_____/    \/    /_____/            \/        
''')

tasks = []

while True:
    print('''Welcome to your To-Do List!
    1. Add Task
    2. Delete Task
    3. Edit Task 
    4. View Tasks
    5. Exit
    ''')

    options = input("Choose an option: ")
   
    if options == '1':
        add = input('Add Task: ')
        tasks.append(add)
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    elif options == '2':
        if not tasks:
            print("No tasks to delete!")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_num = int(input('Enter the number of the task you want to delete: '))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num - 1)
                print(f'Task "{deleted_task}" has been deleted.')
            else:
                print("Invalid task number!")
    
    elif options == '3':
        if not tasks:
            print("No tasks to edit!")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_num = int(input('Enter the number of the task you want to edit: '))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the new task: ")
                tasks[task_num - 1] = new_task
                print(f'Task #{task_num} has been updated to "{new_task}"')
            else:
                print("Invalid task number!")

    elif options == '4':
        if not tasks:
            print("No tasks yet!")
        else:
            print("Your Current Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif options == '5':
        print("Exiting To-Do List. Goodbye! 👋")
        break

    else:
        print("Invalid option. Please choose 1-5.")
