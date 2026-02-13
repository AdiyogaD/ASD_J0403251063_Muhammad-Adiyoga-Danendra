class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Menyimpan node terakhir untuk traversing
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def display_forward(self):
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
        
    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")

    # Mencari elemen
    def search(self, key):
        temp = self.head
        while temp != None:
            if temp.data == key:
                return True
            temp = temp.next
        return False

dll = DoublyLinkedList()
input_data = input("Masukkan data (Pisahkan dengan koma (,)): ") # User memasukkan data (2,6,9,14,20)
search_ele = int(input("Masukkan elemen yang ingin dicari: ")) # User memasukkan elemen yang ingin dicari

data = input_data.split(",")
for i in data:
    dll.insert_at_end(int(i))

dll.display_forward()
dll.display_backward()

if dll.search(search_ele):
    print("\nElemen ditemukan")
else:
    print("\nElemen tidak ditemukan")