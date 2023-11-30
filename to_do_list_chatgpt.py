# Initialize an empty to-do list
to_do_list = []

def perform_action(action):
    """
    Perform the specified action on the to-do list.

    Parameters:
        action (str): The action to be performed ('add', 'delete', 'view', or 'exit').

    Returns:
        None
    """
    if action == 'add':
        # Add a new task to the to-do list
        task = input("Enter your task name: ")
        to_do_list.append(task)
        print("Task added")
    elif action == 'delete':
        # Delete a task from the to-do list
        if not to_do_list:
            print("There is no task")
        else:
            task_name = input("Enter task name: ")
            if task_name in to_do_list:
                to_do_list.remove(task_name)
                print("Task removed")
            else:
                print(f"This task named {task_name} is not in the list")
    elif action == 'view':
        # View all tasks in the to-do list
        if not to_do_list:
            print("There is no task")
        else:
            for task in to_do_list:
                print(task)
    elif action == 'exit':
        # Exit the program
        print("Exiting the to-do list application.")
    else:
        # Handle invalid actions
        print("Invalid action!")

# Main loop for user interaction
while True:
    action_val = input("Enter your command (add, delete, view, or exit): ")
    if action_val == 'exit':
        break
    else:
        perform_action(action_val)
