

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #상하좌우 대각대각대각대각
    dr = [-1,1,0,0,-1,-1,1,1]
    dc = [0,0,-1,1,-1,1,-1,1]
    lst = []
    for row in range(N):
        for col in range(N):
            cnt = 0
            cp = arr[row][col] #비교 기준이 되는곳
            for d in range(8):   #상하좌우 그리고 네방향의 대각선을 비교할 수 있도록 한다.
                newr = row +dr[d]
                newc = col +dc[d]
                if 0 <= newr < N and 0 <= newc < N: #비교하는 곳의 인덱스가 유효인덱스인지 검사한다.
                    if cp > arr[newr][newc]: #기준이 되는 곳의 높이가 비교하는곳보다 높으면
                        cnt += 1 #cnt를 1증가시킨다
            if cnt == 8: 
                lst.append(cp) #주변 8영역보다 높은 봉우리는 리스트에 넣는다
    if len(lst) == 1 or len(lst) == 0: #봉우리가 1개이거나 없으면 -1을 반환한다
        ans = -1
    else:
        mmax = max(lst)
        mmin = min(lst)
        ans = mmax - mmin  #가장 높은 곳의 높이에서 가장 낮은곳 높이를 뺀다
    # print(f'#{tc} {ans}')
    # print(f'#{tc}',end=' ')
    # print(f'{ans}')

    #     mmax = 0
    #     mmin = 75465
    #     for s in lst:
    #         if s > mmax :
    #             mmax = s
    #     for s in lst:
    #         if s < mmin:
    #             mmin = s
    #     ans = mmax - mmin
    print(f'#{tc} {ans}')

