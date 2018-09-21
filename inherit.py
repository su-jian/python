#!/usr/bin/python
#author:dongshuang
#function:use class method to display something your input
class schoolmember:
    '''represents any school member.'''
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        print '(initialized schoolmember:%s)'%self.name

    def tell(self):
        '''tell my details.'''
        print 'name:"%s" age:"%s"'%(self.name,self.age),

class teacher(schoolmember):
    '''represents a teacher.'''
    def __init__(self,name,age,salary):
        schoolmember.__init__(self,name,age)
        self.salary=salary
        print '(initialized teacher: %s)'%self.name

    def tell(self):
        schoolmember.tell(self)
        print 'salary: "%d"'%self.salary

class student(schoolmember):
    '''repersents any school member'''
    def __init__(self,name,age,marks):
        schoolmember.__init__(self,name,age)
        self.marks=marks
        print '(initialized student: %s)'%self.name
    def tell(self):
        schoolmember.tell(self)
        print 'mark: "%d"'%self.marks

y_type=raw_input('please input you type [teacher|student]: ')
y_name=raw_input('please input your name: ')
y_age=int(raw_input('please input your age: '))
y_sa_mak=int(raw_input('please input your salary|marks: '))

if y_type=='teacher' :
    y=teacher(y_name,y_age,y_sa_mak)
    y.tell()
else:
    y=student(y_name,y_age,y_sa_mak)
    y.tell()
