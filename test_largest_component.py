# -*- coding: utf-8 -*-
"""
Created on Fri Apr 03 01:33:40 2015

@author: Jeremy Langley
"""

import unittest as ut
import networkx as nx
from largest_component import CompleteGraphTools as cgt

class NewVisitorTest(ut.TestCase,object):
    def setUp(self): 
        self.maxDiff=None
        self.g=nx.complete_graph(3)
        self.g.add_edge(0,7)
        self.G=nx.complete_graph(5)
        #examples of objects and their answers for various tests
        self.a = {'obj': cgt(self.g,3),
                  'get_relevant_edges':[(0,1),(0,2),(1,2)],
                  'my_map': [[0,1,2]],
                  'get_nodes_of_connected_graph':[0,1,2]}
        self.b = {'obj':cgt(self.G,5),
                  'get_relevant_edges':[(0, 1),
                                (0, 2), 
                                (0, 3),
                                (0, 4),
                                (1, 2),
                                (1, 3),
                                (1, 4),
                                (2, 3),
                                (2, 4),
                                (3, 4)
                                ],
                  'my_map': [[0,1,2,3,4]],
                  'get_nodes_of_connected_graph':[0,1,2,3,4]
                  }
        self.c = {'obj':cgt(self.G,3),
                  'get_relevant_edges':[(0, 1),
                                (0, 2), 
                                (0, 3),
                                (0, 4),
                                (1, 2),
                                (1, 3),
                                (1, 4),
                                (2, 3),
                                (2, 4),
                                (3, 4)],
                  'my_map': [[0,1,2,3,4]],
                  'get_nodes_of_connected_graph':[0,1,2,3,4]
                              }

        self.H=nx.complete_graph(5)
        self.H.add_path(['a','b','c'])
        self.H.add_path(['a','c'])

        self.d = {'obj':cgt(self.H,lower_bound=3),
                  'get_relevant_edges':[(0, 1),
                                (0, 2), 
                                (0, 3),
                                (0, 4),
                                (1, 2),
                                (1, 3),
                                (1, 4),
                                (2, 3),
                                (2, 4),
                                (3, 4),
                                ('a', 'b'),
                                ('a', 'c'),
                                ('b', 'c')],
                  'my_map': [[0,1,2,3,4,'a','b','c']],
                  'get_nodes_of_connected_graph': [[0,1,2,3,4],['a','b','c']]
                  }

#        self.blank = {'obj': ng(nx.Graph(),0),
#                      'get_edges':[],
#                        'my_map': [[]],
#                      'get_nodes_of_connected_graph':[]}
        self.text_graph = nx.Graph()
        self.text_graph.add_path(['a','b','c'])
        self.text_graph.add_path(['a','c','d'])
        self.text ={'obj': cgt(self.text_graph,3),
                      'get_relevant_edges':[('a','b'),('b','c'),('a','c')],
                      'my_map': [['a','b','c']],
                      'get_nodes_of_connected_graph':['a','b','c']}
        
        self.graphs = self.a,self.b,self.c,self.text
        
    def test_get_edges(self):
#        ut.TestCase.assertEqual(get_triangle_nodes(g))
        for i,graph in enumerate(self.graphs):
            print("graph number: ",i)
            print('graph is :',graph['get_relevant_edges'])
            self.assertFalse(set([x for x in graph['obj'].get_relevant_edges()]).difference(graph['get_relevant_edges']))

    def test_my_map(self):
        for i,graph in enumerate(self.graphs):
            print("graph number: ",i)            
            self.assertEqual(list(graph['obj'].my_map()),graph['my_map'])

#    def test_get_nodes_of_connected_graph(self):
#        for graph in self.graphs:
#            self.assertEqual(
#                [x for x in graph['obj'].get_connected_nodes()],
#                  [(0, 1, 2)]
#                  )
#            self.assertEqual(
#                  [x for x in graph['obj'].get_connected_nodes()],
#                   [(0, 1, 2, 3, 4)]
#                   )

if __name__ == '__main__':
    ut.main()
