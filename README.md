import random

class Student:

   def __init__(self, name):

       self.name = name

       self.gladness = 50

       self.progress = 0

       self.alive = True

       self.money = 0

   def to_study(self):

       print("Time to study")

       self.progress += 0.12

       self.gladness -= 3

   def to_chill(self):

       if self.money >= 10:

           print("Time to chill")

           self.gladness += 5

           self.progress -= 0.1

           self.money -= 10

       else:

           print("Not enough money to chill. Time to work.")

           self.to_work()

   def to_sleep(self):

       print("Time to sleep")

       self.gladness += 2

       self.progress -= 0.05

   def to_work(self):

       print("Time to work")

       self.money += 20

       self.progress -= 0.1

   def is_alive(self):

       if self.progress < -0.5:

           print("Cast out…")

           self.alive = False

       elif self.gladness <= 0:

           print("Depression…")

           self.alive = False

       elif self.progress > 5:

           print("Passed externally…")

           self.alive = False

   def end_of_day(self):

       print(f"Gladness = {self.gladness}")

       print(f"Progress = {round(self.progress, 2)}")

       print(f"Money = {self.money}")

   def live(self):

       for day in range(1, 366):

           day_str = f"Day {day} of {self.name}'s life"

           print(f"{day_str:=^50}")

           live_cube = random.randint(1, 4)

           if live_cube == 1:

               self.to_study()

           elif live_cube == 2:

               self.to_sleep()

           elif live_cube == 3:

               self.to_chill()

           elif live_cube == 4:

               self.to_work()

           self.end_of_day()

           self.is_alive()

           if not self.alive:

               print(f"{self.name} died on day {day}.")

               break
