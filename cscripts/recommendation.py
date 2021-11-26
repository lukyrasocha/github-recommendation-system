import networkx as nx
from tqdm import tqdm
import json
import os

def naive_recommend(G, metadata, n=5, filepath='.', name='untitled'):
    os.makedirs(filepath) if not os.path.exists(filepath) else None

    recommendations = {}
    for node in tqdm(G.nodes()):
        sorted_neighbors = sorted(G[node].items(), key=lambda x:x[1]['weight'], reverse=True)[:n]
        neighbor_metadata = [metadata[r]['repo_name'] for r, _ in sorted_neighbors]
        recommendations[metadata[node]['repo_name']] = neighbor_metadata

    with open(f'{filepath}/{name}.json', 'w') as f:
        json.dump(recommendations, f)

if __name__ == '__main__':
    # generate test recommendation system
    print('Start reading')
    G = nx.read_weighted_edgelist('../data/projections/edge_list_format/simple_weight.edges', delimiter = '\t')
    print('Done reading')
    with open('../data/transformed/metadata.json') as infile:
        metadata = json.load(infile)

    naive_recommend(G, metadata, n=1, filepath='../webapp/public/data', name='test2')
