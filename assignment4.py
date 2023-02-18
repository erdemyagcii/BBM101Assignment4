import sys
f = open(sys.argv[1],"r")
list1 = f.readlines()
list2 = []
map = []
for i in list1:
    i = i.rstrip("\n")
    list2.append(i)
f.close()
for k in list2:
    k = k.split()
    map.append(k)
letters_value = {"B":9, "G":8, "W":7, "Y":6, "R":5, "P":4, "O":3, "D":2, "F":1, "X":0, " ":0}
first_score = 0
lenght = len(map[0])
if map[-1] != []:
    map.append([])




def draw_map():
    for i in map:
        for j in i:
            print(j + " ", end = "")
        print()

def enter_point():
    global point_axis
    global point_ordinate
    global point
    valid_input = input("Please enter a row and column number: ")
    valid_input = valid_input.split()
    point_axis = int(valid_input[1])
    point_ordinate = int(valid_input[0])
    point = map[point_ordinate][point_axis]



def mark_point():
    check_check = 0
    global cordinates
    tax = point_axis
    tord = point_ordinate
    cordinates = [[point_axis, point_ordinate]]
    tempcordinates = []
    tempcheck = []
    x = True

    while x:
        relcordinates = [[tax+1, tord], [tax-1, tord], [tax, tord+1], [tax, tord-1]]
        for i in relcordinates:
            try:
                assert i[0] >= 0 and i[1] >= 0
                if map[i[1]][i[0]] == point:
                    tempcordinates.append(i)
                    tempcheck.append(i)
                    check_check = check_check + 1 
                    if i not in cordinates:
                        cordinates.append(i)
            except AssertionError:
                pass
            except IndexError:
                pass
        if check_check == 0:
            print("Cannot delete any ball, Please try again!")
            enter_point()
            mark_point()
            break

        for j in tempcordinates:
            tax = j[0]
            tord = j[1]
            tempcordinates.remove(j)
            break
        if len(tempcheck) > len(map)*len(list1)*4000 : #if code dont run correctly please change the constant number in the expression
            x = False

def cal_score():
    global first_score
    initial_score = len(cordinates)*letters_value[point]
    first_score = initial_score + first_score
    return first_score

def del_letters():
    cordinates2 = []
    map.remove([])
    for i in cordinates:
        map[i[1]][i[0]] = " "
    for a in range(0, lenght):
        for b in range(0,len(map)):
            try:
                if map[b][a] != " ":
                    break
                if map[b][a] == " " and b == len(map)-1:
                    for c in range(len(map)):
                        cordinates2.append([a,c])
            except IndexError:
                pass
    cordinates2.sort(reverse=True)
    for d in cordinates2:
        map[d[1]].pop(d[0])
    map.append([])
def swp_columns():
    for y in range(len(map)-1,0,-1):
        for x in range(len(map[y])):
            control = 1
            if map[y][x] == " " and map[y-1][x] != " ":
                try:
                    (map[y-1][x],map[y][x]) = (map[y][x], map[y-1][x])
                except IndexError:
                    pass
            else:
                try:
                    while map[y][x] == " " and map[y-control][x] == " ":
                        control = control + 1
                        if map[y][x] == " " and map[y-control][x] != " ":
                            (map[y-control][x],map[y][x]) = (map[y][x], map[y-control][x])
                except IndexError:
                        pass

def del_row():
    for i in range(0, len(map)):
        try:
            if len(set(map[i])) == 1 and " " in set(map[i]):
                map.remove(map[i])
                del_row()
        except  IndexError:
            pass
    
main_memory_horizantal = []
main_memory_horizantal2 = []
main_memory_vertical = []
main_memory_vertical2 = []
repostory_horizantal =[]
repostory_vertical = []

def bomb1():
    global main_memory_horizantal
    global main_memory_vertical
    global main_memory_horizantal2
    global main_memory_vertical2
    global point_axis
    global point_ordinate
    global repostory_vertical
    global repostory_horizantal
    global first_score
    map.remove([])
    while_check1 = True
    check_memory = [(point_axis, point_ordinate)]
    while while_check1:
        for a in range(0, len(map[point_ordinate])):
            main_memory_horizantal.append((a, point_ordinate))
            main_memory_horizantal2.append((a, point_ordinate))
        for b in range(0, len(map)):
            main_memory_vertical.append((point_axis, b))
            main_memory_vertical2.append((point_axis, b))
        for c in main_memory_vertical:
            if map[c[1]][c[0]] == "X" and c[1] != point_ordinate and c not in check_memory:
                repostory_vertical.append(c)
        for d in main_memory_horizantal:
            if map[d[1]][d[0]] == "X" and d[1] != point_axis and d not in check_memory:
                repostory_horizantal.append(d)
        repostory_horizantal.extend(repostory_vertical)
        repostory_vertical.clear()
        for e in repostory_horizantal:
            try:
                point_axis = e[0]
                point_ordinate = e[1]
                check_memory.append((e[0], e[1]))
            except IndexError:
                while_check1 = False
            break
        try:
            repostory_horizantal.remove(e)
        except Exception:
            while_check1 = False
        main_memory_vertical = []
        main_memory_horizantal  = []
    map.append([])
    main_memory_vertical2.extend(main_memory_horizantal2)
    main_memory_vertical2 = list(set(main_memory_vertical2))
    for i in main_memory_vertical2:
        try:
            score = letters_value[map[i[1]][i[0]]]
            first_score = first_score + score
        except IndexError:
            pass

def bomb2():
    cordinates3 = []
    map.remove([])
    for i in main_memory_vertical2:
        try:
            map[i[1]][i[0]] = " "
        except IndexError:
            pass
    for a in range(0, lenght):
        for b in range(0,len(map)):
            try:
                if map[b][a] != " ":
                    break
                if map[b][a] == " " and b == len(map)-1:
                    for c in range(len(map)):
                        cordinates3.append([a,c])
            except IndexError:
                pass
    cordinates3.sort(reverse=True)
    for d in cordinates3:
        map[d[1]].pop(d[0])
    map.append([])

def bomb_point():
    return first_score


def game_over():
    for a in range(0, len(map)-1):
        for b in range(0, len(map[a])):
            tax = b
            tord = a
            relcordinates = [[tax+1, tord], [tax-1, tord], [tax, tord+1], [tax, tord-1]]
            for i in relcordinates:
                try:
                    assert i[0] >= 0 and i[1] >= 0
                    if (map[i[1]][i[0]] == map[a][b] and map[a][b] != " ") or map[a][b] == "X" :
                        return 
                except AssertionError:
                    pass
                except IndexError:
                    pass  
    try:
        if map[a][b] == "X":
            return True
        elif map[i[1]][i[0]] == map[a][b] and map[a][b] != " ":
            return True
        elif a == len(map)-2 : #if code will be broken please examine here.
            return False
    except IndexError:
        return False
    
   

ctr1 = False
ctr2 = False
while_check2 = True
draw_map()
print("Your score is: 0")
while game_over() != False:
    while while_check2 == True:
        try:
            enter_point()
        except IndexError:
            print("Please enter a valid size!")
            ctr1 = True  
        if ctr1 != True:
                if point == " ":
                    print("Please enter a valid size!")
                    ctr2 = True
        if ctr1 == False and ctr2 == False:
            while_check2 = False
        (ctr1, ctr2) = (False, False)
    while_check2 = True  
    if point == "X":
        bomb1()
        bombpoint = bomb_point()
        bomb2()
        main_memory_vertical2 = []
        swp_columns()
        del_row()
        draw_map()
        print("Your score is:",bombpoint)
        game_over()
        if game_over() == False:
            print("Game Over!")
    else:
        mark_point()
        del_letters()
        swp_columns()
        del_row()
        draw_map()
        print("Your score is:",cal_score())
        game_over()
        if game_over() == False:
            print("Game over!")
    
 


 


        
    






    







 




























