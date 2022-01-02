with open("2021/day04-giant-squid/input.txt") as f:
    input = [line.replace("\n", "") for line in f]
    numbers_drawn = [int(i) for i in input[0].split(",")]

def makeBoards(input):
    input = input[2:]

    boards = []
    curr_board = []
    for line in input:
        if line == "":
            boards.append(curr_board)
            curr_board = []
        else: 
            curr_board.append([int(i) for i in line.split()])
    boards.append(curr_board) #edge case of last board

    return boards

def checkBoard(board):
    for row in range(5):
        if sum(board[row]) == -5:
            board.pop(row)
            return True
    for i in range(5):
        col = [row[i] for row in board]
        if sum(col) == -5:
            for row in board:
                row.pop(i)
            return True
    return False

def markBoard(num_called, boards):
    for board in boards:
        for y in range(5):
            for x in range(5):
                if board[y][x] == num_called:
                    board[y][x] = -1
    return boards

def getUnmarked(board):
    unmarked = []
    for row in board:
        for number in row:
            if number != -1:
                unmarked.append(number)

    return unmarked


def playBingo(numbers, boards):
    final_score = 0

    for number in numbers:
        boards = markBoard(number, boards)
        for board in boards:
            if checkBoard(board):
                numbers_left =getUnmarked(board)                    
                final_score += sum(numbers_left)
                final_score *= number
                return final_score

boards = makeBoards(input)
print(playBingo(numbers_drawn, boards))
                