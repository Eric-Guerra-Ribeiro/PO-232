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
    maximum_flow, min_cut = max_flow.ford_fulkerson(graph, "s", "t")
    print("The maximum flow is {}".format(maximum_flow))
    pos = nx.spring_layout(graph)
    flow_weights = {(u, v,):"{}/{}".format(d["flow"], d["capacity"]) for u, v, d in graph.edges(data=True)}
    nx.draw(graph, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=flow_weights)
    plt.show()
    pos = nx.spring_layout(min_cut)
    nx.draw(min_cut, pos=pos, with_labels=True, font_weight='bold')
    if min_cut.number_of_edges() > 0:
        flow_weights = {(u, v,):"{}/{}".format(d["flow"], d["capacity"]) for u, v, d in min_cut.edges(data=True)}
        nx.draw_networkx_edge_labels(min_cut, pos, edge_labels=flow_weights)
    plt.show()
    

A = nx.DiGraph()
A.add_nodes_from(["s", "t", 1])
A.add_edges_from([("s", 1, {"capacity" : 10}), (1, "t", {"capacity" : 1})])
B = nx.DiGraph()
B.add_nodes_from(["s", 1, 2, "t"])
B.add_edges_from([("s", 1, {"capacity" : 1000}), ("s", 2, {"capacity" : 1000}),
                 (1, "t", {"capacity" : 1000}), (1, 2, {"capacity" : 1}),
                 (2, "t", {"capacity" : 1000})])
C = nx.DiGraph()
C.add_nodes_from(["s", 1, 2, 3, 4, "t"])
C.add_edges_from([("s", 1, {"capacity" : 10}), ("s", 2, {"capacity" : 10}), (1, 2, {"capacity" : 2}),
                 (1, 3, {"capacity" : 4}), (1, 4, {"capacity" : 8}), (2, 4, {"capacity" : 9}),
                 (3, "t", {"capacity" : 10}), (4, 3, {"capacity" : 6}), (4, "t", {"capacity" : 10})])
D = nx.DiGraph()
D.add_nodes_from(["s", 0, 1, 2, 3, 4, 5, 6, 7, 8, "t"])
D.add_edges_from([("s", 0, {"capacity" : 7}), ("s", 1, {"capacity" : 2}), ("s", 2, {"capacity" : 1}),
                 (0, 3, {"capacity" : 2}), (0, 4, {"capacity" : 4}), (1, 4, {"capacity" : 5}),
                 (1, 5, {"capacity" : 6}), (2, 3, {"capacity" : 4}), (2, 7, {"capacity" : 8}),
                 (3, 6, {"capacity" : 7}), (3, 7, {"capacity" : 1}), (4, 5, {"capacity" : 2}),
                 (4, 6, {"capacity" : 3}), (4, 8 ,{"capacity" : 3}), (5, 8, {"capacity" : 3}),
                 (6, "t", {"capacity" : 1}), (7, "t", {"capacity" : 3}), (8, "t", {"capacity" : 4})])
show_result(A)
show_result(B)
show_result(C)
show_result(D)
