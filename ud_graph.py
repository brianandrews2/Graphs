# Course: CS 261
# Author: Brian Andrews
# Assignment:  6
# Description: Undirected Graph class with methods to build and modify an undirected graph.

from collections import deque


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph
        """
        if v not in self.adj_list.keys():
            self.adj_list[v] = []
        
    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """

        # if u equals v do nothing
        if u == v:
            return

        # if vertices not in graph:
        if u not in self.adj_list.keys():
            self.adj_list[u] = []
        if v not in self.adj_list.keys():
            self.adj_list[v] = []

        # add first edge to u
        if len(self.adj_list[u]) == 0:
            self.adj_list[u] = [v]

        # add additional edge to u if it does not already exist
        else:
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)

        # add same first edge to v
        if len(self.adj_list[u]) == 0:
            self.adj_list[v] = [u]

        # add the same additional edge to v if it does not already exist
        else:
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        # if vertex does not exist
        if u not in self.adj_list.keys():
            return
        if v not in self.adj_list.keys():
            return

        # remove edge from u
        if u in self.adj_list[v]:
            i = 0
            remove = False
            while i < len(self.adj_list[v]) and not remove:
                if self.adj_list[v][i] == u:
                    del(self.adj_list[v][i])
                    remove = True
                i += 1

        # remove same edge from v
        if v in self.adj_list[u]:
            i = 0
            remove = False
            while i < len(self.adj_list[u]) and not remove:
                if self.adj_list[u][i] == v:
                    del(self.adj_list[u][i])
                    remove = True
                i += 1

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        if v not in self.adj_list.keys():
            return

        # remove the edges from other vertices connected to removed vertex
        for vertex in self.adj_list[v]:
            i = 0
            remove = False
            while i < len(self.adj_list[vertex]) and not remove:
                if self.adj_list[vertex][i] == v:
                    del(self.adj_list[vertex][i])
                    remove = True
                i += 1

        # remove the vertex
        del(self.adj_list[v])

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        key_list = []
        for i in self.adj_list.keys():
            key_list.append(i)
        return key_list

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        edge_list = []
        for vertex in self.adj_list:
            for i in self.adj_list[vertex]:
                if vertex < i:                  # we don't want to return both [A, B] and [B, A] duplicates
                    temp_tuple = (vertex, i)
                    edge_list.append(temp_tuple)

        return edge_list

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        # if path length = 1, check if it is in the graph
        if len(path) == 1:
            if path[0] not in self.adj_list.keys():
                return False

        # if path length > 1, check each vertex path
        else:
            i = 0
            while i < len(path) - 1:
                if path[i+1] not in self.adj_list[path[i]]:
                    return False
                i += 1

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """

        # if start vertex does not exist
        if v_start not in self.adj_list.keys():
            return []

        # initialize stack and return list
        stack = []
        visited_vertices = []
        stack.append(v_start)

        # Start the DFS
        end_search = False
        while not end_search:
            vertex = stack.pop()

            # update list of visited vertices
            if vertex not in visited_vertices:
                visited_vertices.append(vertex)
                if vertex == v_end:
                    end_search = True

                # add new vertices to stack
                connected_vertices = self.adj_list[vertex]
                connected_vertices.sort(reverse=True)
                for successor_vertex in connected_vertices:
                    if successor_vertex not in visited_vertices:
                        stack.append(successor_vertex)

            if len(stack) == 0:
                end_search = True

        return visited_vertices

    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        # if start vertex does not exist
        if v_start not in self.adj_list.keys():
            return []

        # initialize queue and return list
        queue = deque()
        visited_vertices = []
        queue.append(v_start)

        # Start the BFS
        end_search = False
        while not end_search:
            vertex = queue.popleft()

            # update list of visited vertices
            if vertex not in visited_vertices:
                visited_vertices.append(vertex)
                if vertex == v_end:
                    end_search = True

                # add new vertices to the queue
                connected_vertices = self.adj_list[vertex]
                connected_vertices.sort()
                for successor_vertex in connected_vertices:
                    if successor_vertex not in visited_vertices:
                        queue.append(successor_vertex)

            if len(queue) == 0:
                end_search = True

        return visited_vertices

    def count_connected_components(self):
        """
        Return number of connected components in the graph
        """
        checked_vertices = []
        number_components = 0
        for vertex in self.adj_list:

            # perform dfs on each un-checked vertex
            if vertex not in checked_vertices:
                connected_graph = self.dfs(vertex)
                number_components += 1

                # updated checked_vertices so we don't complete an entire dfs on each vertex already accounted for
                for checked_vertex in connected_graph:
                    checked_vertices.append(checked_vertex)

        return number_components

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """

        # check each vertex in the graph one at a time for cycle
        for vertex in self.adj_list:

            # initialize stack with vertex successors and put the first vertex in the visited vertices
            stack = []
            visited_vertices = []
            connected_vertices = self.adj_list[vertex]
            connected_vertices.sort(reverse=True)

            visited_vertices.append(vertex)
            for successor_vertex in connected_vertices:
                stack.append(vertex)
                stack.append(successor_vertex)

            # if vertex has successors
            if len(stack) != 0:

                current_cycle = 0   # track how many vertices in current path (min 3 vertices for a cycle)

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

                        # add new successor vertices to stack
                        connected_vertices = self.adj_list[checked_vertex]
                        connected_vertices.sort(reverse=True)
                        for successor_vertex in connected_vertices:
                            if successor_vertex == vertex and current_cycle >= 2:  # cycle must have min 3 vertices
                                return True
                            if successor_vertex not in visited_vertices:
                                stack.append(successor_vertex)

                    # every vertex in this path has been checked and no cycle found.
                    if len(stack) == 0:
                        end_search = True

        return False


if __name__ == '__main__':
    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)

    print("\nPDF - method add_vertex() / add_edge example 2")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)

    g.add_edge('A', 'A')
    print(g)

    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)

    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')

    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))

    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')

    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()

    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())

    print("\nPDF - method has_cycle() example 2")
    print("----------------------------------")
    edges = ['DA', 'DI', 'AD', 'AH', 'BE', 'EB', 'EG', 'EK', 'GE', 'GK', 'GJ', 'KG', 'KE', 'ID', 'HA', 'HJ', 'JG', 'JH']
    g = UndirectedGraph(edges)
    print(g.has_cycle())
