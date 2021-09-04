def remove(string,n):
    first=string[:n]
    last=string[n+1:]
    return first+last
string=input("Enter a string")
n=int(input("Enter the index of character to remove"))
print("Modified string")
print(remove(string,n))