'''
Exercise#5

The task is to create a "Health Management System." Suppose you are a fitness trainer and nutritionist. 
You have to deal with three clients, i.e., (Harry, Rohan, Hammad).
For each client, you have to design their exercise and diet plan.

Instructions:

    Create a food log file for each client
    Create an exercise log file for each client.
    Ask the user whether they want to log or retrieve client data.
    Write a function that takes the user input of the client's name. 
    After the client's name is entered, it will display a message as "What you want to log- Diet or Exercise".
    Use function

'''

#For daily dates. 
def getdate():
        import datetime
        return datetime.datetime.now()
    
# to write the data in file.
def write_in_file(filename):
    with open(filename, "a") as f:
        #print("what do you want to write here : ")
        data = input("what do you want to write here : ")
        f.write(f"{getdate()} : {data}\n")
        
# to read the data from file.
def read_from_file(filename):
    with open(filename, "r") as f:
        print(f.read())
        
# to log the data in file.
def log_data():
    print("""
    1. Harry,
    2. Rohan,
    3. Hammad
        """)
    client_name = input("Enter the client name : ")
    log_type = input("What do you want to log - Diet or Exercise : ")
    if log_type.lower() == "diet":
        write_in_file(f"{client_name.lower()}_diet.txt")
    elif log_type.lower() == "exercise":
        write_in_file(f"{client_name.lower()}_exercise.txt")
    else:
        print("Invalid Input")

# to retrieve the data from file.
def retrieve_data():
    print("""
    1. Harry,
    2. Rohan,
    3. Hammad
        """)
    client_name = input("Enter the client name : ")
    log_type = input("What do you want to retrieve - Diet or Exercise : ")
    if log_type.lower() == "diet":
        read_from_file(f"{client_name.lower()}_diet.txt")
    elif log_type.lower() == "exercise":
        read_from_file(f"{client_name.lower()}_exercise.txt")
    else:
        print("Invalid Input")
        
# Main function
if __name__ == "__main__":
    print("==============================================================================")
    print("==================== Welcome to Health Management System =====================")
    print("==============================================================================")
    print("")
    
    choice = True
    
    while  choice != 00:
        print("1. Log Data")
        print("2. Retrieve Data")
        print("00. for exit ")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            log_data()
        elif choice == 2:
            retrieve_data()
        elif choice == 00:
            print("Thank you for using Health Management System")
            break
        else:
            print("Invalid Input")