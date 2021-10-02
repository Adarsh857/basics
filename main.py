# we donot use curly braces for marking blocks instead we have indentation
#variable is a memory location in the CPU which is used to store the values
# anything and everything inside a single quotation or a double quotation ia a string
print('hello world')

a=112
b=2
print(a+b)
print(type(a))
#string
print('a')

#input()
#format variable_name=input('instruction')
a=input('enter the number')
print(a)   #input function will always give string as its type

#sum input
a=input('enter the number')
b=input('enter the number')
print(a+b)
#type casting varible_nmae=int(input('instruction))
# #we generally convert int and float
a=int(input('enter the number'))
print(type(a))

# phyton has 7 arthematic operator
'''+
-
*
/ - quotient is decimal 10/5=2.0
// -(floor devison) 11//5=2
%(modulus) remainder
**-exponential a**b
'''
print(10/5)
print(10//5)
print(10%3)
print(10**2)

'''
relatinonal operator
>
<
>=
<=
==(compare)
=(asignment)
'''
a=10;
b=20;
print(a>b)

'''
assignmnet operator
=
+=
-=
*=
/=
//=
%=
**=

'''
a=10;
a+=20;
print(a)

#multiplle times print
# if a job is to be down in reptition then it is done in repetion
# for and while
# for iterating_variable in range(lower_limit,upper_limit,step_jump)
# statement/algorithm
for i in range (0,20):
    print(i)


    #for loops follows n-1 rule upper limit id 10 . it will print 9 nbs.
    for i in range(0,5):
        print('hello world')

#alternatibe step jump function
for i in range(1,11,2):
    print('i')

    #reverse
    for i in range(10,1,-1):
        print(i)

#while loop
#iterating variable
#while(condition):
#statement /algorithm
#increment /decrement
i=0
while(i<10):
    print(i)
    i=i+1
    #if we know hoew many timews we ned toexecute we will use for loop and  and
    # if we dont know then we will use while loop