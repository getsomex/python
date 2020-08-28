# pure funtions wont create effect on outside world eg; print
# wont interact with outside of its scope eg: accessing variable, list so on

wizard = {
    'name': 'Merlin',
    'power': 50
}


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3]))
