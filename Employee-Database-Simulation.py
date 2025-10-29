employee_data = { 
    1 : {
    "name" : "Alice Johnson",
    "age" : 28,
    "department" : "HR",
    "salary ($)" : 55000
        }, 
    
    2 : {
    "name" : "Brian Smith",
    "age" : 35,
    "department" : "IT",
    "salary ($)" : 75000
        },

    3 : {
    "name" : "Catherine Lee",
    "age" : 42,
    "department" : "Finance",
    "salary ($)" : 82000
        }, 
            
    4 : {
    "name" : "David Brown",
    "age" : 30,
    "department" : "IT",
    "salary ($)" : 68000
        }, 

    5 : {
    "name" : "Ella Williams",
    "age" : 26,
    "department" : "Marketing",
    "salary ($)" : 50000
        }, 

    6 : {
    "name" : "Frank Green",
    "age" : 33,
    "department" : "Finance",
    "salary ($)" : 64000
        }, 

    7 : {
    "name" : "Grace Miller",
    "age" : 29,
    "department" : "HR",
    "salary ($)" : 58000
        }, 

    8 : {
    "name" : "Henry Davis",
    "age" : 38,
    "department" : "IT",
    "salary ($)" : 79000
        },

    9 : {
    "name" : "Irene Wilson",
    "age" : 31,
    "department" : "Sales",
    "salary ($)" : 60000
        }, 

    10 : {
    "name" : "Jack Thompson",
    "age" : 45,
    "department" : "Management",
    "salary ($)" : 90000
        }, 
                        
}
print("Welcome to the employee database. ")
print(employee_data)
while True:
    print(
    "What task would you like to perform today? \n" \
    "1. View the database \n"
    "2. Add a new employee record. \n" \
    "3. Update an employee salary. \n" \
    "4. Delete an employee record. \n" \
    "5. Retreive total number of employees. \n" \
    "6. Retrieve highest earner. \n" \
    "7. Obtain average salary. \n" \
    "8. Retrieve all employees of a department. \n" \
    "9. View employee by ID. \n" \
    "10. View emloyees by department. \n" \
    "11. Grant percentage bonuses to employee. \n" \
    "12. Exit the database"
    )
    user_task = int(input(">>>>>>>  "))
    if user_task == 1:
        for x , y in employee_data.items():
            print(f'{y['name']} : {y["department"]}')
    elif user_task == 2:
        updated_id = max(employee_data) + 1 
        updated_name = input("Enter employee name: ")
        updated_age = int(input("Enter employee age: "))
        updated_department = input("Enter employee department: ")
        updated_salary = int(input("Enter employee salary: "))
        employee_data.update({updated_id: {"name": updated_name,
                                           "age" : updated_age,
                                           "department" : updated_department,
                                           "salary ($)" : updated_salary}})
        print("New employee record added successfully.")
        user_request = input("Do you want to veiw updated database? (yes/no)")
        if user_request.lower() == "yes":
            print(employee_data)
            continue
        else:
            continue
    elif user_task == 3:
        update_salary = int(input("Enter employee ID to update salary: "))
        if update_salary in employee_data.keys():
            print(f"Employee ID {update_salary} occupied by {employee_data[update_salary]['name']}")
            print(f"Current salary of {employee_data[update_salary]['name']} is ${employee_data[update_salary]['salary ($)']}")
            new_salary = float(input("Enter new salary: "))
            employee_data[update_salary]['salary ($)'] = new_salary
            print("Salary updated successfully.")
            print(f"Updated record:{employee_data[update_salary]}")
        else :
            print("Employee ID not found. Please try again.")
            continue
    elif user_task == 4:
        del_record = int(input("Enter employee ID to delete record: "))
        if del_record in employee_data.keys():
            print(f"Employee ID {del_record} occupied by {employee_data[del_record]['name']}")
            confirm_deletion = input("Are you sure you want to delete this record? (yes/no): ")
            if confirm_deletion.lower() == "yes":
                employee_data[del_record] = "Employee has terminated."
                print("Employee record deleted successfully.")
                user_request = input("Do you want to view updated database? (yes/no): ")
                if user_request.lower() == "yes":
                    print(employee_data)
                else:
                    continue
            else:
                print("Deletion cancelled.")
        else:
            print("Employee ID not found. Please try again.")
            continue
    elif user_task == 5:
        count = 0
        for i in employee_data:
            if employee_data[i] == "Employee has terminated.":
                pass
            else:
                count += 1
        print(f"There are currently {count} employees")
    elif user_task == 6:
        employee_salary = []
        for i in employee_data:
            employee_salary.append(employee_data[i]['salary ($)'])
        highest_salary = max(employee_salary)
        for j in employee_data:
            if employee_data[j]['salary ($)'] == highest_salary:
                print(f"Highest earner is {employee_data[j]['name']} with a salary of ${highest_salary}")
    elif user_task == 7:
        sum_of_salary = 0
        for i in employee_data:
            sum_of_salary += employee_data[i]['salary ($)']
        average_salary = sum_of_salary // max(employee_data)
        # print(sum_of_salary)
        print(f'The average salary of all employees is ${average_salary}')
    elif user_task == 8:
        print("List of departments available: \n" \
        "- HR \n" \
        "- IT \n" \
        "- Finance \n" \
        "- Marketing \n" \
        "- Sales \n" \
        "- Management")
        dept_name = input("Enter department name: ")
        print(f"Employees in {dept_name} department:")
        for i in employee_data:
            if employee_data[i]['department'].lower() == dept_name.lower():
                print(f"- {employee_data[i]['name']}")
    elif user_task == 9:
        employee_id = int(input("Please insert employee ID: "))
        if employee_id in employee_data:
            print(f'Information on employee with ID {employee_id} as follows: \n {employee_data[employee_id]}')
        else:
            print("Employee ID is not in database. Please retry.")
    elif user_task == 10:
        departments = []
        for i in employee_data:
            departments.append(employee_data[i]["department"])
        departments = (set(departments))
        for i in departments:
            print(f"Employees in {i} department:")
            for j in employee_data:
                if employee_data[j]['department'] == i:
                    print(f"- {employee_data[j]['name']}")
            print("")
    elif user_task == 11:
        bonus_id = int(input("Enter desired employee ID: "))
        if bonus_id in employee_data:
            bonus_percentage = float(input("Enter percentage of bonus: "))
            original_salary = employee_data[bonus_id]['salary ($)']
            bonus_amount = original_salary * (bonus_percentage / 100)
            desired_salary = original_salary + bonus_amount
            employee_data[bonus_id]['salary ($)'] = desired_salary
            print(f"Bonus granted successfully. New salary of {employee_data[bonus_id]['name']} is ${desired_salary}")
        else: 
            print("Employee ID not found. Please try again.")
    elif user_task == 12:
        exit_database = input("Do you want to exit database?(yes/no): ")
        if exit_database.lower() == "yes":
            print("Leaving database...")
            break
        else:
            print("Phew.. That was close!")
            continue
    else:
        print("Invalid input. Please try again.")
        continue    