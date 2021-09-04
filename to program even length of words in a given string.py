s=input("Enter a string:- ")
s=s.split(' ')
for word in s:
    if len(word)%2==0:
        print(word,end=" ")
'python program to print even length of words in a given string'