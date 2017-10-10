Title: python中repr和str的区别 
Date: 2010-06-03 20:20
Category: python


    class Person(object):

        def __init__(self, name, gender):

            self.name = name

            self.gender = gender

        def __str__(self):

            return '(Person: %s, %s)' % (self.name, self.gender)
