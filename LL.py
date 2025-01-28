class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)  # временная переменная, создание нода
        if not self.head:  # проверка на пустой список
            self.head = new_node  # преписываем голову
        else:  #
            current = self.head  # временная переменная с ссылкой на голову
            while current.next:  # проверка на наличие больше одного элемента в списке
                current = current.next  # переставляем на следующий элемент
            current.next = new_node  # соеденяем список с новыйм нодом

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


linlist = LinkedList()
linlist.append(10)
linlist.append(15)
linlist.append(20)

linlist.reverse()
