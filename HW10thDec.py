
N = "Ajinkya Gode"

print(len(N))

# Positive slicing (5)
print(N[0:3])
print(N[1:7])
print(N[4:7])
print(N[8:11])
print(N[3:9])

# Negative slicing (5)
print(N[-12:-9])
print(N[-11:-5])
print(N[-8:-1])
print(N[-4:])
print(N[-10:-7])

# Positive step size (4)
print(N[0:12:2])
print(N[1:10:3])
print(N[2:11:2])
print(N[0:11:4])

# Negative step size (4)
print(N[::-1])
print(N[11:7:-1])
print(N[-1:-10:-2])
print(N[6::-1])

# Reverse slicing patterns (4)
print(N[11:0:-1])
print(N[8:2:-1])
print(N[-1:-8:-1])
print(N[-5:-12:-1])

# Mixed index slicing (4)
print(N[2:-2])
print(N[1:-4])
print(N[-10:7])
print(N[3:-3])

# Start / End slicing (2)
print(N[:5])
print(N[6:])

# Full slice variations (2)
print(N[:])
print(N[::3])

# Iteration – frequency (2)
count = 0
for ch in N:
    if ch == "a":
        count += 1
print("Small a =", count)

count2 = 0
for ch in N:
    if ch.lower() == "a":
        count2 += 1
print("A/a =", count2)
