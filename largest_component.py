import networkx as nx
import itertools as it

class CompleteGraphTools(object):
    """ Graph is a networkx graph
    if you want completely connected graphs of a certain sizes 
    you can specify the lower and upper bounds"""
    
    def __init__(self, graph=nx.Graph(), lower_bound=3, upper_bound=None):
        if not graph:
            raise AttributeError('Graph was not specified')
        self.graph = graph
        if lower_bound:
            self.lower_bound=lower_bound
        else:
            self.lower_bound=3 #look for triangles
        self.upper_bound=upper_bound        

#    def get_largest_connected_component(self):
#        raise NotImplementedError("fix this")

    def get_relevant_edges(self):
        """ a filter for edges
        returns an edge where the number of triangles could be a part 
        of a completely connected graph of size "lower_bound"
        """
        if self.lower_bound<3:
            raise AttributeError("""Lower bound needs to be >=3 nodes as this
                can only find triangles and above""")
        lowest_bound= self.lower_bound-1
        should_have_x_triangles = sum(xrange(lowest_bound))
        for x,y in self.graph.edges():
            print("number of triangles: ",nx.triangles(self.graph,x))
            print("number of triangles: ", nx.triangles(self.graph,y))            
            if nx.triangles(self.graph,y)>=should_have_x_triangles \
                and nx.triangles(self.graph,x)>=should_have_x_triangles:
                try:
                    [x,y]=sorted([x,y])
                except:
                    pass
                yield x,y

    def len_node(x,node_num):
        node_list = set([y for x in triad for y in x])
        if len(node_list)==self.lower_bound:
            output[tuple(node_list)]=1
        
    def flat_map(f, items):
            return it.chain.from_iterable(it.imap(f, items))
    
    def my_map(self):
        output = set()
        for list_of_edges in it.combinations(self.get_relevant_edges(),self.lower_bound):
            for x in list_of_edges:
                output.update(x)

        yield sorted(list(output))
        del output


    def get_connected_nodes(self):
        raise NotImplementedError("fix this")
       #keep the state of the graph connections with a counter object so you cna count down the edge counts
    #    for triad in it.combinations(get_relevant_edges(graph),connected_nodes):
    #        it.ifilter(,it.combinations(get_relevant_edges(graph, connected_nodes)))
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
    