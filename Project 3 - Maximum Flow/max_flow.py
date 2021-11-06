import networkx as nx

def bfs(residual_graph, source, sink):
    """
    Finds an augmented path from the residual graph using breadth first search.
    If no augmented path exists, returns an empty graph.

    :param residual_graph: Residual graph in which an augmented path may be found.
    :type residual_graph: networkx.classes.graph.Graph
    :param source: Source node.
    :type source: any hashable type
    :param sink: Sink node.
    :type sink: any hashable type

    :return: The augmented path that was found or an empty graph, if no such path exists.
    :rtype: networkx.classes.graph.Graph
    """
    pass


def ford_fulkerson(graph, source, sink):
    """
    Finds the maximum flow in graph using the Edmonds-Karp implementation of
    the Ford-Fulkerson Algorithm.

    :param graph: graph in which the maximum flow is calculated
    :type graph: networkx.classes.graph.Graph
    :param source: Source node.
    :type source: any hashable type
    :param sink: Sink node.
    :type sink: any hashable type

    :return maximum_flow: Maximum flow possible in the graph.
    :rtype maximum_flow: int
    :return minimum_cut: Cut that separates the sink and the source with minimum edge flow sum
    :rtype minimum_cut: networkx.classes.graph.Graph
    """
    pass
