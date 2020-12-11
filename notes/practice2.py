# s = 'lamba school wont return my emails when i have a problem'
# test = s

# def removeVowel(st):
#     # for e in st:
#     #     if e == 'a','e','i','o','u':
#     #         print(e)
#     newstr = [n for n in st]
#     for e in newstr:
#         if e == 'a,e,i,o,u':
#             print(e)
#     # print(newstr)



# removeVowel(s)
# print(id(s),id(test))

# def foo(n):
#     i = 1
#     while i < n:
#         print(i)
#         i *= 2

# foo(6)

# def doThings(items):
#     last = len(items) - 1
#     print(len(items))
#     print(items[last])

#     middle = len(items) / 2
#     i = 0
#     while i < middle:
#         print(items[i])
#         i += 1

#     for num in range(100):
#         print(num)

# i = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105]
# doThings(i)


def twoSum(numbers,target):
    d = {}
    sol = []

    for i in range(len(numbers)):
        d[numbers[i]] = i
    for e in d:
        if target - e != e and target - e in d:
            sol.append(d[e])
    print(sol)
    print(d)

n = [3,4,5]
twoSum(n,8)