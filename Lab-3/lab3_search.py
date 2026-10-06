"""BFS, DFS, DLS, IDDFS and UCS on the Lab 3 graph."""
from collections import deque
import heapq

GRAPH = {"A":["B","C"], "B":["D","E"], "C":["F"], "D":[], "E":["G"], "F":[], "G":[]}
WEIGHTS = {"A":[("B",1), ("C",12)], "B":[("D",1), ("E",1)], "C":[("F",1), ("G",12)], "D":[], "E":[("G",1)], "F":[], "G":[]}

def bfs(graph, start, goal):
    q = deque([(start, [start])]); seen = {start}; order=[]
    while q:
        node, path = q.popleft(); order.append(node)
        if node == goal: return path, order
        for nxt in graph.get(node, []):
            if nxt not in seen: seen.add(nxt); q.append((nxt, path+[nxt]))
    return None, order

def dfs(graph, start, goal):
    stack=[(start,[start])]; seen=set(); order=[]
    while stack:
        node,path=stack.pop()
        if node in seen: continue
        seen.add(node); order.append(node)
        if node == goal: return path, order
        for nxt in reversed(graph.get(node, [])): stack.append((nxt,path+[nxt]))
    return None, order

def dls(graph, start, goal, limit):
    order=[]; cutoff=False
    def visit(node, path, depth):
        nonlocal cutoff
        order.append(node)
        if node == goal: return "FOUND", path
        if depth == limit:
            if graph.get(node, []): cutoff=True
            return "CUTOFF", None
        for nxt in graph.get(node, []):
            if nxt in path: continue
            status, result = visit(nxt, path+[nxt], depth+1)
            if status == "FOUND": return status, result
        return "CUTOFF" if cutoff else "FAILURE", None
    status,path=visit(start,[start],0)
    return status,path,order

def iddfs(graph,start,goal,max_depth):
    attempts=[]
    for limit in range(max_depth+1):
        status,path,order=dls(graph,start,goal,limit); attempts.append((limit,status,path,order))
        if status == "FOUND": return path,attempts
    return None,attempts

def ucs(graph,start,goal):
    pq=[(0,start,[start])]; best={start:0}; order=[]
    while pq:
        cost,node,path=heapq.heappop(pq)
        if cost != best.get(node): continue
        order.append(node)
        if node == goal: return path,cost,order
        for nxt,w in graph.get(node,[]):
            nc=cost+w
            if nc < best.get(nxt,float('inf')):
                best[nxt]=nc; heapq.heappush(pq,(nc,nxt,path+[nxt]))
    return None,None,order

def main():
    print("BFS", bfs(GRAPH,"A","G")); print("DFS", dfs(GRAPH,"A","G"))
    for limit in [1,2,3,4]: print("DLS",limit,dls(GRAPH,"A","G",limit))
    path,attempts=iddfs(GRAPH,"A","G",4); print("IDDFS",path,attempts)
    weighted={k:[(n,w) for n,w in v] for k,v in WEIGHTS.items()}
    bpath,border=bfs({k:[n for n,w in v] for k,v in weighted.items()},"A","G")
    print("weighted BFS",bpath,"cost",sum(next(w for n,w in weighted[u] if n==v) for u,v in zip(bpath,bpath[1:])),"order",border)
    print("UCS",ucs(weighted,"A","G"))
if __name__ == "__main__": main()
