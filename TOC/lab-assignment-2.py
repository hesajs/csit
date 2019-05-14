#!/usr/local/bin/python3

w = input("Enter the first string: ")
s = input("Enter the second string: ")
prefix_w = []
[prefix_w.append(w[:x+1]) for x in range(len(w))]

if s in prefix_w:
    if s==w:
        print("'{}' is Proper Prefix of '{}'".format(s, w))
    else:
        print("'{}' is Improper prefix of '{}'".format(s, w))
else:
    print("'{}' is not prefix of '{}'".format(s, w))
