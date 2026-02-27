'''
Make a to-do list that saves to a file and allow
users to Add, View and remove tasks depending on what they want. 

'''
def writing_tasks():
    tasks = open("to_do_list.txt","w")
    for i in range(no_of_tasks):
        task = input("Enter what task you must do: ")
        tasks.write("\n")
        tasks.write("-"+ task + "\n")
    tasks.close()

def reading_tasks():
    tasks = open("to_do_list.txt","r")
    print(tasks.read())
    tasks.close()

def changing_tasks():
    tasks = open("to_do_list.txt","r")
    task = tasks.readlines()
    change_task = input("Write changed task:  ")
    change_line = int(input("Enter the line you want to change"))
    task[change_line] = f"- {change_task}"
    tasks.close()
    tasks = open("to_do_list.txt","w")
    tasks.writelines(task)
    tasks.close()
    
no_of_tasks = int(input("How many tasks do you want in your to_do_list:")) 

writing_tasks()   
reading_tasks()

task_change = input("Do you want to change a task? Y/N")
if task_change == "Y":
    changing_tasks()
else:
    reading_tasks()
