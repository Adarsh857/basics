#conditionals
#if
  #  elif
   # else
    #if if condition:
    #statement/algo

    # elif condition:
    #statement/algo:

    #
 #   else:
#statemnt algo

'''x=int(input('enter the number'))
y=int(input('enter the number'))
if x>y:
    print('x is greater')
elif x<y:
    print('y is greater')
else:
    print('both are equal')'''

#fibonaci series
'''first =0;
second=1;
n=int(input('enter the number of terms'))
if n==0:
    print('no serries')
elif n==1:
    print(0)
elif(n==2):
    print(first,'\n')
    print(second,'\n')
elif n>2:
    while n<=2:
        print(first, '\n')
        print(second, '\n')
n=n-2
while n>=1:
    third =first+second
    print(third,'\n')
    first=second
    second=third
    n-=1'''
#palidrom
'''n=int(input('enter the number of terms'))
m = n
sum = 0
while n >0:
    rem = n%10
    sum=(sum*10)+rem
    n=n/10
    if sum==m:
        print('palidrom')
    else:
        print('non palidrom')'''

'''' tupple is a data structure which is inmutable in nature
  variable_name =(elements,'elements')'''
'''a = (1, 2, 3, 'a', '#')
print(a[2])  # inndexing
print(a[2:4])  # slicing'''
'''a=[1,2,3]
print(a)
print('ater addition')
a.append('adarsh')
print(a)'''
#dictionary:it is also data structure it is mutable butit works on the principle of key value pair
# varible_name={key:value}
#dictionary
#break: to get out from the loop
'''a={'key':1,12:'python','jack':'rose',50:85}
print(type(a))
print(a)'''
