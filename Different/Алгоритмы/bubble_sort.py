# Метод сортировки пузырьком
# bubble sort циклом for
def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

print("Sort")
arr = []
n = int(input("Array length: "))
for i in range(0, n):
    element = int(input("arr[" + str(i + 1) + "] = "))
    arr.append(element)
bubble_sort(arr)
print("Sorted array: ")
print(arr)

# С помощью циклов while
# bubble sort_while

a = []
number = int(input("the Total Number of Elements : "))
for i in range(number):
    value = int(input("Enter %d Element of List1 : " %i))
    a.append(value)

i = 0
while(i < number -1):
    j = 0
    while(j < number - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp
        j = j + 1
    i = i + 1

print("The Sorted List in Ascending Order : ", a)


