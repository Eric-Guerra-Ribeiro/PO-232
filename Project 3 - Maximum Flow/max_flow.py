import networkx as nx
import collections
from math import inf


def bfs(residual_graph, source, sink):
    """
    Finds an augmenting path from the residual graph using breadth first search.
    If no augmenting path exists, returns an empty graph.

    :param residual_graph: Residual graph in which an augmenting path may be found.
    :type residual_graph: networkx.classes.digraph.DiGraph
    :param source: Source node.
    :type source: any hashable type
    :param sink: Sink node.
    :type sink: any hashable type

    :return: The augmenting path that was found or an empty list, if no such path exists.
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
        edge = residual_graph.edges[source, node]
        if edge["max_flow"] - edge["current_flow"] > 0:
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
            path.reverse()
            break
        for adj_node in residual_graph.successors(node):
            if not visited[adj_node]:
                edge = residual_graph.edges[node, adj_node]
                if edge["max_flow"] - edge["current_flow"] > 0:
                    visited[adj_node] = True
                    parent[adj_node] = node
                    queue.append(adj_node)
    return path


def increment_flow(residual_graph, augmenting_path):
    """
    Increments the flow along the augmenting path and returns the bottleneck value.

    :param residual_graph: Residual graph in which an augmenting path is.
    :type residual_graph: networkx.classes.digraph.DiGraph
    :param augmenting_path: augmenting path in which the flow will be incremented.
    :type augmenting_path: list

    :return: Bottleneck flow value in augmenting path.
    :rtype: int
    """
    bottleneck_flow = inf
    for i in range(len(augmenting_path) - 1):
        edge = residual_graph.edges[augmenting_path[i], augmenting_path[i+1]]
        bottleneck_flow = min(edge["max_flow"] - 
                              edge["current_flow"], bottleneck_flow)
    for i in range(len(augmenting_path) - 1):
        edge = residual_graph.edges[augmenting_path[i], augmenting_path[i+1]]
        reverse_edge = residual_graph.edges[augmenting_path[i+1], augmenting_path[i]]
        if edge["current_flow"] < 0:
            sign = -1
        else:
            sign = 1
        edge["current_flow"] += sign*bottleneck_flow
        reverse_edge["current_flow"] -= sign*bottleneck_flow
    return bottleneck_flow


def find_min_cut(graph, source):
    """
    Find the minimum cut of the flow network.

    :param graph: Graph in which the flow happens.
    :type graph: networkx.classes.digraph.DiGraph
    :param source: Source node.
    :type source: any hashable type

    :return: Minimum cut of the flow network.
    :rtype: networkx.classes.digraph.DiGraph
    """
    min_cut = nx.DiGraph()
    min_cut.add_node(source)
    queue = collections.deque()
    for node in graph.successors(source):
        edge = graph.edges[source, node]
        if edge["max_flow"] - edge["current_flow"] > 0:
            min_cut.add_node(node)
            min_cut.add_edges_from([(source, node, {"max_flow" : edge["max_flow"], "current_flow" : edge["current_flow"]})])
            queue.append(node)
    while queue:
        node = queue.popleft()
        for adj_node in graph.successors(node):
            edge = graph.edges[node, adj_node]
            if edge["max_flow"] - edge["current_flow"] > 0:
                min_cut.add_node(adj_node)
                min_cut.add_edges_from([(node, adj_node, {"max_flow" : edge["max_flow"], "current_flow" : edge["current_flow"]})])
                queue.append(adj_node)
    return min_cut


def update_flow(graph, residual_graph):
    """
    Adds to the original graph the flow which correspond to the maximum total flow.

    :param graph: digraph in which the maximum flow is calculated.
    :type graph: networkx.classes.digraph.DiGraph
    :param residual_graph: Residual graph with the flow values.
    :type residual_graph: networkx.classes.digraph.DiGraph
    """
    for edge in graph.edges:
        flow = residual_graph.edges[edge[0], edge[1]]["current_flow"]
        graph.edges[edge[0], edge[1]]["current_flow"] = flow


def ford_fulkerson(graph, source, sink):
    """
    Finds the maximum flow in graph using the Edmonds-Karp implementation of
    the Ford-Fulkerson Algorithm.

    :param graph: digraph in which the maximum flow is calculated.
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
        residual_graph.add_edges_from([(edge[1], edge[0], {"max_flow":0})])
    for edge in residual_graph.edges:
        residual_graph.edges[edge[0], edge[1]]["current_flow"] = 0
    augmenting_path = bfs(residual_graph, source, sink)
    max_flow = 0
    while augmenting_path:
        max_flow += increment_flow(residual_graph, augmenting_path)
        augmenting_path = bfs(residual_graph, source, sink)
    update_flow(graph, residual_graph)
    min_cut = find_min_cut(graph, source)
    return max_flow, min_cut
