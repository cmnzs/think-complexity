""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""
import copy
import logging

logging.basicConfig(level=logging.DEBUG)

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def __deepcopy__(self, memodict={}):
        """Defines deepcopy behaviour for the Graph object"""
        return Graph(Vertices(self), Edges(self))

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds an edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v, w):
        """Retrieves the edge connecting two vertices.

        If there is no edge connecting the vertices, the function returns None.
        """
        try:
            e = self[v][w]
            return e
        except KeyError:
            return None
        
    def remove_edge(self, e):
        """Takes an edge and removes all references to it in the graph.

        If the edge does not exist, the function returns None."""
        v,w = e
        del self[v][w]
        del self[w][v]

    def vertices(self):
        """Returns a list of the vertices in the graph"""
        return self.keys()

    def edges(self):
        """Returns a list of the edges in the graph"""
        vs = self.vertices()
        a = []

        #Should be a better way to do this..

        for v in vs:
            for w in vs:
                a.append(self.get_edge(v,w))
        return [x for x in list(set(a)) if x is not None]

    def out_vertices(self,v):
        """Takes a Vertex and returns a list of the adjacent vertices"""
        return self[v].keys()

    def out_edges(self, v):
        """Takes a Vertex and returns a list of the connected edges"""
        return self[v].values()

    def add_all_edges(self):
        """ Make a complete graph from an edgeless graph: add edges between all pairs of vertices"""

        #Could find all pairs of vertices using itertools.combinations trick
        #Going to do it manually
        vs = self.vertices()

        for i in range(len(vs)):
            for j in range(len(vs)):
                if i != j:
                    self.add_edge(Edge(vs[i],vs[j]))

    def add_regular_edges(self, k):
        """Add edges to an edgeless graph such that every node has degree k"""

        vs = self.vertices()
        n = len(vs)

        #Cannot construct a graph if degree is greater than number of nodes
        if k >= n:
            raise ValueError("Not enough Vertices")

        #Construction is different based on whether k is odd or even
        if is_odd(k):
            if is_odd(n):
                raise ValueError("Can't have odd k and odd length")
            self.add_regular_even(k-1)
            self.add_regular_odd()
        else:
            self.add_regular_even(k)
        

    def add_regular_even(self,k):
        """Add edges to the graph is k is even"""
        vs = self.vertices()
        dup = vs * 2
        
        for i, v in enumerate(vs):
            for j in range(1,k/2+1):
                w = dup[i+j]
                self.add_edge(Edge(v, w))

    def add_regular_odd(self):
        """Add edge to the graph if k is odd"""
        vs = self.vertices()
        n = len(vs)
        dup = vs * 2

        for i in range(n/2):
            v = dup[i]
            w = dup[i+n/2]
            self.add_edge(Edge(v, w))

def is_odd(n):
    return n%2;

def main(script, *args):
    v = Vertex('v')
    
    w = Vertex('w')
    
    p = Vertex('p')
    
    q = Vertex('q')
    
    e = Edge(v, w)
    
    g = Graph([v,w,p,q], [])
    
    g.add_regular_edges(2)
    print g


if __name__ == '__main__':
    import sys
    main(*sys.argv)
