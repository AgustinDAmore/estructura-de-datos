class stack():

    __slots__ = 'items', "_size"

    def __init__(self):
        self.items = []
        self._size = 0

    def stack(self, x):
        self.items.append(x)
        self._size += 1

    def unstack(self):
        if self.is_empty():
            raise ValueError("The stack is empty")
        self._size -= 1
        return self.items.pop()

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def view_top(self):
        return self.items[-1]

    def copy(self):
        new_stack = stack()
        while not self.is_empty():
            new_stack.apilar(self.desapilar())
        return new_stack

# funciones python
    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return str(self.items)
    
    def __len__(self):
        return len(self.items)