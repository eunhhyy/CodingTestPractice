def solution(n):
    def is_safe(row, col):
        # 같은 열에 퀸이 있는지 확인
        for i in range(row):
            if board[i] == col:
                return False
            # 대각선 상에 퀸이 있는지 확인
            if abs(board[i] - col) == row - i:
                return False
        return True

    def place_queen(row):
        if row == n:
            # 모든 퀸을 배치했으면 해의 개수 증가
            nonlocal count
            count += 1
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                place_queen(row + 1)
                # 백트래킹
                board[row] = -1

    board = [-1] * n  # 각 행에 퀸의 위치를 저장
    count = 0  # 해의 개수
    place_queen(0)
    return count