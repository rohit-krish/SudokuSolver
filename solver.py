from colorama import Back, Fore, Style

count = 0


def solve(bo):
    global count
    count += 1
    # print(count)

    # using the find_empty() function to get the next empty space(0)
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find  # getting the position of the empty space

    # MAIN PART IS FOLLOWS

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            # check whether the i value is a suted one or not , if true then assign it
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):

    #Check row
    for i in range(len(bo[0])):
        # looping through the row and , [secondCondition]=> we don't need to care about the current position
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #Check inner-box
    # look for some time you'll get it
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

# just printing stuff not that important


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print(Fore.BLUE+"---------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(Fore.LIGHTBLUE_EX+"|", end=" ")
            if j == 8:
                print(Fore.MAGENTA+str(bo[i][j]))
            else:
                print(Fore.MAGENTA+str(bo[i][j])+" ", end="")
    global count
    temp = count
    count = 0
    return temp

# just a simple function to find the empty space


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row,column
    return None
