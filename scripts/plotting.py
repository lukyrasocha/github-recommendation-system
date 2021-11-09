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

import metrics 

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

    ax.set_title(f"Degree Distribution of {name.title()} ({scale.title()}-Scale)", weight = "bold")
    ax.set(xlabel='Degrees ($k$)', ylabel='Counts')

    if scale == 'log':
        ax.set_xscale('log') 
        ax.set_yscale('log')
        ax.set_xlim(10**0*0.9, 10**5)
    elif scale != 'linear':
        return None

    return ax

def plot_degree_distribution(*degrees, names=None, figsize=(5, 5), scale='linear'):
    if type(scale) == str:
        scale = [scale]
    if names == None:
        names = ['Unnamed' for _ in range(len(degrees))]

    n_rows = len(degrees)
    n_cols = len(scale)

    fig, axs = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(figsize[0]*n_cols, figsize[1]*n_rows))

    if n_rows > 1 and n_cols > 1:
        for h_ax, s in zip(axs, scale):
            for ax, degree, name in zip(h_ax, degrees, names):
                fig = plot_single_degree_distribution(degree, name, 
                                                      figsize=figsize, 
                                                      ax=ax, 
                                                      scale=s)

    elif n_rows > 1:
        for ax, degree, name in zip(axs, degrees, names):
            fig = plot_single_degree_distribution(degree, name, 
                                                  figsize=figsize, 
                                                  ax=ax, 
                                                  scale=scale)

    elif n_cols > 1:
        for ax, s in zip(axs, scale):
            fig = plot_single_degree_distribution(degrees[0], names[0], 
                                                  figsize=figsize, 
                                                  ax=ax, 
                                                  scale=s)

    else:
        fig = plot_single_degree_distribution(degrees[0], names[0], 
                                              figsize=figsize,
                                              ax=axs, 
                                              scale=scale)

    return fig



def generate_plots(G, name, filepath='.'):
    os.makedirs(filepath) if not os.path.exists(filepath) else None

    names = ['degree_distribution']
    funcs = [plot_degree_distribution]

    for func_name, func in zip(names, funcs):
        if func_name == 'degree_distribution': 
            fig = func(metrics.get_degrees(G), names=[name], scale=['linear', 'log'])
        
        plt.savefig(f'{filepath}/{func_name}.jpg')


if __name__ == '__main__':
    # test code
    """
    G = nx.read_gpickle('../data/projections/pickle_format/simple_weight.pickle')
    G2 = nx.read_gpickle('../data/projections/pickle_format/heats.pickle')
    """

    G = nx.karate_club_graph()
    G2 = nx.karate_club_graph()

    degrees = metrics.get_degrees(G)
    degrees2 = metrics.get_degrees(G2)

    fig = plot_degree_distribution(degrees, degrees2,
                                   scale=['linear', 'log'])
    plt.show()
