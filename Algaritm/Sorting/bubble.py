def bubble_sort(royxat):
    n = len(royxat)

    for i in range(n):
        for j in range(0, n - i - 1):
            if royxat[j] > royxat[j + 1]:
                royxat[j], royxat[j + 1] = royxat[j + 1], royxat[j]

    return royxat


def katta(sonlar, r):
    tartiblangan = bubble_sort(sonlar)
    return tartiblangan[-r]


print(katta([2,34,5,23,4,1], 2))