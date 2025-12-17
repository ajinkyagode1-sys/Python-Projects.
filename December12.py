# l = []
# # print(type(l))
# # print(l)
# # print(len(l))
# # print(id(l))

# l.append(10)
# l.append(-20.5)
# # print(id(l))
# l.append("Sai Baba")
# l.append(True)
# # print(id(l))
# l.append("Sai")
# l.append(10)

# print(l)
# # print(len(l))
# # print(id(l))
# # Mutable --> Changeable


# # print(l[-1])
# # print(l[len(l)-1])

# # print(l[2])
# # print(l[4])

# # print(l[-2])
# # print(l[len(l)-2])

# # res = l[2]
# # print(res.count("a"))

# # print(l[2][4:])
# # print(l[2][1])

# chotu_list = ["Raj","Rahul","Pavan"]
# l.insert(2,chotu_list)
# # print(l)

# print(l[2][1][2])


# students_marks = [56,89,99,92,72,45,83,77,64,91]

# # How to remove data from list
# # remove method & pop method 
# print(students_marks)
# # ele = students_marks.pop(2)
# # print("Popped element:",ele)
# # print(students_marks)


# res = students_marks.remove(45)
# print("Removed element",res)
# print(students_marks)



l = [10, 20, 30]

t = (100, 200, 300)

l.append(t)

print(l)




for item in l:
    print(item)



print(l[3])       # complete tuple
print(l[3][0])    # tuple  1st element
print(l[3][1])    # tuple  2nd element



t = (1, 2, 3, [10, 20, 30])

print(t)



print(t[3])        # complete list
print(t[3][0])     # list  first element
print(t[3][2])     # list  third element


print(t[0:3])


t[3].append(40)
print(t)
