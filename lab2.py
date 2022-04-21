import re
import MySQLdb

dbConnect = MySQLdb.connect(host="localhost",user="root",password="1234",database='python')
cursor = dbConnect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employee(id int primary key not null,full_name varchar(100) not null,salary int not null,is_manager int);''')
dbConnect.commit()


class Person:
   def __init__(self, full_name, money,sleepmood,healthRate):
      self.full_name = full_name
      self.money = money
      self.sleepmood = sleepmood
      self.healthRate = healthRate

  
   def sethealthRate(self, healthRate):
       if healthRate>=0 and healthRate<=100:
          self.healthRate=healthRate
       else:
          print('healthRate value must be between 0 and 100')

   def sleep(self,hours):
      if hours==7:
          self.sleepmood = 'happy'
          print('happy')
      elif hours > 7:
          self.sleepmood = 'lazy'
          print('lazy')
      elif hours < 7:
          self.sleepmood = 'tired'
          print('tired')
      return self.sleepmood

   def eat(self,meals):
       if meals<=3 and meals>=1:
            if meals==3:
                self.healthRate = '100'
            elif meals==2:
                self.healthRate = '75'
            elif meals==1:
                self.healthRate = '50'
            return self.healthRate
       else:
           print('meals should be between 1 and 3')

   def buy(self,items):
          self.money-=10*items


class Employee(Person):

   def __init__(self,full_name, money,sleepmood,healthRate, id, email, workmood,salary,is_manager):

      Person. __init__(self, full_name, money,sleepmood,healthRate)
      self.id = id
      self.email = email
      self.workmood = workmood
      self.salary = salary
      self.is_manager = is_manager 
     

    
   def setsalary(self, salary):
       if(salary>=1000):
          self.salary = salary
       else:
          print('salary must exceed 1000')
    
   def getsalary(self):
       return self.salary

   def setemail(self, email):
      if(re.search('^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})$', email)):
         self.email = email
      else:
         print("Email not valid")



   def work(self,hours):
      if hours==8:
          self.workmood = 'happy'
          print('happy')
      elif hours < 8:
          self.workmood = 'lazy'
          print('lazy')
      elif hours > 8:
          self.workmood = 'tired'
          print('tired')
      return self.workmood

   def sendemail(self,subject,sentFrom,sentTo):
      print("email sent from ",sentFrom," to ",sentTo," with subject ",subject)

class Office:

   def __init__(self):
       pass
   
   def hire(self,id,full_name,salary,is_manager): 
      cursor.execute("INSERT INTO employee (id, full_name, salary,is_manager) Values(%s,%s,%s,%s)",(id,full_name,salary,is_manager))
      print("employee is hired")  
      dbConnect.commit()    
  
   def get_all_employees(self):
       cursor.execute('select * from employee')
       rows = cursor.fetchall()
       for row in rows:
            print(row)
       dbConnect.commit()
   
   def get_employee(self,num):
            cursor.execute(f'select * from employee where id={num}')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            dbConnect.commit()

   def fire(self,num):
      cursor.execute(f'delete from employee where id={num}')
      print("employee is fired")  
      dbConnect.commit()


choose=True
while choose:
    print ("""
    Welcome to our System

    1.Add a new employee
    2.Get all employees
    3.Get a specific employee
    4.Fire employee
    5.Exit
    """)
    choose=input("Choose a number from the list ") 
    if choose=="1": 
       office=Office()
       id = input("Enter employee id ")
       name = input("Enter employee name ")
       salary = input("Enter employee salary ")
       is_manager = input("Is this employee a manager? print 0 for no or 1 for yes ")
       office.hire(id,name,salary,is_manager)
    elif choose=="2": 
       office=Office()
       office.get_all_employees()
    elif choose=="3": 
       office=Office()
       id = input("Enter employee id ")
       office.get_employee(id)
    elif choose=="4": 
       office=Office()
       id = input("Enter employee id ")
       office.fire(id)
    
    elif choose=="5":
      print("\n Thanks, see you soon") 
      choose=False
    
  
              