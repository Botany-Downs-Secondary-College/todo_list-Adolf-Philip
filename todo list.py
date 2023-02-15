#Functions

#Greets the User
def greeting():
    name = input("What is your name? ")
    print(f"Hello, {name}! \n")

#Asks user to add task 
def add_task(tasks):
    task = input("What task would you like to add? ")
    tasks.append(task)
    print(f"Task '{task}' has been added to your todo list.")

#Shows user current items in todo list
def view_list(tasks):
    if not tasks:
        print(" \nYour todo list is empty.")
    else:
        print(" \nHere is your current todo list:")
        for i in tasks:
            print(" - {} \n".format(i))

#The main program
def main():
    tasks = []
    greeting()
    while True:
        print("Please choose an option:")
        print("1. Add a task")
        print("2. View list")
        print("3. Exit \n")
        choice = input("Enter your choice (1, 2, or 3):")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_list(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

#Initiates Programme
main()
