from collections import deque
stack = ['Rahul','Mike','Rosa','Amy']
queue = deque(['Rahul','Mike','Rosa','Amy'])

stack.append('El')
queue.append('Will')
print(stack)
print(stack.pop())
print(queue)
print(queue.popleft())    #pop(0) implementation with list. Lists are considerably slower while removing elements from the front, hence deque