#Python program to check whether the string is Symmetrical or Palindrome
s=str(input("enter the value"))
n=len(s)//2
ss=s[:n]
print(ss)
if len(s)%2==0:
    ss=s[:n]
    sss=s[n:]
    if ss==sss:
        print("it is symetrical:")
    else:
        print("it is not symetrical:")
else:
     print("not symetricl")
        
reverse=s[::-1]
if s==reverse:
    print("yes it is polindrome")
else:
    print("not polindrome")

#Reverse words in a given String in Python
''''s1=input("enter the value:")
reverse=s1[::-1]
print("reverse", reverse)'''

#Ways to remove iâ€™th character from string in Python
"""s2="anu?!@radha"
alphanum=" "
for i in s2:
    if i.isalnum():
        alphanum +=i
print(alphanum)"""

