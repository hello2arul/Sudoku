


def solve(board):
    row, col = find_empty(board)
    if row is None:
        return True
    
    for num in range(1, 10):
        if is_valid_state(board, row, col):
            board[row][col] = num
            
            if solve(board):
                return True

            board[row][col] = False

    return False


def is_valid_state(board, row, col, num):
    board[row][col] = 0
    for idx in range(len(board)):
        if board[row][idx] == num or board[idx][col] == num:
            return False

    box_x, box_y = (row // 3) * 3, (col // 3) * 3

    #print(box_x, box_y)

    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if board[i][j] == num:
                return False
    print("true")
    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)

    return None