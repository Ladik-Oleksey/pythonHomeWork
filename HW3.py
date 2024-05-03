class StudySubject:

 def __init__(self):

     self.name = input("Введіть назву предмету: Python ")

     self.hours = int(input("Введіть кількість годин: 3 "))

     self.enable = input("Чи є активним? (Так/Ні): Yes ").lower() == 'так'

 def info_study(self):

     print(f'Предмет: {self.name} | {self.hours} годин')

class Student:

 def __init__(self):

     self.name = input("Введіть ім'я студента: Олексій ")

     self.surname = input("Введіть прізвище студента: Ладік ")

     self.subjects = []

     num_subjects = int(input("Введіть кількість предметів: 1 "))

     for _ in range(num_subjects):

         print(f"\nВведіть дані для предмету {_+1}:")

         self.subjects.append(StudySubject())

 def info_student(self):

     print(f'Студент: {self.name} | {self.surname}')

 def info_all(self):

     self.info_student()

     for subject in self.subjects:

         subject.info_study()

class Group:

 def __init__(self):

     self.group_name = input("Введіть назву групи: C2126 ")

     self.num_students = int(input("Введіть кількість студентів у групі: 15 "))

     self.age_category = input("Введіть вікову категорію: 13-14 ")

     self.students = []

     for _ in range(self.num_students):

         print(f"\nВведіть дані для студента {_+1}:")

         self.students.append(Student())

 def display_group_info(self):

     print(f"\nНазва групи: C2126 {self.group_name}")

     print(f"Вікова категорія: 13-14 {self.age_category}")

     print(f"Кількість студентів: 15 {self.num_students}")

     print("\nІнформація про студентів: ")

     for student in self.students:

         student.info_all()



if __name__ == "__main__":

 group = Group()

 group.display_group_info()

