import string
import numpy as np

from GraphWorld import *
from Graph import Edge

import Queue

class RandomGraph(Graph):

    def __init__(self, vs=[]):
        super(RandomGraph,self).__init__(vs,[])
    
    def add_random_edges(self,p):
        """prob p, start with edgeless graph, add edges at random 
         so that the probability is p that there is an edge 
         between any two nodes."""
        vs = self.vertices()
        n = len(vs)

        for i in range(n):
            for j in range(i,n):
                if (i!=j and np.random.binomial(1,p)==1):
                    self.add_edge(Edge(vs[i],vs[j]))

    def is_connected(self):
        """Uses a bread-first search to determine whether a graph is fully connected"""
        vs = self.vertices()
        q = Queue.Queue()
        count = 0

        visited = set()

        #Should this be random initial vertex?
        q.put(vs[0])

        while not q.empty():
            v = q.get(block = False)
            visited.add(v)
            #self[v]['mark'] = True
            con_vs = self.out_vertices(v)
            
            for i,nv in enumerate(con_vs):
                if nv in visited:
                    pass
                else:
                    q.put(nv, block=False)

        if len(visited) < len(vs):
            return False
        else:
            return True




def test_np(n,p,n_test=1000):
    float(n_test)
    ts = [gen_graph(n,p).is_connected() for x in range(n_test)]
    return float(sum(ts))/n_test


def gen_graph(n,p):
    g = RandomGraph(create_labels(int(n)))  
    g.add_random_edges(float(p))
    return g

def create_labels(n):
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    return vs

def draw_graph(g):
    
    layout = CircleLayout(g)
    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()

def main(script, n='5', p='0.5',*args):

    ns = range(10,1001,100)
    ps = np.arange(0,1,0.1)
    print "using range of values: " + str(ps)
    print "using range of ns" + str(ns) 
    
    for nn in ns:
        results = [test_np(nn,pp,10) for pp in ps]
        print str(results)
    #results = dict((nn,dict((pp,test_np(nn,pp,10)) for nn in ns for pp in ps)
    #results = {nn:{pp:test_np(nn,pp,10)} for nn in ns for pp in ps}
    
    # g = RandomGraph(create_labels(int(n)))  
    # g.add_random_edges(float(p))   

    # # print "Is graph connected? " + str(g.is_connected())

    # draw_graph(g)


if __name__ == '__main__':
    import sys
    main(*sys.argv)

