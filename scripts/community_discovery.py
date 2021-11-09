#Community discovery on backboning
import networkx as nx
import pandas as pd


def CD_unipartite(Graph, method = 'label_prop',weight_name='score'):
    """
    method options = ['label_prop_semi','label_prop_asyn','max_modularity']
    'label_prop_asyn'
    -----------------
    The algorithm proceeds as follows. After initializing each node with a unique label, the algorithm repeatedly sets the label of a node to be the label that appears most frequently among that nodes neighbors. The algorithm halts when each node has the label that appears most frequently among its neighbors. The algorithm is asynchronous because each node is updated without waiting for updates on the remaining nodes.
    'label_prop_semi'
    -----------------
    Finds communities in G using a semi-synchronous label propagation method[R1ae1fcea5a29-1]_. This method combines the advantages of both the synchronous and asynchronous models. Not implemented for directed graphs.

    'max_modularity'
    ----------------
    This function uses Clauset-Newman-Moore greedy modularity maximization [2]. This method currently supports the Graph class.

Greedy modularity maximization begins with each node in its own community and joins the pair of communities that most increases modularity until no such pair exists


    'random_walk'
    --------------
    The basic intuition of the algorithm is that random walks on a graph/ network tend to get trapped into densely connected parts corresponding to communities. (read more on towardsdatascience.com


    """
    from networkx.algorithms import community
    from cdlib import algorithms

    if method == 'label_prop_semi':
        return community.label_propagation_communities(Graph)
        #return community.asyn_lpa_communities(Graph)

    elif method == 'label_prop_asyn':
        return community.asyn_lpa_communities(Graph)

    elif method == 'max_modularity':
        return community.greedy_modularity_communities(Graph, weight=weight_name)

    elif method == 'random_walk':
        return algorithms.walktrap(Graph)

    elif method =='louvain':
        return algorithms.louvain(Graph, weight=weight_name, resolution=1., randomize=False)
    
    
    
    
def Partition_measure(Graph,communities,method = 'modularity',weight_name='score'):
    """
    METHODS
    modularity
    ----------
    look into NA book

    coverage
    --------
    The coverage of a partition is the ratio of the number of intra-community edges to the total number of edges in the graph.

    performance
    -----------
    The performance of a partition is the number of intra-community edges plus inter-community non-edges divided by the total number of potential edges.


    """
    from networkx.algorithms import community

    if method == 'modularity':
        """
        If resolution is less than 1, modularity favors larger communities. Greater than 1 favors smaller communities.
        """
        return community.modularity(Graph, communities,weight=weight_name,resolution=1)

    elif method == 'coverage':
        return community.quality.coverage(Graph, communities)

    elif method == 'performance':
        return community.quality.performance(Graph, communities)




if __name__ == '__main__':

    #Read graph
    edge_list = pd.read_csv('backbone_test.csv')
    G = nx.from_pandas_edgelist(edge_list,'src','trg', edge_attr='score')
    print(G.edges(data=True))
    G2 = nx.karate_club_graph()
    print(G.get_edge_data('r1','r1111').get('score',1))

    #Print communities
    print(list(CD_unipartite(G, method='random_walk')))

    #Quality measure
    print('Quality:', Partition_measure(G,CD_unipartite(G, method='label_prop_semi'),method='modularity'))





