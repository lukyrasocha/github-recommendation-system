import networkx as nx
from tqdm import tqdm
import json
import os
import math


def naive_recommend(G, n=5):
    """
    The NaiveRecommend algorithm makes recommendation sorely on the neighboring repositories
    in the final recommendation graph. For each node, we consider the n neighboring
    repositories with highest edge weight, as we assume those to be the most similar, and thus
    the best recommendation. 

    Runtime: |V|*avg(k)
    Memory: |V|*n
    """

    recommendations = {}
    for node in tqdm(G.nodes()):
        sorted_neighbors = [x[0] for x in sorted(G[node].items(), 
                            key=lambda x:x[1]['weight'], reverse=True)][:n]
        recommendations[node] = sorted_neighbors

    return recommendations


def search_depth_recommend(G, n=5, search_depth='max'):
    """
    The SearchDepthRecommend improves the NaiveRecommend by also considering non-neighboring 
    repositories. It is based on the idea, that a low-weight neighboring repository is not 
    as good of a recommendation as a highly connected second level neighbor (ie. it follows
    communities of repositories).
    The algorithm is based on n calls to dijkstras on the graph subsetted to a certain search depth,
    at each node dijkstras chooses the maximum edge weight to construct the max weight path of 
    length search_depth. We then consider all possible length paths and compute a disproportional
    weighted average.
    """
    if search_depth == 'max':
        search_depth = math.inf

    recommendations = {}
    for node in G.nodes():
        path = [] 
        # start dijkstras with search depth
        current_search_depth = 1
        max_neighbor = max(G[node].items(), key=lambda x:x[1]['weight'])
        visited = set(G[node])
        visited.add(node)
        path.append(max_neighbor)

        while current_search_depth < search_depth:
            # find neighbors of the previous max neighbor without the node 
            max_neighbors = dict(G[max_neighbor[0]])

            # filter out all already visited neighbors
            max_neighbors = {neighbor: weight for neighbor, weight in max_neighbors.items() 
                                if neighbor not in visited}
            visited.union(set(max_neighbors.keys()))
            visited.add(max_neighbor[0])

            # stop search depth if no more neighbors
            if len(max_neighbors) == 0:
                break

            # recompute max_neighbors
            max_neighbor = max(max_neighbors.items(), key=lambda x:x[1]['weight'])
            path.append(max_neighbor)
            current_search_depth += 1

        naive_recommend = [(key, val['weight']) for key, val in G[node].items()]
        dijkstra_scores = list(_dijkstra_scores(path).items())
        all_recommend = naive_recommend + dijkstra_scores

        recommendations[node] = [x[0] for x in sorted(all_recommend, key=lambda x:x[1], reverse=True)][:n]

    return recommendations

def write_recommendation(recommendations, metadata, filepath='.', name='untitled'):
    os.makedirs(filepath) if not os.path.exists(filepath) else None

    ans = {}
    for key, val in recommendations:
        key = metadata[key]['repo_name']
        val = [metadata[v]['repo_name'] for v in val]

        ans[key] = val

    with open(f'{filepath}/{name}.json', 'w') as outfile:
        json.dump(key, outfile)

def _dijkstra_scores(path, penalty='linear'):
    scores = {}
    for i, node in enumerate(path):
        if i == 0:
            continue
        node,_  = node
        scores[node] = 0
        for j in range(1, i+2):
            scores[node] += 1/j**2 * path[j-1][-1]['weight']
        scores[node] /= i+1
    return scores



if __name__ == '__main__':
    # generate test recommendation system
    print('Start reading')
    G = nx.read_weighted_edgelist('../data/projections/edge_list_format/simple_weight.edges', delimiter = '\t')
    print('Done reading')

    with open('../data/transformed/metadata.json') as infile:
        metadata = json.load(infile)

    """
    weighted_edge_list = [
            [1, 3, {'weight': 0.3}],
            [1, 4, {'weight': 0.01}],
            [2, 3, {'weight': 0.5}]
            ]

    G = nx.from_edgelist(weighted_edge_list)
    """
    write_recommendation(naive_recommend(G, n=1), metadata)

    #print('Naive Recommend: ', naive_recommend(G, n=2))
    #print('Search Depth Recommend: ', search_depth_recommend(G, search_depth=3))
