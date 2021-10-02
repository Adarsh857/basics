#function: it is a block of code which is written fro a specific task and is executed only when called
#system  defined and user defined
'''
format of making a function
def function_name(argument if any):
statement/algorithm
function_name(value)
def fun_sum(a=10,b=20):
   print(a+b)
   fun_sum()

   def fun(a,b):
   print('the value a is',a,'the value of b is',b)
   temp=a
   a=b
   b=temp
   print('A=',a)
   print('B=',b)
   n=int(input('enter the number'))
   m=int(input('another value'))
fun(n,m)
# faactorial
n=int(input("enter the number"))
fact=1
while(n>1):
    fact = fact * n
    n-=1
    print(fact)

    #recursion factorail
def recur_function(n):
    if(n==1):
        return n
    else:
        return n*recur_function(n-1)
    num =int(inout("enter the number"))
    if num<0:
        print("no fact")
    elif num==0:
        print("zero")
    else:
        print("fact of num", num ,"is",recur_function(n) )
'''
