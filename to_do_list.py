to_do_list=[]

def do_action(action):
    if(action=='add'):
        task=input("Enter Your task name: ")
        to_do_list.append(task)
        print("task added")
    elif(action=='delete'):
        if not to_do_list:
            print("There is no task")
        else:
            task_name=input("Enter task name: ")
            if task_name in to_do_list:
                to_do_list.remove(task_name)
                print("task removed")
            else:
                print(f"This task named {task_name} not in the list")
    elif(action=='view'):
        if not to_do_list:
            print("There is no task")
        else:
            for task in to_do_list:
                print(task)
    else:
        print("Invalid action!")

while True:
    action_val=input("Enter Your command add,delete,view or exit ")
    if action_val =='exit':
        break
    else:
        do_action(action_val)