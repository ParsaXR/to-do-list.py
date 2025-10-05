
def save_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
        print("task added☑️")
       

def load_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("there is no task")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}- {task}")


def add_task():
    while True:
        user_new_task = input("Enter your task (or e for exit): ")
        if user_new_task == "e":
            print(" ")
            break
        else:
            save_task(user_new_task)


def delete_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    for i, task in enumerate(tasks, start=1):
        print(f"{i} - {task}")

    while True:
        user_delete = int(input("which task ? "))

        if 1 <= user_delete <= len(tasks):
            tasks.pop(user_delete - 1)
            print("task deleted")
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            break
        else:
            print("invalid number")


def menu():
    while True:
        print("Menu\n---------------")
        print("     1- view tasks")
        print("     2- Add tasks")
        print("     3- Delete tasks")
        print("     4- Exit")
        try:
            user_choice = int(input("----> "))
        except ValueError:
            print("please enter a number!")
            continue

        if 1 <= user_choice <= 4:
            if user_choice == 1:
                load_task()

            elif user_choice == 2:
                add_task()

            elif user_choice == 3:
                delete_task()

            else:
                break
        else:
            print("invalid number")


menu()
