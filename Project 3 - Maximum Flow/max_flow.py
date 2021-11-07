import networkx as nx
import collections

def bfs(residual_graph, source, sink):
    """
    Finds an augmented path from the residual graph using breadth first search.
    If no augmented path exists, returns an empty graph.

    :param residual_graph: Residual graph in which an augmented path may be found.
    :type residual_graph: networkx.classes.digraph.DiGraph
    :param source: Source node.
    :type source: any hashable type
    :param sink: Sink node.
    :type sink: any hashable type

    :return: The augmented path that was found or an empty list, if no such path exists.
    :rtype: list
    """
    visited = {}
    parent = {}
    for node in residual_graph:
        visited[node] = False
        parent[node] = None
    queue = collections.deque()
    path = []
    visited[source] = True
    for node in residual_graph.successors(source):
        visited[node] = True
        parent[node] = source
        queue.append(node)
    while queue:
        node = queue.popleft()
        if node == sink:
            path.append(node)
            parent_node = parent[node]
            while parent_node != None:
                path.append(parent_node)
                parent_node = parent[parent_node]
            path = path.reverse()
            break
        for adj_node in residual_graph.successors(node):
            if not visited[adj_node]:
                edge = residual_graph[node, adj_node]
                if edge["max_flow"] - edge["current_flow"] > 0: 
                    visited[adj_node] = True
                    parent[adj_node] = node
                    queue.append(adj_node)
    return path


def ford_fulkerson(graph, source, sink):
    """
    Finds the maximum flow in graph using the Edmonds-Karp implementation of
    the Ford-Fulkerson Algorithm.

    :param graph: digraph in which the maximum flow is calculated
    :type graph: networkx.classes.digraph.DiGraph
    :param source: Source node.
    :type source: any hashable type
    :param sink: Sink node.
    :type sink: any hashable type

    :return maximum_flow: Maximum flow possible in the graph.
    :rtype maximum_flow: int
    :return minimum_cut: Cut that separates the sink and the source with minimum edge flow sum
    :rtype minimum_cut: networkx.classes.digraph.DiGraph
    """
    pass
