def pyramida(n):
    for x in range(0, n):
        print(" "*(n-x-1) + "*"*(2*x + 1))


print(pyramida(3))
#   *
#  ***
# *****

print(pyramida(5))
#     *
#    ***
#   *****
#  *******
# *********