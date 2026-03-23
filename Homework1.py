def hanoi_plus(n, x, y, z):
    if n == 1:
        print(f'{x}->{y}')
        print(f'{y}->{z}')
        return 
    hanoi_plus(n-1, x, y, z)
    print(f'{x}->{y}')
    hanoi_plus(n-1, z, y, x)
    print(f'{y}->{z}')
    hanoi_plus(n-1, x, y, z)

def circle(n):
    lst = list(range(1, n + 1))
    count = 1
    index = 0
    while len(lst) > 1:
        if count % 2 == 0:
            lst.pop(index)
            count = 1
        else:
            count += 1
            index = (index + 1) % len(lst)
    return lst[0]

def T(n):
    if n==1:
        return 1
    if n>=1:
        if n%2==0:
            return 2*T(n/2)-1
        else:
            return 2*T((n-1)/2)+1

def T1(n):
    m=0
    while 2**(m+1)<=n:
        m+=1
    l=n-2**m
    return 2*l+1

def grid_cover(k: int, i: int, j: int) -> list[list[int]]:
    board = [[0] * 2**k for i in range(2**k)]
    black_i = i - 1
    black_j = j - 1

    def cover(x, y, k, fake_i, fake_j):

        half = 2 ** (k - 1)

        if k == 0:
            return

        if fake_i < half and fake_j < half:
            cover(x, y, k - 1, fake_i, fake_j)
            cover(x, y + half, k - 1, half - 1, 0)
            cover(x + half, y, k - 1, 0, half - 1)
            cover(x + half, y + half, k - 1, 0, 0)

            board[x + half - 1][y + half] = 4
            board[x + half][y + half - 1] = 4
            board[x + half][y + half] = 4

        elif fake_i < half and fake_j >= half:
            cover(x, y + half, k - 1, fake_i, fake_j - half)
            cover(x, y, k - 1, half - 1, half - 1)
            cover(x + half, y, k - 1, 0, half - 1)
            cover(x + half, y + half, k - 1, 0, 0)

            board[x + half - 1][y + half - 1] = 3
            board[x + half][y + half - 1] = 3
            board[x + half][y + half] = 3

        elif fake_i >= half and fake_j < half:
            cover(x + half, y, k - 1, fake_i - half, fake_j)
            cover(x, y, k - 1, half - 1, half - 1)
            cover(x, y + half, k - 1, half - 1, 0)
            cover(x + half, y + half, k - 1, 0, 0)

            board[x + half - 1][y + half - 1] = 2
            board[x + half - 1][y + half] = 2
            board[x + half][y + half] = 2

        else:
            cover(x + half, y + half, k - 1, fake_i - half, fake_j - half)
            cover(x, y, k - 1, half - 1, half - 1)
            cover(x + half, y, k - 1, 0, half - 1)
            cover(x, y + half, k - 1, half - 1, 0)

            board[x + half - 1][y + half - 1] = 1
            board[x + half - 1][y + half] = 1
            board[x + half][y + half - 1] = 1

    board[black_i][black_j] = 0
    cover(0, 0, k, black_i, black_j)
    
    print("[")
    for i, row in enumerate(board):
        if i == len(board) - 1:
            print(f"  {row}")
        else:
            print(f"  {row},")
    print("]")
    
    return board
