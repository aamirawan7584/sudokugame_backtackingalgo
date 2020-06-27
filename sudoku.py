main_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def solve(board):
    #print(board)
    find = find_empty(board)
    if find is None:
        return True
    else:
        row, col = find
    for num in range(1,10):
        if valid_placement(board,find,num):
            board[row][col] = num

            if solve(board):
                return True
            
            board[row][col] = 0    
    return False

def valid_placement(board,pos,num):
    """
    this function check that if a number can be placed in particular position or not
    """
    row,col =pos
    #for checking in row
    for j in range(len(board[row])):
        if board[row][j] == num and col!=j:
            return False
    #for checking in column
    for i in range(len(board)):
        if board[i][col] == num and row !=i:
            return False
    #check 3X3 board that if there same number exist then return false
    box_x = col //3 
    box_y = row //3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

print_board(main_board)
solve(main_board)
print("-----------------SOlved---------------------------")
print_board(main_board)    