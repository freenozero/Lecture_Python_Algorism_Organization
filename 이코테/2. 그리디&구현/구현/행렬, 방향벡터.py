#행렬
for i in range(5):
    for j in range(5):
        print('(', i, ',', j,')',end=' ')
    print()

#방향벡터
#동, 북, 서, 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

#서=x -1
#동=x +1
#남=y-1
#북=y+1

x, y= 2, 2

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
