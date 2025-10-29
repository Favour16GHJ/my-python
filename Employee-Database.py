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
# print(type(employee_data.keys()))


# 1. Print the name and department of all employee.

# for x , y in employee_data.items():
#     print(f'{y['name']} : {y["department"]}')

print(employee_data)

# Before that, start user interaction.
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

    # 1. Print the name and department of all employee(Task 1).
    if user_task == 1:
        for x , y in employee_data.items():
            print(f'{y['name']} : {y["department"]}')
   

# 2. Add a new employee record.(Task 2)

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

# 3. Update employee salary.(Task 3)

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

# 4. Delete employee from the record(Task 4).
    elif user_task == 4:
        del_record = int(input("Enter employee ID to delete record: "))
        if del_record in employee_data.keys():
            print(f"Employee ID {del_record} occupied by {employee_data[del_record]['name']}")
            confirm_deletion = input("Are you sure you want to delete this record? (yes/no): ")
            if confirm_deletion.lower() == "yes":
                employee_data[del_record] = "Employee has terminated."

                # del employee_data[del_record]
                print("Employee record deleted successfully.")

                # So basically, I am to rearrange the remaining records after deletion.
                # According to ChatGPT,
                ## Rearrange IDs (renumber)
                # new_employees = {}
                # new_id = 1
                # for key in sorted(employees.keys()):
                #     new_employees[new_id] = employees[key]
                #     new_id += 1
                # employees = new_employees  # 🔥 This is where replacement happens

                # reordered_data = {}
                # new_id = 1
                # for key in sorted(employee_data.keys()):
                #     reordered_data[new_id] = employee_data[key]
                #     new_id += 1
                # employee_data = reordered_data 

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
        # Ask Sir Henry how to make the remaining records arrange themselves after deletion. 
        # Okay don't bother, you used his idea on Employee Resigned instead.


# 5. Display the total number of employee currently in the dictionary( Task 5).

    elif user_task == 5:
        # print(f'There are currently {max(employee_data)} employees in the database')
        # This would pose an issue as deleted employees would still be counted. 
        # FIND A SOLUTION TO AFTER DELETION ARRANGEMENTS.
        count = 0
        for i in employee_data:
            if employee_data[i] == "Employee has terminated.":
                pass
            else:
                count += 1
        print(f"There are currently {count} employees")

# 6. find and display the employee with the highest salaryc(Task 6).
    # You would have to compare each one to the last and to the rest, read up on multiple comparisons in python.
    # So apparently you could just use the in built max() function
    # But you need to figure out a way to get the salary value
    #       # print(max(value['salary ($)']))
            # TypeError: 'int' object is not iterable
        # print(max(employee_data[key]['salary']))
    #  So you should first of all extract all the salaries into an iterable list, then apply max() on that list. For example
    #   # ages = []
        # for e in employees:
        #     ages.append(employees[e]["age"])

        # print(max(ages))
        #for e in employees:
        # if employees[e]["age"] == highest_age:
        #     print(f"Employee with highest age is {employees[e]['name']} with age {highest_age}")

    elif user_task == 6:
        employee_salary = []
        for i in employee_data:
            employee_salary.append(employee_data[i]['salary ($)'])
        highest_salary = max(employee_salary)
        for j in employee_data:
            if employee_data[j]['salary ($)'] == highest_salary:
                print(f"Highest earner is {employee_data[j]['name']} with a salary of ${highest_salary}")

    # Alternatively,
    #highest_age = 0
    # oldest_employee = ""

    # for e in employees:
    #     if employees[e]["age"] > highest_age:
    #         highest_age = employees[e]["age"]
    #         oldest_employee = employees[e]["name"]

    # print(f"Employee with highest age is {oldest_employee} with age {highest_age}")


# 7. Calculate and print the average salary of all employees (Task 7).
    elif user_task == 7:
        sum_of_salary = 0
        for i in employee_data:
            sum_of_salary += employee_data[i]['salary ($)']
        average_salary = sum_of_salary // max(employee_data)
        # print(sum_of_salary)
        print(f'The average salary of all employees is ${average_salary}')


# 8. List the names of employees who work at a particular department (Task 8)

    elif user_task == 8:
        print("List of departments available: \n" \
        "- HR \n" \
        "- IT \n" \
        "- Finance \n" \
        "- Marketing \n" \
        "- Sales \n" \
        "- Management")
        i_name = input("Enter department name: ")
        print(f"Employees in {i_name} department:")
        for i in employee_data:
            if employee_data[i]['department'].lower() == i_name.lower():
                print(f"- {employee_data[i]['name']}")

# 9. Enter an employee ID and view that employee's full record (Task 9).
    elif user_task == 9:
        employee_id = int(input("Please insert employee ID: "))
        if employee_id in employee_data:
            print(f'Information on employee with ID {employee_id} as follows: \n {employee_data[employee_id]}')
        else:
            print("Employee ID is not in database. Please retry.")
# 10. Group employees by department and print all names under each. (Task 10)

    elif user_task == 10:
        departments = []
        for i in employee_data:
            # print(employee_data[i]["department"])
            departments.append(employee_data[i]["department"])
        departments = (set(departments))
        # print(departments)
        for i in departments:
            print(f"Employees in {i} department:")
            for j in employee_data:
                if employee_data[j]['department'] == i:
                    print(f"- {employee_data[j]['name']}")
            print("")
        

# 11. Add bonus for any employees by percentage. (Task 11)
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

#12. Exiting the database(Additional Task 12)
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

## Finished at approx 6hours 30 minutes from 9:00 AM to 2:30 PM