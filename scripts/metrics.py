# metrics.py 
# script holding function to analyse unipartite and bipartite networkx

# last modified     : 09/11/21
# author            : jonas-mika senghaas

import os
import time
from datetime import date
from handle_timeout import * 

import numpy as np
import pandas as pd
import networkx as nx
from tqdm import tqdm

# global settings
STOP_EXECUTION = 15 
np.set_printoptions(suppress=True)

def five_num_summary(arr):
    return np.percentile(arr, [0, 25, 50, 75, 100])

@break_after(STOP_EXECUTION)
def get_degrees(G):
    return [degree for _, degree in G.degree()]

@break_after(5)
def get_lccs(G):
    return list(nx.clustering(G).values())

@break_after(STOP_EXECUTION)
def get_ccs(G):
    return [G.subgraph(cc) for cc in nx.connected_components(G)]

# single network metrics
@break_after(STOP_EXECUTION)
def number_of_nodes(G):
    return G.number_of_nodes()

@break_after(STOP_EXECUTION)
def number_of_edges(G):
    return G.number_of_edges()

# degree
@break_after(STOP_EXECUTION)
def average_degree(degrees):
    return np.mean(degrees)

@break_after(STOP_EXECUTION)
def summarise_degrees(degrees):
    return five_num_summary(degrees)

# local clustering coefficient
@break_after(STOP_EXECUTION)
def average_lcc(lccs):
    return np.mean(lccs)

@break_after(STOP_EXECUTION)
def summarise_lcc(lccs):
    return five_num_summary(lccs)

# connected components (size)
@break_after(STOP_EXECUTION)
def number_of_ccs(ccs):
    return len(ccs)

@break_after(STOP_EXECUTION)
def average_cc_size(ccs):
    return np.mean([cc.number_of_nodes() for cc in ccs])

@break_after(STOP_EXECUTION)
def summarise_cc_size(ccs):
    return five_num_summary([cc.number_of_nodes() for cc in ccs])

# density 
@break_after(STOP_EXECUTION)
def global_density(G):
    return nx.density(G)

@break_after(STOP_EXECUTION)
def average_cc_density(G, ccs):
    return np.mean([nx.density(cc) for cc in ccs])

@break_after(STOP_EXECUTION)
def summarise_cc_density(G, ccs):
    return five_num_summary([nx.density(cc) for cc in ccs])

# diameter (longest shortest path)
@break_after(STOP_EXECUTION)
def global_diameter(G):
    if nx.is_connected(G):
        return nx.diameter(G)
    else: return 'No Global Diameter (Unconnected Graph)'

@break_after(STOP_EXECUTION)
def average_diameter(ccs):
    return np.mean([nx.diameter(cc) for cc in ccs])

@break_after(STOP_EXECUTION)
def summarise_diameter(ccs):
    return five_num_summary([nx.diameter(cc) for cc in ccs])

# centrality measures
@break_after(STOP_EXECUTION)
def degree_centrality(G, n):
    return sorted([item for item in nx.algorithms.centrality.degree_centrality(G)], 
                    key=lambda item: item[1], reverse=True)[:n]

@break_after(STOP_EXECUTION)
def betweenness_centraliy(G, n):
    return sorted([item for item in nx.algorithms.centrality.betweenness_centrality(G)], 
                    key=lambda item: item[1], reverse=True)[:n]

# meta-level statistics
def basic_metrics(G):
    return {'Number of Nodes': number_of_nodes(G), 
            'Number of Edges': number_of_edges(G), 
            'Global Density' : f'{round(global_density(G)*100, 2)}%'}
            #'Global Diameter': global_diameter(G),
            #'Average Diameter': f'{round(average_diameter(G), 2)}', 'Five-Number-Summary Diameter': summarise_diameter(G)}

def degree_metrics(G):
    degrees = get_degrees(G)
    if degrees != None:
        return {'Average Degree': f'{round(average_degree(degrees), 2)}',
                'Five-Number-Summary Degrees': summarise_degrees(degrees)}
    else: 
        return {name: 'TimeoutException' for name in ['Average Degree', 'Five-Number-Summary Degrees']}

def lcc_metrics(G):
    lccs = get_lccs(G)
    if lccs != None:
        return {'Average LCC': f'{round(average_lcc(lccs), 2)}',
                'Five-Number-Summary LCC': summarise_lcc(lccs)}
    else: 
        return {name: 'TimeoutException' for name in ['Average LCC', 'Five-Number-Summary LCCS']}

    
def cc_metrics(G):
    ccs  = get_ccs(G)
    if ccs != None:
        return  {'Number of CC': number_of_ccs(ccs), 
                 'Average CC Size': f'{round(average_cc_size(ccs), 2)}', 
                 'Five-Number-Summary of CC Sizes': summarise_cc_size(ccs),
                 'Average CC Density': average_cc_density(G, ccs),
                 'Five-Number-Summary of CC Densities': summarise_cc_density(G, ccs)}

def generic_markdown_summary(G, filepath, name):
    titles = ['Basic Metrics', 
              'Degree Metrics', 
              'Clustering (LCC) Metrics', 
              'Connected Componenent (CC) Metrics']
    meta_funcs = [basic_metrics, degree_metrics, lcc_metrics, cc_metrics]

    s = f"# Generic Summary of Unipartite Graph **{name}**\n---\n"
    s += f"Created: {date.today().strftime('%d/%m/%y')}\n\n"

    for title, meta_func in zip(titles, meta_funcs):
        s += f'## {title}\n---\n'
        s += "|   Network Statistic   |   Computed Value   |\n"
        s += "|:---------------------:|:---------------------------------------------:|\n"
        for func_name, res in tqdm(meta_func(G).items()):
            s += f"|   {func_name}   |   {res if not None else 'TimeoutException'}   |\n"
        s += '\n\n'

    with open(f'{filepath}/{name}.md', 'w') as outfile:
        outfile.write(s)


def test():
    G = nx.read_gpickle('../data/projections/pickle_format/simple_weight.pickle')
    # G = nx.karate_club_graph()

    generic_markdown_summary(G, '.', 'test')


    """
    def gen_l(n):
        return [[(i,j) for i in range(n)] for j in range(n)]

    gen_l(10000)
    start = time.time()
    #df = pd.read_csv('../data/backboning/nc_table_simple_weight.csv')
    #G = nx.from_pandas_edgelist(df, source='src', target='trg', edge_attr='score')
    #G = nx.karate_club_graph()
    end = time.time()
    print(f'Finished Reading in {end-start}s')

    # print(nx.clustering(G))

    print(number_of_nodes(G))
    print(number_of_edges(G))
    print(global_density(G))
    print('\nDegree Metrics')
    print(degree_metrics(G))
    
    print('\nLCC Metrics')
    print(lcc_metrics(G))

    print('\nCC Metrics')
    print(cc_metrics(G))
    """

if __name__ == '__main__':
    test()
