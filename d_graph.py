# Course: CS261 - Data Structures
# Author:  Brian Andrews
# Assignment: 6
# Description:  Directed Graph class with methods to build and modify a directed weighted graph.

from collections import deque


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Add new vertex to the graph.  The first vertex is index 0, and each subsequent addition is index 1, 2...n.
        Returns the number of vertices in the graph.
        """
        self.v_count += 1

        # add a new column to all existing vertices with 0 edges to the new vertex
        for row in self.adj_matrix:
            row.append(0)

        # create a new column for the new vertex with 0 edges to existing vertices
        new_list = []
        for i in range(self.v_count):
            new_list.append(0)  # TEST
        self.adj_matrix.append(new_list)

        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Add weighted edge to the graph.  If vertices do not exist, weight is not positive, or if the src and dst are
        the same then this does nothing.
        """
        # do nothing under these conditions
        if src == dst:
            return
        if weight < 1:
            return
        if src >= len(self.adj_matrix):
            return
        if dst >= len(self.adj_matrix):
            return

        # add edge
        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes an edge between two vertices with provided indices.  If either vertex does not exist or if there is no
        edge between them this method does nothing.
        """
        # do nothing under these conditions
        if src == dst:
            return
        if src >= len(self.adj_matrix) or src < 0:
            return
        if dst >= len(self.adj_matrix) or dst < 0:
            return

        # remove edge
        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Returns a list of vertices of the graph.
        """
        vertex_list = []
        for row in range(len(self.adj_matrix)):
            vertex_list.append(row)

        return vertex_list

    def get_edges(self) -> []:
        """
        Returns a list of edges of the graph.
        """
        edge_list = []
        row_index = 0
        for row in self.adj_matrix:
            for column_index in range(len(row)):
                if row[column_index] != 0:
                    edge_tuple = (row_index, column_index, row[column_index])
                    edge_list.append(edge_tuple)
            row_index += 1

        return edge_list

    def is_valid_path(self, path: []) -> bool:
        """
        Takes a list of vertices and returns True if that path is possible or False otherwise.  An empty path is valid.
        """
        if len(path) == 0:
            return True

        for i in range(len(path)-1):
            curr = path[i]
            next = path[i+1]
            if self.adj_matrix[curr][next] == 0:
                return False

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Performs a depth-first search starting at v_start and returns a list of vertices visited in the search.
        If the start vertex is not in the graph, returns an empty list.  If the v_end end vertex is in the graph,
        the dfs stops there.
        """
        if v_start >= len(self.adj_matrix):
            return []

        # initialize stack and return-list
        stack = []
        visited_vertices = []
        stack.append(v_start)

        # start the DFS
        end_search = False
        while not end_search:
            vertex = stack.pop()

            if vertex not in visited_vertices:

                # update list of visited vertices
                visited_vertices.append(vertex)
                if vertex == v_end:
                    end_search = True

                # populate list of connected vertices from current vertex
                connected_vertices = []
                for column in range(len(self.adj_matrix)):  # for every column in the current row
                    value = self.adj_matrix[vertex][column]
                    if value != 0 and column not in visited_vertices:
                        connected_vertices.append(column)

                # add connected vertices to stack from highest to lowest
                connected_vertices.sort(reverse=True)
                for vertex in connected_vertices:
                    stack.append(vertex)

            if len(stack) == 0:
                end_search = True

        return visited_vertices

    def bfs(self, v_start, v_end=None) -> []:
        """
        Performs a breadth-first search starting at v_start and returns a list of vertices visited in the search.
        If the start vertex is not in the graph, returns an empty list.  If the v_end end vertex is in the graph,
        the bfs stops there.
        """

        if v_start >= len(self.adj_matrix):
            return []

        # initialize queue and return-list
        queue = deque()
        visited_vertices = []
        queue.append(v_start)

        # start the BFS
        end_search = False
        while not end_search:
            vertex = queue.popleft()

            if vertex not in visited_vertices:

                # update list of visited vertices
                visited_vertices.append(vertex)
                if vertex == v_end:
                    end_search = True

                # populate list of connected vertices from current vertex
                connected_vertices = []
                for column in range(len(self.adj_matrix)):
                    value = self.adj_matrix[vertex][column]
                    if value != 0 and column not in visited_vertices:
                        connected_vertices.append(column)

                # add connected vertices to queue from highest to lowest
                connected_vertices.sort()
                for vertex in connected_vertices:
                    queue.append(vertex)

            if len(queue) == 0:
                end_search = True

        return visited_vertices

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise.
        """
        # check each vertex in the graph one at a time for cycle
        for vertex in range(len(self.adj_matrix)):

            # initialize stack with vertex successors and put the first vertex in the visited vertices
            stack = []
            visited_vertices = []
            connected_vertices = []
            for column in range(len(self.adj_matrix)):
                value = self.adj_matrix[vertex][column]
                if value != 0 and column not in visited_vertices:
                    connected_vertices.append(column)
            connected_vertices.sort(reverse=True)

            visited_vertices.append(vertex)
            for successor_vertex in connected_vertices:
                stack.append(vertex)
                stack.append(successor_vertex)

            # if vertex has successors
            if len(stack) != 0:

                current_cycle = 0   # track how many vertices in current path (min 2 vertices for a cycle in digraph)

                # perform dfs on each un-checked vertex; if start vertex is a successor in the dfs return True.
                end_search = False
                while not end_search:
                    checked_vertex = stack.pop()

                    # if we are back at the start, the first path had no cycle, check next successor for cycle
                    if checked_vertex == vertex:
                        current_cycle = 0

                    else:
                        # update list of visited vertices
                        if checked_vertex not in visited_vertices:
                            visited_vertices.append(checked_vertex)
                            current_cycle += 1

                        # check the vertex's successor vertices
                        connected_vertices = []
                        for column in range(len(self.adj_matrix)):
                            value = self.adj_matrix[checked_vertex][column]
                            if value != 0:
                                if column == vertex and current_cycle >= 1:
                                    return True
                                elif column not in visited_vertices:
                                    connected_vertices.append(column)
                        connected_vertices.sort(reverse=True)

                        # add new successor vertices to stack
                        for successor_vertex in connected_vertices:
                            if successor_vertex not in visited_vertices:
                                stack.append(successor_vertex)

                    # every vertex in this path has been checked and no cycle found.
                    if len(stack) == 0:
                        end_search = True

        return False


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7), (5, 2, 20)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)

    # Test remove edges
    g.remove_edge(0, 1)
    print("TEST REMOVE EDGE")
    print(g)

    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')

    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))

    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')

    print("\nPDF - method dfs() and bfs() example 2")
    print("--------------------------------------")
    edges = [(2, 9, 2), (3, 9, 20), (4, 3, 19), (5, 6, 19), (5, 11, 11), (5, 12, 20), (6, 4, 8), (7, 5, 11), (8, 4, 6),
             (9, 0, 11), (9, 3, 7), (10, 5, 13), (11, 7, 15)]
    g = DirectedGraph(edges)
    for start in range(2, 3):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')

    print("\nPDF - remove_edge example 1")
    print("--------------------------------------")
    edges = [(2, 9, 2), (3, 9, 20), (4, 3, 19), (5, 6, 19), (5, 11, 11), (5, 12, 20), (6, 4, 8), (7, 5, 11), (8, 4, 6),
             (9, 0, 11), (9, 3, 7), (10, 5, 13), (11, 7, 15)]
    g = DirectedGraph(edges)
    print(g)
    g.remove_edge(3, -1)
    print(g)

    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)

    print("\nPDF - method has_cycle() example 2")
    print("----------------------------------")
    edges = [(0, 11, 15), (2, 11, 19), (0, 6, 1), (4, 6, 18), (4, 7, 16), (7, 4, 6), (7, 5, 19), (7, 12, 18), (8, 2, 5),
             (8, 6, 4), (9, 5, 5), (9, 6, 15), (10, 7, 2), (12, 2, 20)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)
