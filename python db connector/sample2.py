import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="niranj003",  
    database="Emp_management"  
)

mycr = mydb.cursor()


def listing():
    a = int(input("Enter the ID of the employee: "))
    mycr.execute("SELECT * FROM Emp_management WHERE id = %s", (a,))
    result = mycr.fetchall()
    for i in result:
        print(i)


def add():
    id = int(input("Enter the ID of the employee: "))
    name = input("Enter the name of the employee: ")
    age = int(input("Enter the age of the employee: "))
    salary = int(input("Enter the salary of the employee: "))
    val = "INSERT INTO Emp_management (id, name, age, salary) VALUES (%s, %s, %s, %s)"
    fields = (id, name, age, salary)
    mycr.execute(val, fields)
    mydb.commit()
    print("Added Successfully")

def delete():
    id = int(input("Enter the ID of the employee: "))
    mycr.execute("DELETE FROM Emp_management WHERE id = %s", (id,))
    mydb.commit()
    print("Deleted Successfully")


def edit():
    id = int(input("Enter the ID of the employee: "))
    newname = input("Enter the new name: ")
    newage = int(input("Enter the new age: "))
    newsal = int(input("Enter the new salary: "))
    mycr.execute("UPDATE Emp_management SET name = %s, age = %s, salary = %s WHERE id = %s", (newname, newage, newsal, id))
    mydb.commit()
    print("Updated Successfully")

while True:
    print("\n1. List")
    print("2. Add")
    print("3. Edit")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
        
    if choice == 1:
        listing()
    elif choice == 2:
        add()
    elif choice == 3:
        edit()
    elif choice == 4:
        delete()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("invalid")