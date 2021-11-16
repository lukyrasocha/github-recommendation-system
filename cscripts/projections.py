# projections.py 
# script holding function to project bipartite network onto one class

# last modified     : 16/11/21
# author            : jonas-mika senghaas

import os
import sys
import time
from datetime import date
import numpy as np
import networkx as nx
from tqdm import tqdm

local_path = os.path.dirname(os.path.realpath(__file__))
if local_path not in sys.path:
    sys.path.append(local_path)

#--- PROJECTIONS METHODS
def simple_weight(G, u, v):
    n_u, n_v = set(G[u]), set(G[v])
    # len of set of intersection
    return len(n_u & n_v)

def jaccard(G, u, v):
    n_u, n_v = set(G[u]), set(G[v])
    # normalise len of set of intersection by union
    return len(n_u & n_v) / len(n_u | n_v)

def hyperbolic(G, u, v):
    common = set(G[u]) & set(G[v])
    return sum([1/(len(set(G[node])) - 1) for node in common])

def probs(G, u, v):
    common = set(G[u]) & set(G[v])
    return sum([1/(len(set(G[node]))*len(set(G[u]))) for node in common])

def heats(G, u, v):
    common = set(G[u]) & set(G[v])
    return sum([1/(len(set(G[node]))*len(set(G[v]))) for node in common])

def hybrid(G, u, v):
    common = set(G[u]) & set(G[v])
    return sum([1/(len(set(G[node]))*len(set(G[u]))*len(set(G[v]))) for node in common])
 
class VectorisedProjection:
    def __init__(self, G, repos, users):
        self.metric = None
        self.adj = nx.algorithms.bipartite.matrix.biadjacency_matrix(G, repos, users)
        self.repo_map = {repos[i]: i for i in range(len(repos))}
    def project(self, G, u, v):
        v_u = np.ravel(self.adj.getrow(0).todense().sum(axis=0))
        v_v = np.ravel(self.adj.getrow(1).todense().sum(axis=0))
        if self.metric == 'simple_weight':
            return np.sum((v_u + v_v) == 2)
        elif self.metric == 'euclidean':
            return sp.spatial.distance.euclidean(v_u, v_v)
        elif self.metric == 'normalised_euclidean':
            return 1 / (np.sqrt(np.sum(np.power((v_u - v_v),2))) + 1)
        elif self.metric == 'pearson':
            return sp.stats.stats.pearsonr(v_u, v_v)[0] + 1
        elif self.metric == 'cosine':
            return 1 - sp.spatial.distance.cosine(v_u, v_v)
        else:
            print("Please specify one of the following metrics: ['simple_weight', 'euclidean', 'normalised_euclidean', 'pearson', 'cosine'].")



#--- PROJECTION
def project(G, onto=):
    # custom function to perform projections

    # algorithm
    # 1. compute matrix of all neighbors for one class of nodes
    # 2. use double for loop to iterate over all unique pairs of nodes (because
    #    resulting graph is undirected) and compute edge weight according to 
    #    weight function
    #
    # return projected graph including all node attributes () and computed edge weights
    pass

if __name__ == '__main__':
    pass
