""" Test script for Graph coding problems"""
from Graph import *
import copy

#Create some vertices

v = Vertex('v')
w = Vertex('w')
p = Vertex('p')
q = Vertex('q')


#Create some edges
e1 = Edge(v, w)
e2 = Edge(v, p)
e3 = Edge(p,q)

#Create the graph
g = Graph([v,w,p,q], [e1,e2,e3])
g1 = Graph ([v,w,p], [])
#g2 = copy.deepcopy(g)

#g = Graph([v,w], [e1])

#Create vertices and edges not in the graph
r = Vertex('r')
s = Vertex('s')

e4 = Edge(r,s)
e5 = Edge(v,q)

#Test some methods
#get_edge(e)
g.get_edge(v,w)

print "got e1"

g.get_edge(v,q)

print "\n"
print g
print "\n"

#remove_edge(e)
# g1.remove_edge(e1)
# g1.remove_edge(e2)
# g1.remove_edge(e3)

# print "The graph with removed edge\n"
# print g1


print "Print all the vertices in the graph"

print g.vertices()

print "Print all the edges in the graph"

print g.edges()
