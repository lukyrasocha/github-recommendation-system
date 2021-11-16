import networkx as nx
from tqdm import tqdm
import json

def naive_recommend(G, metadata, filepath='.', name='untitled'):
    recommendations = {}
    for node in tqdm(G.nodes()):
        sorted_neighbors = sorted(G[node].items(), key=lambda x:x[1]['weight'], reverse=True)
        repo_names = [metadata[r]['repo_name'] for r, _ in sorted_neighbors]
        recommendations[metadata[node]['repo_name']] = repo_names

    with open(f'{filepath}/{name}.json', 'w') as f:
        json.dump(recommendations, f)
