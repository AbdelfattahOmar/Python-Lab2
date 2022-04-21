from multipledispatch import *

@dispatch(int,int)
def add(num1,num2):
	result = num1+num2
	print("first add method result: ",result)


@dispatch(int,int,int)
def add(num1,num2,num3):
	result = num1 + num2 + num3
	print("second add method result: ",result)

add(1,2)
add(1,2,3)
