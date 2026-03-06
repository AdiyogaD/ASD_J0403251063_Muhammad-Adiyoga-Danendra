# =================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : A2
# =================================

def insertionSort(data):
    for index in range(1, len(data)):

        currentvalue = data[index]
        position = index

        while position > 0 and data[position-1] < currentvalue:
            data[position] = data[position-1]
            position = position - 1

        data[position] = currentvalue

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
insertionSort(data)
print(data)

# 1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
print(data[:5]) # 98, 89, 76, 68, 57

# 2. Kandidat berapa saja yang lolos? (index)
# 98 index ke-6, 89 index ke-3, 76 index ke-1, 68 index ke-8, 57 index ke-5
# maka kandidat yang lolos adalah 7, 4, 2, 9, dan 6