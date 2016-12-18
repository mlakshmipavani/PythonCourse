#version - python3
#input
s1 = input("first word\n")
s2 = input("second word\n")

#sorting
b1 = sorted(s1)
b2 = sorted(s2)

#checking if equal
if b1 == b2:
    print("Yes " + s1 + ","+ s2 + " are anagrams\n")
else:
    print("No " + s1 + ","+ s2 + " are not anagrams\n")