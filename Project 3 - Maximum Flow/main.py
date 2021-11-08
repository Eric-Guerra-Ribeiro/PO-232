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
    max_flow.ford_fulkerson(graph, "s", "t")
    pos = nx.spring_layout(A)
    max_flow_weights = {(u,v,):d["max_flow"] for u,v,d in A.edges(data=True)}
    current_flow_weights = {(u,v,):d["current_flow"] for u,v,d in A.edges(data=True)}
    subax1 = plt.subplot(121)
    nx.draw(A, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(A, pos, edge_labels=max_flow_weights)
    subax2 = plt.subplot(122)
    nx.draw(A, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(A, pos, edge_labels=current_flow_weights)
    plt.show()
    

A = nx.DiGraph()
A.add_nodes_from(["s", 1, 2, "t"])
A.add_edges_from([("s", 1, {"max_flow" : 1000}), ("s", 2, {"max_flow" : 1000}),
                 (1, "t", {"max_flow" : 1000}), (1, 2, {"max_flow" : 1}),
                 (2, "t", {"max_flow" : 1000})])
show_result(A)
