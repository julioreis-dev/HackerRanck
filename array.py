
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    x = 0
    for n in ar:
        x=x+n
    return x

x = [1,2,3,4,10,11]
print(simpleArraySum(x))