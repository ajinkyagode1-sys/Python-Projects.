# 1. Int Data Type 

print(10 + 20)        # 30 → int + int = addition
print(10 + 20.5)      # 30.5 → int + float = float
print(10 + True)      # 11 → True = 1

# print(10 + "Hello")     # ❌ TypeError → int + string not allowed
# print(10 + [1,2])       # ❌ TypeError → int + list not allowed
# print(10 + (1,2))       # ❌ TypeError → int + tuple not allowed
# print(10 + {1:10})      # ❌ TypeError → int + dict not allowed

# 2. String Data Type

s1 = "Hello"
s2 = "Python"
print(s1 + s2)        # HelloPython → string concatenation


# print("Hi" - "i")      # ❌ TypeError → subtraction not allowed
print("Hi" * 3)          # HiHiHi → repetition


# 3. List Data Type 

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

print(l1 + l2)       # [1,2,3,4,5,6,7,8,9,10] → concatenation
print(l1 * 2)        # [1,2,3,4,5,1,2,3,4,5]


# print(l1 - l2)        # ❌ TypeError → list subtraction not allowed


# 4. Tuple Data Type

t1 = (1,2,3)
t2 = (4,5)

print(t1 + t2)       # (1,2,3,4,5)
print(t1 * 2)        # (1,2,3,1,2,3)

# print(t1 - t2)        # ❌ TypeError


# 5. Set Data Type 

s1 = {1,2,3}
s2 = {3,4,5}

# print(s1 + s2)        # ❌ TypeError → + not supported
print(s1 - s2)          # {1,2} → set difference


# 6. Dictionary Data Type 

d1 = {1:10, 2:20}
d2 = {3:30, 4:40}

# print(d1 + d2)        # ❌ TypeError → dict + dict not allowed


# 7. None Data Type 

# print(None + None)    # ❌ TypeError
# print(None * 5)       # ❌ TypeError


# 8. Movies Dictionar Addition Check 

Movies2025 = {"Movie1": ["Actor1"]}
Movies2024 = {"Movie2": ["Actor2"]}

# print(Movies2025 + Movies2024)   # ❌ TypeError → cannot add dictionaries


# 9. Multiplication Checks 

print(3 * "Hi")         # HiHiHi
print(2 * [1,2])        # [1,2,1,2]
print(2 * (3,4))        # (3,4,3,4)

print(100 * "JAI SHRI RAM") # JAI SHRI RAM 100 Times 

# print(2 * {1:10})     # ❌ TypeError