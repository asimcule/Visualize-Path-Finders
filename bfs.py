from collections import deque

def bfs(G, source, dest):
    dist={}
    prev={}
    queue=deque()
    row=len(G)
    column=len(G[0])
    # initializing distances from source. O(row*col)
    for m in range(row):
        for n in range(column):
            dist[(m,n)]=-1
            prev[(m,n)]=None

    queue.append(source)
    dist[source]=0
    prev[(0,0)]=0
    # run the bfs loop
    while queue:
        i,j=queue.popleft()
        if i==dest[0] and j==dest[1]:
            print(f"Distance of ({dest[0], dest[1]}) from ({source[0], source[1]}: {dist[(i,j)]})")
            cursor=dest
            path=[dest]
            while cursor!=source:
                path.append(prev[cursor])
                cursor=prev[cursor]
            return path[::-1]

        # search for neighbors in all four directions
        if j+1<column and G[i][j+1]:     # node to the right
            if dist[(i, j+1)]==-1:
                dist[(i,j+1)]=dist[(i,j)]+1 # update the distance of the visited node
                prev[(i,j+1)]=(i,j)
                queue.append((i, j+1))
        
        if j-1>=0 and G[i][j-1]:     # node to the left
            if dist[(i, j-1)]==-1:
                dist[(i,j-1)]=dist[(i,j)]+1 # update the distance of the visited node
                prev[(i,j-1)]=(i,j)
                queue.append((i, j-1)) 

        if i+1<row and G[i+1][j]:     # node to the bottom
            if dist[(i+1,j)]==-1:
                dist[(i+1,j)]=dist[(i,j)]+1 # update the distance of the visited node
                prev[(i+1,j)]=(i,j)
                queue.append((i+1,j))

        if i-1>=0 and G[i-1][j]:     # node to the top
            if dist[(i-1, j)]==-1:
                dist[(i-1,j)]=dist[(i,j)]+1 # update the distance of the visited node
                prev[(i-1,j)]=(i,j)
                queue.append((i-1,j))
    return None
    

# G=[[1,1,1,1],
#    [1,1,0,1],
#    [1,0,0,1],
#    [1,1,1,1]]

# source=(0,0)
# dest=(3,3)
# bfs(G,source,dest)