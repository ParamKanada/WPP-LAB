# Employee

class emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, emp):
            combined_salary = self.salary + other.salary
            return emp(f"{self.name} & {other.name}", combined_salary)

    def __sub__(self, other):
        if isinstance(other, emp):
            salary_difference = self.salary - other.salary
            return abs(salary_difference)

    def __str__(self):
        return f"Employee(Name = {self.name}, Salary = {self.salary})"
    
a = input("Enter Employee One Name = \n")
b = int(input("Enter Salary of Employee One = \n"))

emp1 = emp(a,b)

c = input("Enter Employee Two Name = \n")
d = int(input("Enter Salary of Employee Two = \n"))

emp2 = emp(c,d)

print("\nCombined Salary of Employees = \n")
combine = emp1 + emp2
print(combine)

print("\nCompared Salary of Employees = \n")
Diff = emp1 - emp2
print(Diff)