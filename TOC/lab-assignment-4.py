#!/usr/local/bin/python3

print("\n")

w = input("Enter the first string: ")
s = input("Enter the second string: ")
substring_w = []
temp =[]

for i in range(len(w)):
    [temp.append(w[x:i+1]) for x in range(len(w))]
substring_w = list(set(sorted(temp)))

if s==w:
    print("The string '{}' is improper substring of '{}'".format(s,w))
elif s in substring_w:
    print("The string '{}' is proper substring of '{}'".format(s,w))
else:
    print("The string '{}' is not a substring of '{}'".format(s,w))

print("\n")
