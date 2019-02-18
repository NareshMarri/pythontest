#!/usr/bin/python
class sample:
 def __init__(self,name,age):
     self.name=name
     self.age=age
 def myfunction(abc,name):
     abc.name=name

p1=sample("Naresh",36)
p1.myfunction("Mahesh")
