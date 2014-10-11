""" Testing script for Graph.py"""

from Graph import Vertex
from Graph import Edge
from Graph import Graph

from  GraphWorld import *
import string

# create n Vertices
n = 4
labels = string.ascii_lowercase + string.ascii_uppercase
vs = [Vertex(c) for c in labels[:n]]

# create a graph and a layout
g = Graph(vs)
g.add_regular_edges(3)
layout = CircleLayout(g)

# draw the graph
gw = GraphWorld()
gw.show_graph(g, layout)
gw.mainloop()



