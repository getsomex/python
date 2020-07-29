# doc strings let us comment about the function
# when someone will invoke the function the comment will pop up
def test(a):
    '''
    Infor: this function tests and prints parama a
    '''
    print(a)


test('!!!!')

print(test.__doc__)  # will show the comment
