"""A* versus UCS with heuristic audit and a deliberate overestimate."""
import heapq
GRAPH={"S":[("A",1),("B",4)],"A":[("C",2)],"B":[("G",5)],"C":[("G",3)],"G":[]}
H={"S":5,"A":4,"B":4,"C":2,"G":0}
TRUE_REMAINING={"S":6,"A":5,"B":5,"C":3,"G":0}

def search(graph,h,start,goal):
    pq=[(h[start],0,start,[start])]; best={start:0}; processed=[]; expanded=[]
    while pq:
        f,g,node,path=heapq.heappop(pq)
        if g != best.get(node): continue
        processed.append((node,g,h[node],f))
        if node == goal: return g,path,processed,expanded
        expanded.append(node)
        for nxt,w in graph.get(node,[]):
            ng=g+w
            if ng < best.get(nxt,float('inf')):
                best[nxt]=ng; heapq.heappush(pq,(ng+h[nxt],ng,nxt,path+[nxt]))
    return None,None,processed,expanded

def audit(h):
    admissible=all(h[n] <= TRUE_REMAINING[n] for n in h)
    consistent=all(h[u] <= w+h[v] for u,edges in GRAPH.items() for v,w in edges)
    return admissible,consistent

def cost(graph,path): return sum(next(w for n,w in graph[u] if n==v) for u,v in zip(path,path[1:]))

def main():
    print("heuristic audit",audit(H))
    astar=search(GRAPH,H,"S","G"); ucs=search(GRAPH,{n:0 for n in H},"S","G")
    print("A*",astar,"independent_cost",cost(GRAPH,astar[1]))
    print("UCS",ucs,"independent_cost",cost(GRAPH,ucs[1]))
    bad=dict(H); bad["C"]=10
    print("overestimate h(C)=10",search(GRAPH,bad,"S","G"))
if __name__ == "__main__": main()
