# Clase queue: Implementar la clase queue que implementa una cola a partir de nodos enlazados.
# Implementar los métodos públicos

class Empty(Exception):
    pass


class Node:
    def __init__(self, data, next) -> None:
        self._data = data
        self._next = next


class Queue:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self) -> None:
        return self._size

    def is_empty(self):
        if self._size:
            return True
        else:
            return False

    def push(self, data):
        if self._head == None:
            self._head = self._tail = Node(data, None)
        else:
            new_node = Node(data, None)
            self._tail._next = new_node
            self._tail = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise (Empty("Empty Queue"))
        answer = self._head._next
        self._size -= 1
        return answer

    def top(self):
        return self._head._data


    def destructive_print(s):
        L = []
        while len(s) > 0:
            L.append(s.pop())
        print(L)


if __name__ == '__main__':
    q = Queue()
    for j in range(10):
        q.push(j)
        q.destructive_print(q)
