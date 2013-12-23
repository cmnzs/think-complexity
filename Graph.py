""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

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
        return list(set(a))[1:]

    def out_vertices(self,v):
        """Takes a Vertex and returns a list of the adjacent vertices"""
        self[v].keys()

    def out_edges(self, v):
        """Takes a Vertex and returns a list of the connected edges"""
        return self[v].values()

    def add_all_edges(self):
        """ Make a complete graph from an edgeless graph: add edges between all pairs of vertices"""

        #Could find all pairs of vertices using combs from itertools
        #Going to do it manually
        vs = self.vertices()

        for i in range(len(vs)):
            for j in range(len(vs)):
                if i != j:
                    self.add_edge(Edge(vs[i],vs[j]))





def main(script, *args):
    v = Vertex('v')
    print v
    w = Vertex('w')
    print w
    e = Edge(v, w)
    print e
    g = Graph([v,w], [e])
    print g


if __name__ == '__main__':
    import sys
    main(*sys.argv)
