class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def balance(myString):
        s=Stack()
        length = len(myString)
        index = 0
        while(index<length):
            paranth = myString[index]
            if paranth =="(":
                s.push(paranth)
                index += 1
            elif paranth == ")":
                try:
                    s.pop()
                    index += 1
                except:
                    myString.remove
