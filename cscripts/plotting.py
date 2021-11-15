# plotting.py 
# script holding function to analyse unipartite and bipartite networkx

# last modified     : 09/11/21
# author            : jonas-mika senghaas

import os
import sys
from collections import Counter

# allow imports locally (without referring to module structure)
local_path = os.path.dirname(os.path.realpath(__file__))
if local_path not in sys.path:
    sys.path.append(local_path)

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

    ax.set_title(f"Degree Distribution of {name.title()} ({scale.title()}-Scale)", weight = "bold")
    ax.set(xlabel='Degrees ($k$)', ylabel='Counts')

    if scale == 'log':
        ax.set_xscale('log') 
        ax.set_yscale('log')
        ax.set_xlim(10**0*0.9, 10**5)
    elif scale != 'linear':
        return None

    return ax

def plot_degree_distribution(*degrees, names=None, scales='linear', figsize=(5,5)):
    if names == None:
        names = ['Unnamed' for _ in range(len(degrees))]
    if type(scales) == str:
        scales = [scales]

    # initialising subplots figure
    n_rows = len(scales)
    n_cols = len(degrees)

    fig, axs = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(figsize[0]*n_cols, figsize[1]*n_rows), 
                            constrained_layout=True)

    # formatting axes array
    axs = np.array(axs)
    if n_rows > 1 and n_cols==1:
        axs = axs.reshape(-1, 1)
    elif n_rows == 1 and n_cols > 1:
        axs = axs.reshape(1, -1)
    elif n_rows == 1 and n_cols == 1:
        axs = axs.reshape(1, 1)


    for i, s in zip(range(n_rows), scales):
        for j, degree, name in zip(range(n_cols), degrees, names):
            fig = plot_single_degree_distribution(degree, name, 
                                                  figsize=figsize, 
                                                  ax=axs[i][j], 
                                                  scale=s)

    return fig



def generate_plots(G, name, filepath='.', create_path=True):
    if create_path:
        os.makedirs(filepath) if not os.path.exists(filepath) else None

    names = ['degree_distribution']
    funcs = [plot_degree_distribution]

    for func_name, func in zip(names, funcs):
        if func_name == 'degree_distribution': 
            fig = func(get_degrees(G), names=[name], scale=['linear', 'log'])
        
        plt.savefig(f'{filepath}/{func_name}.jpg')


if __name__ == '__main__':
    # test code
    """
    G = nx.read_gpickle('../data/projections/pickle_format/simple_weight.pickle')
    G2 = nx.read_gpickle('../data/projections/pickle_format/heats.pickle')
    """

    G = nx.karate_club_graph()
    G2 = nx.karate_club_graph()

    degrees = get_degrees(G)
    degrees2 = get_degrees(G2)
    degrees3 = get_degrees(G2)

    fig = plot_degree_distribution(degrees, degrees2, names=['test1', 'test2'], scales=['linear', 'log'])
    plt.show()
