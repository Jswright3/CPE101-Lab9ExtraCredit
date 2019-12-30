# Project 6
# Name: John Wright
# Instructor: Sussan Einakian
# Section: 101-05
def nested_sum(list):
   #list -> int
   #returns sum of nested list
   sum = 0
   for i in list:
      for i in i:
         sum += int(i)
   return sum


def capitalize_nested(list):
   #list -> list
   #returns new nested capitalized list
   caplist = []
   for i in list:
      for i in i:
         caplist.append(i.capitalize())
   return caplist


def cumulative(list):
   #list -> list
   #returns list with each value being the sum of the first i + 1 elements from the original list.
   sum = 0
   newlist = []
   for i in list:
      sum += i
      newlist.append(sum)
   return newlist


def middle(list):
   #list ->list
   #returns list without first and last element
   newlist = []
   index = 0
   for i in list:
      length = len(list)
      if index == 0 or index == (len(list)-1):
         pass
      else:
         newlist.append(i)
      index += 1
   return newlist


def chop(list):
   #list -> list
   # takes a list, modifies it by removing the first and last elements, prints the new list and returns the new list
   newlist = middle(list)
   print(newlist)
   return newlist


class Person:
   #str, int -> str
   #creates class for Person
   def __init__(self,name,age):
      self.name = name
      self.age = age


   def __repr__(self,):
      return 'Name:{} Age:{}'.format(self.name,self.age)

   def __eq__(self,other):
      if self.name == self.name and self.age == self.age:
         return True
      else:
         return False




class Student:
   #str,str,int -> str
   #creates class for students
   def __init__(self,person,major,gpa):
      self.person = person
      self.major = major
      self.gpa = gpa


   def __repr__(self):
      return 'Person: {} Major: {} GPA: {}'.format(self.person,self.major,self.gpa)


   def __eq__(self,other):
      if self.major == major and self.gpa == gpa:
         return True
      else:
         return False


def average(p1,p2):
   #2 objects -> int
   #returns avg gpa of two students
   return (p1.gpa/2 + p2.gpa)/2


