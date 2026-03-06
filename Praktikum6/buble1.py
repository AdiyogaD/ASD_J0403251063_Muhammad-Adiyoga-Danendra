# =================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : A2
# =================================

# Buble Sort Ascending
print('Buble Sort Ascending')
def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i] > data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [54,26,93,17,77,31,44,55,20]
bubbleSort(data)
print(data)

# Short Bubble Sort Ascending
print('\nShort Bubble Sort Ascending')
def Shortbubblesort(data):
    exchange = True
    passnum = len(alist)-1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1

alist = [54,26,93,17,77,31,44,55,20]
Shortbubblesort(alist)
print(alist)