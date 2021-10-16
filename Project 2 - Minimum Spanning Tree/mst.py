import networkx as nx
import random
from numpy import inf
import heapq

def jarnik_prim_simple(graph):
    """
    Performs the Jarník-Prim Algorithm which finds a minimum spanning trees.

    :param graph: Graph which the tree spans.
    :type graph: networkx.classes.graph.Graph.

    :return trees: List with a minimum spanning trees.
    :rtype trees: networkx.classes.graph.Graph list
    :return cost: sum of the weight of all edges
    :rtype cost: float/int
    """
    trees = [nx.Graph()]
    cost = 0
    root = random.choice(list(graph.nodes))
    trees[0].add_node(root)
    priority_queue = []
    heapq.heapify(priority_queue)
    for node in graph.adj[root]:
        if node in trees[0].nodes:
            continue
        heapq.heappush(priority_queue, (graph.edges[root, node]["weight"], root, node))
    while priority_queue:
        node_info = heapq.heappop(priority_queue)
        edge_weight = node_info[0]
        parent = node_info[1]
        node = node_info[2]
        if node in trees[0]:
            continue
        trees[0].add_node(node)
        trees[0].add_weighted_edges_from([(parent, node, edge_weight)])
        cost += edge_weight
        for son in graph.adj[node]:
            if son in trees[0].nodes:
                continue
            heapq.heappush(priority_queue, (graph.edges[node, son]["weight"], node, son))
    return trees, cost
