l = [1, 2, 3, 4, 5, 6]

l[0], l[-1] = l[-1], l[0]

print(l)
delet_element = l.pop(1)

print(f"Удаленный элемент = {delet_element}")
print(l)