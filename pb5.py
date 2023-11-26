# hike 15, 7,5


def hikeSalary(level, salary):
    if level == 3:
        total_salary = salary + ((salary * 15) / 100)  # + (23000 * 15)/100 ->  23000 + 345000 / 100
        return total_salary
    elif level == 4:  # 23000 + 3450 - >  26500
        total_salary = salary + ((salary * 7) / 100)
        return total_salary
    elif level == 5:
        total_salary = salary + ((salary * 5) / 100)
        return total_salary
    else:

        return "Invalid job number"


level = int(input("Enter your job level 3,4 or 5: "))
data = int(input("Enter your salary: "))
print("total_salary after hike is:",hikeSalary(level, data))
