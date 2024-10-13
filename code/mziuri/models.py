class Member:
    def __init__(self, name, age, status) -> None:
        self.name = name
        self.age = age
        self.status = status

class Teacher(Member):
    def __init__(self, name, age, status, subject, salary) -> None:
        super().__init__(name, age, status)
        self.subject = subject
        self.salary = salary
    
    def calculate_yearly_salary(self):
        return self.salary * 12

class Student(Member):
    def __init__(self, name, age, status, grade):
        super().__init__(name, age, status)
        self.grade = grade

    def __str__(self) -> str:
        return f"name: {self.name}, age: {self.age}, " \
        f"status: {self.status}, grade: {self.grade}"

shotiko = Teacher(
    "shotiko",
    21,
    "teacher",
    "Python",
    100000
)

lizi = Student("lizi", 14, "student", "95.7")

print(f"{shotiko.name}'s yearly salary: {shotiko.calculate_yearly_salary()} \n")

print(lizi.__str__())
