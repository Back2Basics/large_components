import networkx as nx
import itertools as it

class NodeGraph(object):
    """ Graph is a networkx graph
    and connected_nodes is how many 
    connected nodes are in the graph"""
    def __init__(self, graph, connected_nodes):
        self.graph = graph
        if connected_nodes:
            self.connected_nodes=connected_nodes        
        else:
            self.connected_nodes=3

    def get_largest_connected_component():
        raise NotImplementedError

    def get_edges(self):
        """ a filter for edges
        returns an edge where the number of triangles could be a part 
        of a completely connected graph of size "connected_nodes"
        """
        connected_nodes= self.connected_nodes-2
        for x,y in self.graph.edges():
            if nx.triangles(self.graph,y)>=connected_nodes \
                and nx.triangles(self.graph,x)>=connected_nodes:
                [x,y]=sorted([y,x])
                yield x,y

    def len_node(x,node_num):
        node_list = set([y for x in triad for y in x])
        if len(node_list)==connected_nodes:
            output[tuple(node_list)]=1
        
    def flat_map(f, items):
            return it.chain.from_iterable(it.imap(f, items))
    
    def my_map(self):
        output = []
        for list_of_edges in it.combinations(self.get_edges(),self.connected_nodes):
            for x,y in list_of_edges:
                output.append(x)
                output.append(y)
            
        yield sorted(list(set(output)))        
        del output

    def get_nodes_of_connected_graph(self):
        raise NotImplemented
       #keep the state of the graph connections with a counter object so you cna count down the edge counts
    #    for triad in it.combinations(get_edges(graph),connected_nodes):
    #        it.ifilter(,it.combinations(get_edges(graph, connected_nodes)))
    #        node_list = set([y for x in triad for y in x])
    #        if len(node_list)==connected_nodes:
    #            output[tuple(node_list)]=1
    #    for x in output.keys():
    #        yield x
        #    triangle_node_list=[set.update(it.chain(*x)) for x in ]

if __name__=="__main__":
    pass    
#    G = nx.erdos_renyi_graph(10,.95,1)
#    print([x for x in get_nodes_of_connected_graph(g)])
    