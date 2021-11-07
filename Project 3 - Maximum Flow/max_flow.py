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

    :return max_flow: Maximum flow possible in the graph.
    :rtype max_flow: int
    :return min_cut: Cut that separates the sink and the source with minimum edge flow sum
    :rtype min_cut: networkx.classes.digraph.DiGraph
    """
    pass
    residual_graph = nx.DiGraph(graph)
    for edge in graph.edges:
        residual_graph.add_weighted_edges_from([(edge[1], edge[0], 0)])
    for edge in residual_graph.edges:
        residual_graph.edges[edge[0], edge[1]]["current_flow"] = 0
    augmented_path = bfs(residual_graph)
    max_flow = 0
    while len(augmented_path) != 0:
        # TODO increment flow
        augmented_path = bfs(residual_graph)
    min_cut = nx.DiGraph()
    # TODO find min_cut
    return max_flow, min_cut
