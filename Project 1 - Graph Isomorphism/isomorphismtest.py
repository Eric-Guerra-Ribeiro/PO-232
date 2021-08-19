import networkx as nx

def weisfeiler_lehman(G, compression):
    """
    Performs the Weisfeiler-Lehman Algorithm which colours/labels a graphs vertices canonically.

    :param G: Graph which will be coloured.
    :type G: networkx.classes.graph.Graph.
    :param compression: Dicitionary used for the compressed label.
    :type compression: Dictionary.

    :return: Coloured graph G.
    :rtype: networkx.classes.graph.Graph.
    """
    # Starting conditions - all nodes are label as 1
    for node in G.nodes:
        node["label"] = 1

    labels_changed = True
    # Colours the node iteratively util it converges
    while labels_changed:
        labels_changed = False
        for node in G.nodes:
            node["multiset"] = []
            node["multiset"].append(node["label"])
            for neighbor in G.adj[node]:
                node["multiset"].append(neighbor["label"])
            node["multiset"].sort()
        for node in G.nodes:
            if node["multiset"] in compression:
                new_label = compression[node["multiset"]]
            else:
                new_label = len(compression) + 1
                compression[new_label] = node["multiset"]
            if new_label != node["label"]:
                labels_changed = True
                node["label"] = new_label
    return G



def isomorphism_test(G, H):
    """
    Performs a isomorphic test based on the coloring from the Weisfeiler-Lehman Algorithm.
    Cannot give a conclusive answer if the  graphs are isomorphic.
    If they pass the test, they still could be non-isomorphic.
    However, if it fails, they are definitely non-isomorphic.

    :param G: Graph G which we want to know if is isomorphic to H.
    :type G: networkx.classes.graph.Graph.
    :param H: Graph H which we want to know if is isomorphic to G.
    :type H: networkx.classes.graph.Graph.
    :return: True if the graphs could be isomorphic, False if they definitely are not.
    """
