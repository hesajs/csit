#!/usr/local/bin/python3

'''
WAP that takes two inputs first a string (w) and second string (s) 
over some alphabet set , check whether the string s is suffix,proper suffix or not.
'''
w = input("Enter the first string: ")
s = input("Enter the second string; ")
suffix_w=[]
[suffix_w.append(w[x+1:len(w)]) for x in range(len(w))]

if s in suffix_w:
    print("'{}' is Proper Suffix of '{}'".format(s,w))
elif s == w:
    print("'{}' is Improper Suffix of '{}'".format(s,w))
else:
    print("'{}' is not Suffix of '{}'".format(s,w))
