'''#Find length of a string in python (4 ways)
length of string
for loop
find length'''
#Python program to print even length words in a string

s=input("emter the value:")
#s=s.split(" ")
for word in s:
    if len(s)%2==0:
        print(word)
    else:
        print("not even")
