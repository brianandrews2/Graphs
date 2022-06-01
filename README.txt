# Graphs
Directed and Undirected Graph classes.  The classes each contain methods to create, search, modify, and display the graphs.  Example outputs for each method are displayed below:

# Undirected Graph:
PDF - method add_vertex() / add_edge example 1
----------------------------------------------
GRAPH: {}
GRAPH: {A: [], B: [], C: [], D: [], E: []}
GRAPH: {A: [], B: [], C: [], D: [], E: []}
GRAPH: {
  A: ['B', 'C']
  B: ['A', 'C', 'D']
  C: ['A', 'B', 'D', 'E']
  D: ['B', 'C', 'E']
  E: ['C', 'D']}

PDF - method add_vertex() / add_edge example 2
----------------------------------------------
GRAPH: {}
GRAPH: {A: [], B: [], C: [], D: [], E: []}
GRAPH: {A: [], B: [], C: [], D: [], E: []}
GRAPH: {
  A: ['B', 'C']
  B: ['A', 'C', 'D']
  C: ['A', 'B', 'D', 'E']
  D: ['B', 'C', 'E']
  E: ['C', 'D']}
GRAPH: {
  A: ['B', 'C']
  B: ['A', 'C', 'D']
  C: ['A', 'B', 'D', 'E']
  D: ['B', 'C', 'E']
  E: ['C', 'D']}

PDF - method remove_edge() / remove_vertex example 1
----------------------------------------------------
GRAPH: {
  A: ['C']
  B: ['C', 'D']
  C: ['A', 'B', 'D', 'E']
  D: ['B', 'C', 'E']
  E: ['C', 'D']}
GRAPH: {A: ['C'], B: ['C'], C: ['A', 'B', 'E'], E: ['C']}

PDF - method get_vertices() / get_edges() example 1
---------------------------------------------------
[]
[]
[('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E')]
['A', 'B', 'C', 'D', 'E']

PDF - method is_valid_path() example 1
--------------------------------------
['A', 'B', 'C'] True
['A', 'D', 'E'] False
['E', 'C', 'A', 'B', 'D', 'C', 'B', 'E'] False
['A', 'C', 'D', 'E', 'C', 'B'] True
[] True
['D'] True
['Z'] False

PDF - method dfs() and bfs() example 1
--------------------------------------
A DFS:['A', 'C', 'B', 'D', 'E', 'H'] BFS:['A', 'C', 'E', 'B', 'D', 'H']
B DFS:['B', 'C', 'A', 'E', 'D', 'H'] BFS:['B', 'C', 'D', 'E', 'H', 'A']
C DFS:['C', 'A', 'E', 'B', 'D', 'H'] BFS:['C', 'A', 'B', 'D', 'E', 'H']
D DFS:['D', 'B', 'C', 'A', 'E', 'H'] BFS:['D', 'B', 'C', 'E', 'H', 'A']
E DFS:['E', 'A', 'C', 'B', 'D', 'H'] BFS:['E', 'A', 'B', 'C', 'D', 'H']
G DFS:['G', 'F', 'Q'] BFS:['G', 'F', 'Q']
H DFS:['H', 'B', 'C', 'A', 'E', 'D'] BFS:['H', 'B', 'C', 'D', 'E', 'A']
-----
B-G DFS:['B', 'C', 'A', 'E', 'D', 'H'] BFS:['B', 'C', 'D', 'E', 'H', 'A']
C-E DFS:['C', 'A', 'E'] BFS:['C', 'A', 'B', 'D', 'E']
D-D DFS:['D'] BFS:['D']
E-C DFS:['E', 'A', 'C'] BFS:['E', 'A', 'B', 'C']
G-B DFS:['G', 'F', 'Q'] BFS:['G', 'F', 'Q']
H-A DFS:['H', 'B', 'C', 'A'] BFS:['H', 'B', 'C', 'D', 'E', 'A']

PDF - method count_connected_components() example 1
---------------------------------------------------
1 2 3 4 4 5 5 5 6 6 5 4 3 2 1 1 1 1 1 2 

PDF - method has_cycle() example 1
----------------------------------
add QH     True
remove FG  True
remove GQ  True
remove HQ  True
remove AE  True
remove CA  True
remove EB  True
remove CE  True
remove DE  True
remove BC  False
add EA     False
add EF     False
add GQ     False
add AC     False
add DQ     False
add EG     True
add QH     True
remove CD  True
remove BD  False
remove QG  False
add FG     True
remove GE  False

PDF - method has_cycle() example 2
----------------------------------
True


# Directed Graph
PDF - method add_vertex() / add_edge example 1
----------------------------------------------
EMPTY GRAPH

GRAPH (5 vertices):
   | 0  1  2  3  4
------------------
 0 | 0  0  0  0  0
 1 | 0  0  0  0  0
 2 | 0  0  0  0  0
 3 | 0  0  0  0  0
 4 | 0  0  0  0  0

GRAPH (5 vertices):
   | 0  1  2  3  4
------------------
 0 | 0 10  0  0  0
 1 | 0  0  0  0 15
 2 | 0 23  0  0  0
 3 | 0  5  7  0  0
 4 |12  0  0  3  0

TEST REMOVE EDGE
GRAPH (5 vertices):
   | 0  1  2  3  4
------------------
 0 | 0  0  0  0  0
 1 | 0  0  0  0 15
 2 | 0 23  0  0  0
 3 | 0  5  7  0  0
 4 |12  0  0  3  0


PDF - method get_edges() example 1
----------------------------------
[(0, 1, 10), (1, 4, 15), (2, 1, 23), (3, 1, 5), (3, 2, 7), (4, 0, 12), (4, 3, 3)]
[0, 1, 2, 3, 4]

PDF - method is_valid_path() example 1
--------------------------------------
[0, 1, 4, 3] True
[1, 3, 2, 1] False
[0, 4] False
[4, 0] True
[] True
[2] True

PDF - method dfs() and bfs() example 1
--------------------------------------
0 DFS:[0, 1, 4, 3, 2] BFS:[0, 1, 4, 3, 2]
1 DFS:[1, 4, 0, 3, 2] BFS:[1, 4, 0, 3, 2]
2 DFS:[2, 1, 4, 0, 3] BFS:[2, 1, 4, 0, 3]
3 DFS:[3, 1, 4, 0, 2] BFS:[3, 1, 2, 4, 0]
4 DFS:[4, 0, 1, 3, 2] BFS:[4, 0, 3, 1, 2]

PDF - method dfs() and bfs() example 2
--------------------------------------
2 DFS:[2, 9, 0, 3] BFS:[2, 9, 0, 3]

PDF - remove_edge example 1
--------------------------------------
GRAPH (13 vertices):
   | 0  1  2  3  4  5  6  7  8  9 10 11 12
------------------------------------------
 0 | 0  0  0  0  0  0  0  0  0  0  0  0  0
 1 | 0  0  0  0  0  0  0  0  0  0  0  0  0
 2 | 0  0  0  0  0  0  0  0  0  2  0  0  0
 3 | 0  0  0  0  0  0  0  0  0 20  0  0  0
 4 | 0  0  0 19  0  0  0  0  0  0  0  0  0
 5 | 0  0  0  0  0  0 19  0  0  0  0 11 20
 6 | 0  0  0  0  8  0  0  0  0  0  0  0  0
 7 | 0  0  0  0  0 11  0  0  0  0  0  0  0
 8 | 0  0  0  0  6  0  0  0  0  0  0  0  0
 9 |11  0  0  7  0  0  0  0  0  0  0  0  0
10 | 0  0  0  0  0 13  0  0  0  0  0  0  0
11 | 0  0  0  0  0  0  0 15  0  0  0  0  0
12 | 0  0  0  0  0  0  0  0  0  0  0  0  0

GRAPH (13 vertices):
   | 0  1  2  3  4  5  6  7  8  9 10 11 12
------------------------------------------
 0 | 0  0  0  0  0  0  0  0  0  0  0  0  0
 1 | 0  0  0  0  0  0  0  0  0  0  0  0  0
 2 | 0  0  0  0  0  0  0  0  0  2  0  0  0
 3 | 0  0  0  0  0  0  0  0  0 20  0  0  0
 4 | 0  0  0 19  0  0  0  0  0  0  0  0  0
 5 | 0  0  0  0  0  0 19  0  0  0  0 11 20
 6 | 0  0  0  0  8  0  0  0  0  0  0  0  0
 7 | 0  0  0  0  0 11  0  0  0  0  0  0  0
 8 | 0  0  0  0  6  0  0  0  0  0  0  0  0
 9 |11  0  0  7  0  0  0  0  0  0  0  0  0
10 | 0  0  0  0  0 13  0  0  0  0  0  0  0
11 | 0  0  0  0  0  0  0 15  0  0  0  0  0
12 | 0  0  0  0  0  0  0  0  0  0  0  0  0


PDF - method has_cycle() example 1
----------------------------------
[(0, 1, 10), (1, 4, 15), (2, 1, 23), (3, 2, 7), (4, 0, 12), (4, 3, 3)]
True
[(0, 1, 10), (1, 4, 15), (2, 1, 23), (3, 2, 7), (4, 3, 3)]
True
[(0, 1, 10), (1, 4, 15), (2, 1, 23), (4, 3, 3)]
False
[(0, 1, 10), (1, 4, 15), (2, 1, 23), (4, 3, 1)]
False
[(0, 1, 10), (1, 4, 15), (2, 1, 23), (2, 3, 1), (4, 3, 1)]
False
[(0, 1, 10), (1, 3, 1), (1, 4, 15), (2, 1, 23), (2, 3, 1), (4, 3, 1)]
False
[(0, 1, 10), (1, 3, 1), (1, 4, 15), (2, 1, 23), (2, 3, 1), (4, 0, 1), (4, 3, 1)]
True

 GRAPH (5 vertices):
   | 0  1  2  3  4
------------------
 0 | 0 10  0  0  0
 1 | 0  0  0  1 15
 2 | 0 23  0  1  0
 3 | 0  0  0  0  0
 4 | 1  0  0  1  0


PDF - method has_cycle() example 2
----------------------------------
[(0, 6, 1), (0, 11, 15), (2, 11, 19), (4, 6, 18), (4, 7, 16), (7, 4, 6), (7, 5, 19), (7, 12, 18), (8, 2, 5), (8, 6, 4), (9, 5, 5), (9, 6, 15), (10, 7, 2), (12, 2, 20)]
True

 GRAPH (13 vertices):
   | 0  1  2  3  4  5  6  7  8  9 10 11 12
------------------------------------------
 0 | 0  0  0  0  0  0  1  0  0  0  0 15  0
 1 | 0  0  0  0  0  0  0  0  0  0  0  0  0
 2 | 0  0  0  0  0  0  0  0  0  0  0 19  0
 3 | 0  0  0  0  0  0  0  0  0  0  0  0  0
 4 | 0  0  0  0  0  0 18 16  0  0  0  0  0
 5 | 0  0  0  0  0  0  0  0  0  0  0  0  0
 6 | 0  0  0  0  0  0  0  0  0  0  0  0  0
 7 | 0  0  0  0  6 19  0  0  0  0  0  0 18
 8 | 0  0  5  0  0  0  4  0  0  0  0  0  0
 9 | 0  0  0  0  0  5 15  0  0  0  0  0  0
10 | 0  0  0  0  0  0  0  2  0  0  0  0  0
11 | 0  0  0  0  0  0  0  0  0  0  0  0  0
12 | 0  0 20  0  0  0  0  0  0  0  0  0  0
