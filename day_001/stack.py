from replit import clear
clear()
stack_arr = [1,2,3,4,5,6]
new_stack = []
for i in range(len(stack_arr)):
    new_int = stack_arr.pop()
    new_stack.append(new_int)

print(new_stack)