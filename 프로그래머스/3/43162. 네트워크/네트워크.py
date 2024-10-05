def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for k in range(n):
            if computers[node][k] == 1 and visited[k] == False:
                dfs(k)
                
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt+=1
    return cnt