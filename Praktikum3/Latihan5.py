class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # tambahkan pointer tail

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga merujuk ke node pertama
        else:
            self.tail.next = new_node # Menyambung kan tail ke node baru
            self.tail = new_node # Update tail node baru

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

ll = LinkedList()
input_data = input("Masukkan data (Pisahkan dengan koma (,)): ") # User memasukkan data

data = input_data.split(",")
for i in data:
    ll.insert_at_end(int(i))

# Normal
print("Linked List sebelum dibalik: ", end="")
ll.display()

# Reverse  
print("Linked List setelah dibalik: ", end="")
ll.reverse()
ll.display()