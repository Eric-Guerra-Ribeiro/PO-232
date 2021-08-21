import networkx as nx

def weisfeiler_lehman(G, compression={():1}):
    """
    Performs the Weisfeiler-Lehman Algorithm which colours/labels a graphs vertices canonically.

    :param G: Graph which will be coloured.
    :type G: networkx.classes.graph.Graph.
    :param compression: Dicitionary used for the compressed label.
    :type compression: Dictionary.

    :return: Graph as a multiset (represented by an ordered tuple) of its nodes' labels.
    :rtype: int tuple which size matches the order of G.
    """
    # Starting conditions - all nodes are label as 1
    for node in G.nodes:
        G.nodes[node]["label"] = 1
    old_new_correspondence = {}
    new_old_correspondence = {}
    partition_changed = True
    # Colours the node iteratively util the color partition converges
    while partition_changed:
        partition_changed = False
        for node in G.nodes:
            multiset_list = [G.nodes[node]["label"]]
            for neighbor in G.adj[node]:
                multiset_list.append(G.nodes[neighbor]["label"])
            multiset_list.sort()
            G.nodes[node]["multiset"] = tuple(multiset_list)
        old_new_correspondence.clear()
        new_old_correspondence.clear()
        for node in G.nodes:
            multiset = G.nodes[node]["multiset"]
            old_label = G.nodes[node]["label"]
            if multiset in compression:
                new_label = compression[multiset]
            else:
                new_label = len(compression) + 1
                compression[multiset] = new_label
            if not partition_changed:
                # Checks bijection between old labeling and new labeling
                # If there is a bijection, partitions did not change (algorithm converged)
                if old_label in old_new_correspondence:
                    if old_new_correspondence[old_label] != new_label:
                        partition_changed = True
                else:
                    old_new_correspondence[old_label] = new_label
                if new_label in new_old_correspondence:
                    if new_old_correspondence[new_label] != old_label:
                        partition_changed = True
                else:
                    new_old_correspondence[new_label] = old_label
            G.nodes[node]["label"] = new_label
    # Creates the multiset of all the graph's nodes.
    graph_multiset = []
    for node in G.nodes:
        graph_multiset.append(G.nodes[node]["label"])
    graph_multiset.sort()
    return tuple(graph_multiset)


def isomorphism_test(G, H, print_labeling = False):
    """
    Performs a isomorphic test based on the coloring from the Weisfeiler-Lehman Algorithm.
    Cannot give a conclusive answer if the  graphs are isomorphic.
    If they pass the test, they still could be non-isomorphic.
    However, if it fails, they are definitely non-isomorphic.

    :param G: Graph G which we want to know if is isomorphic to H.
    :type G: networkx.classes.graph.Graph.
    :param H: Graph H which we want to know if is isomorphic to G.
    :type H: networkx.classes.graph.Graph.
    :param print_labeling: if it is to print the Weisfeiler-Lehman Algorithm Labeling.
    :type print_labeling: bool.

    :return: True if the graphs could be isomorphic, False if they definitely are not.
    :rtype: bool
    """
    compression = {():1}
    g_multiset = weisfeiler_lehman(G, compression)
    h_multiset = weisfeiler_lehman(H, compression)
    if print_labeling:
        print("First Graph Labeling: ", g_multiset)
        print("Second Graph Labeling: ", h_multiset)
    return g_multiset == h_multiset
