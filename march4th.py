#Python program to interchange first and last elements in a list
l=[1,2,3,4,5]
lst=len(l)
temp=l[0]
l[0]=l[lst-1]
l[lst-1]=temp
print(l)

#Python program to swap two elements in a list
a=input("enter A value:")
b=input("enter B value:")
temp=a
a=b
b=temp
print(a,b)

"""#3. Python | Ways to find length of list
using len()
using length_hint()
using for loop"""

"""Maximum of two numbers in Python
5. Minimum of two numbers in Python"""

x=input("enter x value:")
y=input("enter y value:")
print("maximum:", max(x, y))
print("minimum:", min(x, y))
