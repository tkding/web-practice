name = "Harry"

print(name[0])
print()

#list
names = ["Harry", "Ron", "Alex"]
print(names)
print(names[0])

names.append("Draco")
names.sort()
print(names)
print()

#tuple
coordinate = (10.0, 20.0)
print(coordinate)

#set
s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

print(s)
s.remove(2)
print(s)
print(f"The set has {len(s)} elements now")
print()

#dict
