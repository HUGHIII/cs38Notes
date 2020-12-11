# def csWhereIsBob(names):
#     for name in names:
#         if name == 'Bob':
#             return names.index(name)
        
#     return -1
        



# l = ["Jimmy","Layla","Mandy","Bob"]
# csWhereIsBob(l)


# def csSquareAllDigits(n):
#     newstr = ''
#     for e in str(n):
#         newstr += str(int(e) * int(e))
#     print(newstr)


# csSquareAllDigits(9119)
import string

def scoolgroups(years, groups):
    sol = ''

    atoz = list(string.ascii_lowercase)
    for i1 in range(1,years + 1):
        for i2 in  range(groups):
            if len(sol) / 4 < years * groups:
                sol += str(i1) + atoz[i2] + ', '
        #  try making list of strings then join by comma space
    return print(sol)






scoolgroups(7,4)