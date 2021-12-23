# Reference diagram
# -------------------
#   1  |    2   |  3     
#   4  |    5   |  6    
#   7  |    8   |  9         
# -------------------

def printTable(l):
    print("-------------------")
    print("  {val1}  |    {val2}   |  {val3} ".format(val1 = l[0], val2 = l[1], val3 = l[2]))
    print("  {val1}  |    {val2}   |  {val3} ".format(val1 = l[3], val2 = l[4], val3 = l[5]))
    print("  {val1}  |    {val2}   |  {val3} ".format(val1 = l[6], val2 = l[7], val3 = l[8]))
    print("-------------------")