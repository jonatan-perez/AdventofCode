def get_input(file):
    with open(f"2021/day04-giant-squid/{file}.txt") as f:
        input = [line.replace("\n", "") for line in f]
        numbers_drawn = [int(i) for i in input[0].split(",")]
    return input, numbers_drawn

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
            return True
    for i in range(5):
        col = [row[i] for row in board]
        if sum(col) == -5:
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
        board_won = False
        winning_boards = []
        boards = markBoard(number, boards)
        
        for i in range(len(boards)):
            if checkBoard(boards[i]) and len(boards) > 1:
                board_won = True
                winning_boards.append(i)
            elif checkBoard(boards[i]): 
                numbers_left = getUnmarked(boards[i])                    
                final_score += sum(numbers_left)
                final_score *= number
                return final_score
        if board_won:
            boards_copy = boards
            boards = []
            for i in range(len(boards_copy)):
                if i not in winning_boards:
                    boards.append(boards_copy[i])
def get_answer(file):
    input, numbers_drawn = get_input(file)
    boards = makeBoards(input)
    return playBingo(numbers_drawn, boards)

print(get_answer("input"))