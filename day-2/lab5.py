import mysql.connector
#1
class Employee:
    employees = []
    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.employees.append(self)
        self.insert_into_db()
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="mydatabase"
        )

    def insert_into_db(self):
        conn = self.get_connection()
        cur = conn.cursor()
        query = """
        INSERT INTO employee (first_name, last_name, age, department, salary)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            self.first_name,
            self.last_name,
            self.age,
            self.department,
            self.salary
        )
        cur.execute(query, values)
        conn.commit()
        conn.close()

    def transfer(self, new_department):
        self.department = new_department
        conn = self.get_connection()
        cur = conn.cursor()
        query = """
        UPDATE employee
        SET department = %s
        WHERE first_name = %s AND last_name = %s
        """
        cur.execute(query, (new_department, self.first_name, self.last_name))
        conn.commit()
        conn.close()
    def fire(self):
        if self in Employee.employees:
            Employee.employees.remove(self)
        conn = self.get_connection()
        cur = conn.cursor()
        query = """
        DELETE FROM employee
        WHERE first_name = %s AND last_name = %s
        """
        cur.execute(query, (self.first_name, self.last_name))
        conn.commit()
        conn.close()
    def show(self):
        print(f"{self.first_name} {self.last_name} | "
              f"{self.age} | {self.department} | {self.salary}")
    @classmethod
    def list_employees(cls):
        conn = cls.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employee")
        rows = cur.fetchall()
        conn.close()
        return rows

        



#2
class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        print(
            f"{self.first_name} {self.last_name} | "
            f"{self.age} | {self.department} | "
            f"Salary: Confidential | "
            f"Manages: {self.managed_department}"
        )




while True:
    print("\n===== MENU =====")
    print("add -> Add Employee")
    print("m   -> Add Manager")
    print("t   -> Transfer Employee")
    print("f   -> Fire Employee")
    print("l   -> List from DB")
    print("q   -> Quit")

    choice = input("Enter choice: ").lower()

    if choice == "add":
        print("\nEmployee Data:")

        fn = input("First name: ")
        ln = input("Last name: ")
        age = int(input("Age: "))
        dep = input("Department: ")
        sal = float(input("Salary: "))

        e = Employee(fn, ln, age, dep, sal)
        print("Employee added!")

    elif choice == "m":
        print("\nManager Data:")

        fn = input("First name: ")
        ln = input("Last name: ")
        age = int(input("Age: "))
        dep = input("Department: ")
        sal = float(input("Salary: "))
        mdep = input("Managed department: ")

        m = Manager(fn, ln, age, dep, sal, mdep)

        print("Manager added!")

    elif choice == "t":
        fn = input("First name: ")
        ln = input("Last name: ")
        new_dep = input("New department: ")

        for e in Employee.employees:
            if e.first_name == fn and e.last_name== ln:
                e.transfer(new_dep)
                print("Transferred!")


    elif choice == "f":
        fn = input("First name: ")
        ln = input("Last name: ")

        for e in Employee.employees:
             if e.first_name == fn and e.last_name == ln:
                e.fire()
                print("Fired!")

    elif choice == "l":
        employees =Employee.list_employees()
        for e in employees:
            print(e)

    elif choice == "q":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

    


        