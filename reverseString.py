str = "Ankit"
str_char = list(str)
print(str[::-1])



length = len(str)
    
rev_string = ''

    # iteration from the last character till
    # first character and cocatenating them
for index in range(length-1,-1,-1) :
    rev_string += str[index]

print(rev_string)


import sys

def push(element, size, stack):
    '''
    this function is used to push the elements
    in the stack and it will return Error! message
    if the stack is full and terminate the program.
    '''
    global top
    if top >= size - 1:
        print('Stack Overflow')
        sys.exit()
    else:
        top += 1
        stack[top] = element

def pop():
    '''
    this function is used to pop elements from
    the stack and it will return Error! message
    if the stack is empty and terminate the program.
    '''
    global top
    if top < 0:
        print('Stack Underflow')
        sys.exit()
    else:
        element = stack[top]
        print('%s' % element, end='')
        top -= 1

def reverse_by_sort(string):
    '''
    This function is used to reverse any string
    by reversed() method.
    '''

    string = list(string)
    rev_str = ''
    
    for i in reversed(string):
        rev_str += i

    return rev_str

if __name__=='__main__':

    size = 11
    stack = [0]*size
    string = 'Includehelp'
    top = -1

    # Pushing value in the stack
    push('I', 11, stack)
    push('n', 11, stack)
    push('c', 11, stack)
    push('l', 11, stack)
    push('u', 11, stack)
    push('d', 11, stack)
    push('e', 11, stack)
    push('h', 11, stack)
    push('e', 11, stack)
    push('l', 11, stack)
    push('p', 11, stack)

    print('Original String = %s' % string)
    
    print('\nUsing Stack')

    # Popping values from stack and printing them
    print('Reversed String = ',end='')
    for i in stack:
        pop()

    print('\n\nUsing sort()')
    print('Reversed string = %s' % reverse_by_sort(string))
