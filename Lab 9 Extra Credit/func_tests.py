# Lab 9
# Name: John Wright
# Instructor: Sussan Einakian
# Section: 101-05
import unittest
from funcs import *
class TestCases(unittest.TestCase):
   def test_nested_sum(self):
      list = [[1,2,3],[2,3],[8,3]]
      list2= [[1,2,3],[2,3],[8,1]]
      self.assertEqual(nested_sum(list),22)
      self.assertEqual(nested_sum(list2),20)


   def test_capitalize_nested(self):
      list = [['W', 'k', 'n'], ['r', 'm'], ['c', 'C']]
      list2 = [['Z', 'b', 'l'], ['A', 'c'], ['A', 'd']]
      self.assertEqual(capitalize_nested(list),['W', 'K', 'N', 'R', 'M', 'C', 'C'])
      self.assertEqual(capitalize_nested(list2), ['Z', 'B', 'L', 'A', 'C', 'A', 'D'])


   def test_cumulative(self):
      list = [1,2,3,4,5,6,6]
      list2 = [1,2,3]
      self.assertEqual(cumulative(list),[1, 3, 6, 10, 15, 21, 27])
      self.assertEqual(cumulative(list2),[1,3,6])


   def test_middle(self):
      list = [1,2,3,4,5,6,6]
      list2 = [1,2,3]
      self.assertEqual(middle(list),[2, 3, 4, 5, 6])
      self.assertEqual(middle(list2),[2])


   def test_chop(self):
      list = [1, 2, 3, 4, 5, 6, 6]
      list2 = [[1,2,3],4,5,6,7]
      self.assertEqual(chop(list), [2, 3, 4, 5, 6])
      self.assertEqual(chop(list2), [4,5,6])

   def test_person(self):
      self.assertEqual(Person('John',19),'Name:John Age:19')
      self.assertEqual(Person('Steve',12),'Name:Steve Age:12')

   def test_average(self):
      p1 = Student('Bill', 'CS', 3.56)
      p2 = Student('Sheryl', 'AG', 2.41)
      p3 = Student('Billeee', 'BS', 3.9)
      p4 = Student('Sherlie', 'CE', 1.2)
      self.assertEqual(average(p1,p2),2.095)
      self.assertEqual(average(p3, p4),1.575)




if __name__ == '__main__':
   unittest.main()

