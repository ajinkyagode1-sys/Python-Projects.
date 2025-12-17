s = set()
s.add(10)
s.add("Sai")
s.add(-30.7)
s.add(True)
s.add(True)
s.add(10)
s.add("Sai")

print(s)

s.remove(-30.7)

print(s)


s1 =  {11,30,99,45,-10,-11,"Hello there", "Jai Shri Ram",True,12,31,100,46,-10}
s2 = {11,30,99,45,-10,-11,"Hello there","Jai Shri Ram",True,12,31,100,46,-10,4,8}

s3 = s1.intersection(s2)      # Common Elements 
s4 = s1.union(s2)             # Unique Elements
# print(s3)
# print(s4)


fs = frozenset(s3)
fs1 = frozenset(s4)
print(fs)                  # FrozenSet
print(fs1)                  # FrozenSet

fs.add(11)   # ❌ error – frozen set is immutable


s = {100, 200, 307}        # Tuple in Set 

s.add((40, 50, 4))
print(s)


s = {100, 200, 307}          # List in Set

s.add([40, 50,4])
print(s)

