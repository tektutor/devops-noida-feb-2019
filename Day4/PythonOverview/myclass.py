#!/usr/bin/python

class MyClass:

      def __init__(self):
         self.x = 0
         self.y = 0

      def setValues(self,val1, val2):
         self.x = val1
         self.y = val2

      def printValues(self):
          print ( "Value of x is ", self.x )
          print ( "Value of y is ", self.y )


obj = MyClass()
obj.printValues()

obj.setValues ( 100, 200)
obj.printValues()
      
