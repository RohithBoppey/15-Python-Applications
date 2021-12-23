def win(l):
    if(l[0] == l[1] == l[2] and l[0] != " "):
        return l[0]
    elif(l[0] == l[3] == l[6] and l[0] != " "):
        return l[0]
    elif(l[0] == l[4] == l[8] and l[0] != " "):
        return l[0]
    elif(l[1] == l[4] == l[7] and l[1] != " "):
        return l[1]
    elif(l[3] == l[4] == l[5] and l[3] != " "):
        return l[3]
    elif(l[6] == l[7] == l[8] and l[6] != " "):
        return l[6]
    elif(l[2] == l[5] == l[8] and l[2] != " "):
        return l[2]
    elif(l[2] == l[4] == l[6] and l[2] != " "):
        return l[2]
    else:
        return 0