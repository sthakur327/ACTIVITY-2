# Python Program to Put Even and Odd Numbers in Separate List
#program to open odd.txt and even.txt files
file = open("input.txt","rt")
for i in file:
    if i.strip:
        num = int(i)
        if (num % 2 == 0):
            even = open("even.txt","a")
            even.write(str(num))
            even.write("\n")
        else:
            odd = open("odd.txt","a")
            odd.write(str(num))
            odd.write("\n")

