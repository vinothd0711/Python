l1 = input('Enter the list of numbers:')
l2 = input ('Enter the list of numbers:')
l3 = l1 + " " + l2
final = []
print(l3)
for i in l3:
    if i not in final:
        final.append(i)
output = type(final)
print(final)
    
