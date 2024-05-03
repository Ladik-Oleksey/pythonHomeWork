class Person:
    firstName = str
    secondName = str
    age = int

    def init(self,  firstName: str,  secondName: str,  age: int):
        self.firstName = firstName
        self.secondName = secondName
        self.age = age

    def info_person(self):
       print(f"{self.firstName} {self.secondName} {self.age}")

class Student(Person):
    progress: float
    groupName: str
    pensione = int

    def init(self, firstName: str, secondName: str, progress: float, groupName: str, age: int, pensione: int):
        self.progress = progress
        self.groupName = groupName
        self.pensione = pensione

        self.age = age
        self.firstName = firstName
        self.secondName = secondName

Ladik = Student(progress=52, groupName="C2126", age=13, firstName="Oleksey", secondName="Ladik", pensione=55)
Ladik.info_person()

class teacher(Person):
    position = str
    salary = int

    def init(self, firstName: str, secondName: str, position: str, salary: int, age: int):
        self.position = position
        self.salary = salary

        self.age = age
        self.firstName = firstName
        self.secondName = secondName

polishko = teacher(position='teacher', salary=50000, age=30, firstName="Konstiantyn", secondName="Polishko")
polishko.info_person()

class Worker(Person):
    position = str
    salary = int
    duties = str
    pensione = int

    def init(self, firstName: str, secondName: str, position: str, salary: int, age: int, duties: str, pensione: int):
        self.position = position
        self.salary = salary
        self.duties = duties
        self.pensione = pensione

        self.age = age
        self.firstName = firstName
        self.secondName = secondName

Worker1 = Worker(position='Worker', salary=30000, age=52, firstName="Sergey", secondName="Kosow", duties='work', pensione=60)