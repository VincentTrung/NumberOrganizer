# ask for input and turn into list
numlist = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numlist.append(item)


# sort function
def merge_sort(l):
    if len(l) > 1:          #split into 2 parts
        middle = len(l)//2
        left = l[:middle]
        right = l[middle:]

        merge_sort(left)    #recursive for left and right
        merge_sort(right)

        x = 0   #x and y to traverse the two halves
        y = 0
        z = 0    #therefore makes values in k sorted

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                l[z] = left[x]
                x += 1
            else:
                l[z] = right[y]
                y += 1
            z += 1

        while x < len(left):
            l[z] = left[x]
            x += 1
            z += 1

        while y < len(right):
            l[z] = right[y]
            y += 1
            z += 1

merge_sort(numlist)
print (numlist)