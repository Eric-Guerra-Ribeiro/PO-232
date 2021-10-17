import networkx as nx
import random
import copy
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


def jarnik_prim_recursive(graph, trees, tree_index, cost, priority_queue):
    """
    Performs the Jarník-Prim Algorithm which finds all the minimum spanning trees, may have repeats.

    :param graph: Graph which the tree spans.
    :type graph: networkx.classes.graph.Graph.

    :return trees: List with all the minimum spanning trees, may have repeats.
    :rtype trees: networkx.classes.graph.Graph list
    :return cost: sum of the weight of all edges
    :rtype cost: float/int
    """
    while priority_queue:
        node_info = heapq.heappop(priority_queue)
        edge_weight = node_info[0]
        parent = node_info[1]
        node = node_info[2]
        if node in trees[tree_index]:
            continue
        if priority_queue and priority_queue[0][0] == edge_weight and priority_queue[0][2] not in trees[tree_index]:
            popped = []
            aux_priority_queue = copy.deepcopy(priority_queue)
            while aux_priority_queue and aux_priority_queue[0][0] == edge_weight:
                popped.append(heapq.heappop(aux_priority_queue))
            for next_node_info in popped:
                if next_node_info[2] in trees[tree_index]:
                    continue
                trees.append(copy.deepcopy(trees[tree_index]))
                next_tree_index = len(trees) - 1
                next_priority_queue = copy.deepcopy(priority_queue)
                next_edge_weight = next_node_info[0]
                next_parent = next_node_info[1]
                next_node = next_node_info[2]
                trees[next_tree_index].add_node(next_node)
                trees[next_tree_index].add_weighted_edges_from([(next_parent, next_node, next_edge_weight)])
                for son in graph.adj[next_node]:
                    if son in trees[next_tree_index].nodes:
                        continue
                    heapq.heappush(next_priority_queue, (graph.edges[next_node, son]["weight"], next_node, son))
                heapq.heappush(next_priority_queue, (edge_weight, parent, node))
                jarnik_prim_recursive(graph, trees, next_tree_index, cost+edge_weight, next_priority_queue)
        trees[tree_index].add_node(node)
        trees[tree_index].add_weighted_edges_from([(parent, node, edge_weight)])
        cost += edge_weight
        for son in graph.adj[node]:
            if son in trees[tree_index].nodes:
                continue
            heapq.heappush(priority_queue, (graph.edges[node, son]["weight"], node, son))
    return trees, cost


def jarnik_prim_all(graph):
    """
    Intializes the Jarník-Prim Algorithm to find all the minimum spanning trees, may have repeats.

    :param graph: Graph which the tree spans.
    :type graph: networkx.classes.graph.Graph.

    :return trees: List with all the minimum spanning trees, may have repeats.
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
    trees, cost = jarnik_prim_recursive(graph, trees, 0, cost, priority_queue)
    return trees, cost
