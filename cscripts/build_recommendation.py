import networkx as nx
from tqdm import tqdm
import json

PROJECTIONS_TYPES = [
        'simple_weight'
        ]

SAVE_PATH = '../recommendations'
N = 5

def single_repo_recommend(G, n):
    return {node: [G.nodes[el[1]]['metadata'] for el in sorted([edge for edge in G.edges(node, data=True)] , key=lambda x:x[-1]['weight'], reverse=True)][:n] for node in G.nodes()}

for projection in tqdm(PROJECTIONS_TYPES):
    G = nx.read_gpickle(f'../data/projections/{projection}.pickle')

    with open(f'{SAVE_PATH}/{projection}/single_recommend{N}.json', 'w') as f:
        json.dump(single_repo_recommend(G, n=N), f)
