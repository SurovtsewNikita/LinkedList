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
        prev = None  # временная переменная
        current = self.head  # переменная с "головой"
        while current:  # цикл для обхода всего списка
            next_node = (
                current.next
            )  # временная переменная для запоминания след переменной
            current.next = prev  # замена следующего элемента
            prev = current  # временная переменная для соеденения
            current = next_node  # замена для перехода на следующий элемент
        self.head = prev  # завершение обратного списка

    def print(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


linlist = LinkedList()
linlist.append(10)
linlist.append(15)
linlist.append(20)

linlist.print()

linlist.reverse()
linlist.print()
