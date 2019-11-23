def main():
    list = [[1,'a'],[2,'b'],[3,'c'],[4,'d'],[5,'e']]
    # var = list[1][1]
    # list[0][1] = var
    # var = list[2][1]
    # list[1][1] = var
    # var = list[3][1]
    # list[2][1] = var
    # var = list[4][1]
    # list[3][1] = var
    go = input("Put desired input")
    go = ord(go) - 65
    
    for pos in range(len(list)):
        pos = (pos+go) % 5
        print(list[pos][1])

        # list[i+1] = [list[i][1]]
    # var1 = list[4][1]
    # list[3][1] = var
    # list.append(var)
    # print(var)
    # print(list)
main()
