# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         min_idx=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_idx]:
#                 min_idx=j
#         arr[i],arr[min_idx]=arr[min_idx],arr[i]

#         return arr

# def kichik(sonlar, r):
#     tartiblangan = selection_sort(sonlar)
#     return tartiblangan[-r]


# print(kichik([18, 7, 25, 3, 11], 5))





# def selection_sort(a):
#     n = len(a)
#     for i in range(n - 1):
#         m = i
#         for j in range(i + 1, n):
#             if a[j] < a[m]:
#                 m = j
#         a[i], a[m] = a[m], a[i]
#     return a

# students = [
#     ["ali"],
#     ["vali"],
#     ["hasan"],
#     ["akmal"],
#     ["dilshod"]
# ]

# print(selection_sort(students))
    


def selection_sort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            if arr[j][1] < arr[m][1]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr


oquvchilar = [
    ["Bunyod", 85],
    ["Mansur", 62],
    ["Abdullo", 98],
    ["Bekzod", 71],
    ["Hasan", 90]
]

selection_sort(oquvchilar)

print(oquvchilar)
print("Eng kichik ball:", oquvchilar[0][0], "-", oquvchilar[0][1])
print("Eng katta ball:", oquvchilar[-1][0], "-", oquvchilar[-1][1])






3