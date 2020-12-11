arr1 = [1,5,3,2,6,9,8,6]
# arr2 = []

# for i in arr1:
#     arr2.append(i)
# for i in range(0,len(arr1)):
#     print(arr1[i])
def containsDupl(arr1):
    arr1.sort()
    print(arr1)
    dupl = []
    for i in range(0,len(arr1)-1):
        if arr1[i] == arr1[i + 1]:
            dupl.append(arr1[i])
            return True
        
    print(dupl)    

containsDupl(arr1)