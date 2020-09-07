my_list = ['a', 'b', 'c', 'd', 'n', 'n', 'b']
my_list.sort()
new_list = []

previosValue = ''
for element in my_list:
    if(element == previosValue):
        new_list.append(element)
    previosValue = element

print(new_list)
