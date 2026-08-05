def binary_search(royhat,target):
    left=0
    right=len(royhat)-1

    while left<=right:
        mid=(left+right) //2

        if royhat[mid]==target:
            return mid
        elif royhat[mid]<target:
            left=mid+1
        else:
            right=mid-1

sonlar = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(sonlar, 11))
