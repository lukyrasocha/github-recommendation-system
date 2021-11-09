# summarise.py
# file that contains code to generate complex summaries including all relevant network 
# statistics and visualisation for a generic graph.

# last modified: 09.11.21
# author: jonas-mika senghaas

import os
from time import time
from datetime import date
import networkx as nx

# custom imports
from metrics import export_metrics
from plotting import generate_plots


def generate_markdown(G, filepath, name='unnamed'):
    savepath = f'{filepath}/{name}'
    os.makedirs(savepath) if not os.path.exists(savepath) else None

    s = f"# Generic Summary of Unipartite Graph **{name.title()}**\n---\n"
    s += f"Created: {date.today().strftime('%d/%m/%y')}\n"

    start = time()
    stats = export_metrics(G) 
    generate_plots(G, name=name, filepath=f'{savepath}/assets')
    end = time()
    s += f"Computation Time: {round(end - start, 2)}sec\n\n"

    # metrics
    for section in stats:
        s += f'## {section}\n---\n'
        s += '<table>\n<tr><th align="center"><img width="441" height="1"><p><small>Network Statistic</small></p></th><th align="center"><img width="441" height="1"><p><small>Result</small></p></th></tr>\n'

        for func_name, res in stats[section].items():
            s +=f"<tr><td>{func_name}</td><td>{res if not None else 'TimeoutException'}</td></tr>\n"
        s += '</table>\n\n'


    # plots
    for file in os.listdir(f'{savepath}/assets'):
        title = file[:-4].replace('_', ' ').title()
        s += f'## {title} Plot\n---\n'
        s += f'![image](./assets/{file})'

    # write all string to markdown file
    with open(f'{savepath}/{name}.md', 'w') as outfile:
        outfile.write(s)


if __name__ == '__main__':
    # test code
    G = nx.karate_club_graph()
    generate_markdown(G, filepath='../data/graph_summaries', name='karate')
