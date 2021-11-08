import networkx as nx
import matplotlib.pyplot as plt
import max_flow

# YouTube Video link: 

def show_result(graph):
    """
    Draws the graph with the flow within its edges as well as displaying the maximum flow.

    :param graph: Graph to be drawn along with the flow within its edges.
    :type graph: networkx.classes.digraph.DiGraph
    """
    pass
    

A = nx.DiGraph()
A.add_nodes_from(["s", 1, 2, "t"])
A.add_edges_from([("s", 1, {"max_flow" : 1000}), ("s", 2, {"max_flow" : 1000}),
                 (1, "t", {"max_flow" : 1000}), (1, 2, {"max_flow" : 1}),
                 (2, "t", {"max_flow" : 1000})])
show_result(A)
