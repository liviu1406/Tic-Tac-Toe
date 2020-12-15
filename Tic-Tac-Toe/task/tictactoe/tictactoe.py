# write your code here
def grid():
    print(f'''
---------
| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |
| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |
| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |
---------''')


def check(i, grid):
    for y in range(0, 3):
        if grid[y][0] == grid[y][1] == grid[y][2] == i:
            return True
        elif grid[0][y] == grid[1][y] == grid[2][y] == i:
            return True
        elif grid[0][0] == grid[1][1] == grid[2][2] == i:
            return True
        elif grid[0][2] == grid[1][1] == grid[2][0] == i:
            return True


matrix = []
ls = []
for i in range(0, 8, 3):
    matrix.append([' ', ' ', ' '])


def engine():
    counter = 1
    mark = 'X'
    while True:
        if counter % 2 != 0:
            mark = 'X'
        else:
            mark = 'O'
        try:
            x, y = input('Enter the coordinates: ').split(' ')
            x = int(x)
            y = int(y)
            if y >= 4 or y <= 0:
                print('Coordinates should be from 1 to 3!')
                continue
            if matrix[3 - y][x - 1] == ' ':
                matrix[3 - y][x - 1] = mark
                ls.append(mark)
                counter += 1
                continue
            else:
                print('This cell is occupied! Choose another one!')
                continue
        except ValueError:
            print('You should enter numbers!')
            continue
        except IndexError:
            print('Coordinates should be from 1 to 3!')
            continue
        finally:
            grid()
            if check(mark, matrix):
                grid()
                print(f'{mark} wins')
                exit()
            elif any(' ') in matrix or len(ls) == 9:
                print('Draw')
                exit()


def play():
    grid()
    engine()


play()
