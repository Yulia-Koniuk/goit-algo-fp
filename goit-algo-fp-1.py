class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# функція реверсування однозв'язного списку
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# алгоритм сортування злиттям
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head

        middle = self.get_middle(self.head)
        next_to_middle = middle.next

        middle.next = None

        left = LinkedList()
        right = LinkedList()

        left.head = self.head
        right.head = next_to_middle

        left.merge_sort()
        right.merge_sort()

        self.head = self.sorted_merge(left.head, right.head)

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, left, right):
        dummy = Node()
        tail = dummy

        while left and right:
            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        elif right:
            tail.next = right

        return dummy.next

# Функція, що об'єднує два відсортовані однозв'язні списки
    def merge_two_sorted_lists(self, llist1, llist2):
        dummy = Node()
        tail = dummy

        l1 = llist1.head
        l2 = llist2.head

        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        self.head = dummy.next

# Використання функцій
# Створення двох невідсортованих списків
llist1 = LinkedList()
llist1.insert_at_end(20)
llist1.insert_at_end(3)
llist1.insert_at_end(15)
llist1.insert_at_end(8)
llist1.insert_at_end(30)
llist1.insert_at_end(45)

llist2 = LinkedList()
llist2.insert_at_end(25)
llist2.insert_at_end(5)
llist2.insert_at_end(1)
llist2.insert_at_end(35)
llist2.insert_at_end(18)
llist2.insert_at_end(12)

print("Невідсортований список 1:")
llist1.print_list()
print("Невідсортований список 2:")
llist2.print_list()

# Сортування двох списків
llist1.merge_sort()
llist2.merge_sort()

print("Відсортований список 1:")
llist1.print_list()
print("Відсортований список 2:")
llist2.print_list()

# Об'єднання двох відсортованих списків
merged_list = LinkedList()
merged_list.merge_two_sorted_lists(llist1, llist2)
print("Об'єднаний відсортований список:")
merged_list.print_list()

# Реверсування списку
print("Реверсований об'єднаний список:")
merged_list.reverse_list()
merged_list.print_list()


