# -*- coding: utf-8 -*-
"""
Created on Fri Apr 03 01:33:40 2015

@author: jeremy
"""

import unittest as ut
import networkx as nx
from largest_component import NodeGraph as ng

class NewVisitorTest(ut.TestCase): #
    def setUp(self): 
        self.maxDiff=None
        self.g=nx.complete_graph(3)
        self.G=nx.complete_graph(5)
        #examples of objects and their answers for various tests
        self.a = {'obj': ng(self.g,3),
                  'get_edges':[(0,1),(0,2),(1,2)],
                  'my_map': [[0,1,2]]}
        self.b = {'obj':ng(self.G,5),
                  'get_edges':[(0, 1),
                                (0, 2), 
                                (0, 3),
                                (0, 4),
                                (1, 2),
                                (1, 3),
                                (1, 4),
                                (2, 3),
                                (2, 4),
                                (3, 4)],
                  'my_map': [[0,1,2,3,4]]
                  }
        self.blank = {'obj': ng(nx.Graph(),0),
                      'get_edges':[],
                        'my_map': [[]]}
        self.text_graph = nx.Graph()
        self.text_graph.add_path(['a','b','c'])
        self.text_graph.add_path(['a','c','d'])
        self.text ={'obj': ng(self.text_graph,3),
                      'get_edges':[('a','b'),('b','c'),('a','c')],
                        'my_map': [['a','b','c']]}
        
        self.graphs = self.a,self.b,self.blank,self.text
        
    def test_get_edges(self):
#        ut.TestCase.assertEqual(get_triangle_nodes(g))
        for graph in self.graphs:
            self.assertFalse(set([x for x in graph['obj'].get_edges()]).difference(graph['get_edges']))

    def test_my_map(self):
        for graph in self.graphs:
            self.assertEqual(list(graph['obj'].my_map()),graph['my_map'])

     def test_get_nodes_of_connected_graph(self):
         for graph in self.graphs:
             self.assertEqual(
                 [x for x in graph.get_nodes_of_connected_graph()],
                  [(0, 1, 2)]
                  )
                  self.assertEqual(
                  [x for x in self.a.get_nodes_of_connected_graph()],
                   [(0, 1, 2, 3, 4)]
                   )


if __name__ == '__main__':
    ut.main()
