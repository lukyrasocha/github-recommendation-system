# plotting.py 
# script holding function to analyse unipartite and bipartite networkx

# last modified     : 09/11/21
# author            : jonas-mika senghaas

import os
from collections import Counter

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import networkx as nx
from tqdm import tqdm

from metrics import get_degrees

# global settings
sns.set_style("darkgrid")
sns.set(rc={"xtick.bottom" : True, "ytick.left" : True})

def plot_single_degree_distribution(degrees, name='', ax=None, figsize=(5,5), scale='linear'):
    if ax == None:
        _, ax = plt.subplots(figsize)

    counter = Counter(degrees)
    data = pd.DataFrame(list(counter.items()), columns = ("k", "count")).sort_values(by = "k")

    sns.scatterplot(data=data, x='k', y='count', 
                    ax=ax, 
                    alpha=0.6)

    ax.set_title(f"Degree Distribution of {name} ({scale.title()}-Scale)", weight = "bold")
    ax.set(xlabel='Degrees ($k$)', ylabel='Counts')

    if scale == 'log':
        ax.set_xscale('log') 
        ax.set_yscale('log')
        ax.set_xlim(10**0*0.9, 10**5)
    elif scale != 'linear':
        return None

    return ax

def plot_degree_distribution(*degrees, names=None, figsize=(5, 5), scale='linear'):
    n_plots = len(degrees)
    fig, axs = plt.subplots(ncols=n_plots, figsize=(figsize[0]*n_plots, figsize[1]))
    if names == None:
        names = ['' for _ in range(len(degrees))]

    if n_plots > 1:
        for ax, degree, name in zip(axs, degrees, names):
            fig = plot_single_degree_distribution(degree, name, 
                                                  figsize=figsize, 
                                                  ax=ax, 
                                                  scale=scale)
    else:
        fig = plot_single_degree_distribution(degrees[0], names[0], 
                                              figsize=figsize,
                                              ax=axs, 
                                              scale=scale)

    return fig



def test():
    G = nx.read_gpickle('../data/projections/pickle_format/simple_weight.pickle')
    G2 = nx.read_gpickle('../data/projections/pickle_format/heats.pickle')
    """
    G = nx.karate_club_graph()
    G2 = nx.karate_club_graph()
    """

    degrees = get_degrees(G)
    degrees2 = get_degrees(G2)

    fig = plot_degree_distribution(degrees, degrees2, 
                                   names=['Simple Weight Projection', 'Heats Projection'],
                                   scale='log')
    plt.show()

if __name__ == '__main__':
    test()
