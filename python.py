"""a = ["DATA","python","python","science","DATA","Machine Learning"]
append_values = []
for items in range(0, len(a)):
    index_a = 0
    a_value_pop = a.pop(index_a)
    if(a_value_pop) in a :
        append_values.append(a_value_pop)
    else:
        pass
    index_a += 1

print(append_values)"""
"""print(chr(65))
print(chr(90))"""
"""n= 65
for i in range(0,6):
    for j in range(0,i+1):
        print(chr(n))
"""
"""
STAR PATTERN IN PYTHON
"""
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print("*", end="  ")
    print("")
