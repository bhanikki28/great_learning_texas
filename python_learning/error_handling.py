print('Code to demonstrate error handling using try/except')
salary = []
while True:
    salary_details = input("Please enter Salary to add and zero to stop: ")
    try:
        salary_parsed = float(salary_details)
    except ValueError:
        print("Salary has to be number, please enter proper value")
        continue
    if( salary_parsed == 0):
        break

    if( salary_parsed < 0):
        continue
    if(salary_parsed > 0):
        salary.append(salary_parsed)

print(salary)