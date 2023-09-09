class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop());
        return self.second[len(self.second)-1];


    def pop(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop());
        return self.second.pop();

    def put(self, value):
        self.first.append(value);


queue = MyQueue()
t = int(input("first"))
for line in range(t):
    values = map(int, input("the secinde").split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())