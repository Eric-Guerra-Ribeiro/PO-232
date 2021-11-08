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
    maximum_flow = max_flow.ford_fulkerson(graph, "s", "t")
    print("The maximum flow is {}".format(maximum_flow))
    pos = nx.spring_layout(graph)
    max_flow_weights = {(u,v,):d["max_flow"] for u,v,d in graph.edges(data=True)}
    current_flow_weights = {(u,v,):d["current_flow"] for u,v,d in graph.edges(data=True)}
    subax1 = plt.subplot(121)
    nx.draw(graph, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=max_flow_weights)
    subax2 = plt.subplot(122)
    nx.draw(graph, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=current_flow_weights)
    plt.show()
    

A = nx.DiGraph()
A.add_nodes_from(["s", 1, 2, "t"])
A.add_edges_from([("s", 1, {"max_flow" : 1000}), ("s", 2, {"max_flow" : 1000}),
                 (1, "t", {"max_flow" : 1000}), (1, 2, {"max_flow" : 1}),
                 (2, "t", {"max_flow" : 1000})])
B = nx.DiGraph()
B.add_nodes_from(["s", 1, 2, 3, 4, "t"])
B.add_edges_from([("s", 1, {"max_flow" : 10}), ("s", 2, {"max_flow" : 10}), (1, 2, {"max_flow" : 2}),
                 (1, 3, {"max_flow" : 4}), (1, 4, {"max_flow" : 8}), (2, 4, {"max_flow" : 9}),
                 (3, "t", {"max_flow" : 10}), (4, 3, {"max_flow" : 6}), (4, "t", {"max_flow" : 10})])
show_result(A)
show_result(B)

