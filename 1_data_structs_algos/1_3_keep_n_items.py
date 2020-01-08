import pdb
from collections import deque


# yields the matching line along with previous N lines
def search(lines, pattern, history=5):
    # creates a queue that holds a max of "history" values
    previous_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
        
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)

# Deque max size is set, as the q extends, it removes older values
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

# If you dont give it a size it can append and pop items on either end
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)
