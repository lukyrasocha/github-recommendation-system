## General

- [x] Add proper requirements.txt file

## Which sections to re-compute

- [ ] Projections
- [ ] Summary projections
- [ ] Compute backboning scores
- [ ] Select threshold, bacbone selected projected network and run summary algorithm

## Questions to ask

- [x] How to deal with too many components in the network? (See slack)

## Network Selection and basic summary

- [x] Choose a proper network to work on
- [x] Do basic summary:
  - Where the network is from
  - What it represents
  - What are the nodes attributes
  - (Add more if needed)
  - See the result of this step on this [slide](https://docs.google.com/presentation/d/13dyLBafxCt2VNjRtrBzkrYpuNhHQViyT52FdB1JcBHQ/edit#slide=id.p)

## Network preprocessing steps

- [x] Get the data into suitable format such that they can be easily readed into NetworkX Graph as edgelist. See the result in: `data/transformed/data.txt`.
- [x] Extract the metadata for each repository and save is as a JSON so we can then easily added to NX graph nodes object. See the result in `data/transformed/metadata.json`.
- [x] Network cleaning (see the corresponding section in `main.ipynb`)
  - Take care of mismatches between repos.txt and lang.txt
  - Take care of nodes whose edges were randomly removed, see my node in slack channel phase-02-eda

## Do a summary of our bipartite network

- [x] Core metrics such as number of nodes, edges, any self-loops etc.
- [x] Top 10 repositories in terms number of watches
- [x] Top 10 languages in terms of usage
- [x] Degree distribution
- [x] Power law fit - partially done - need to add comments regards to the computation
- [ ] (Add more here if needed)

## Network projection

- [x] Apply following methods to project our network onto repositories:
  - Simple weight
  - Jaccard
  - Probs
  - Heats
  - Hyperbolic
  - Vectorised projections (e.g. Cosine) - Implemented but due to performance reasons excluded it
- [ ] Add description/comment to the above defined methods

## Network backboning

- [x] Do network backboning using following methods:

  - Disparity filter
  - Noise corrected filter
  - Double Stochastic - attempted but did not converge

- [x] Save all backboned graphs for the later use

- _(Add more here if needed)_

## Analysis of Metrics and Visualising Unipartite Networks (Projection/ Backboned Networks)

- [ ] Add further plots to generated markdown (ccdf of dd, power law fit, distribution
      of edge weights, distribution of cc sizes, ...)
- [ ] Find way to automatically convert MD into well-formatted PNG, PDF (to load
      file into Jupyter while displaying plots) / alternatively: find out why iPython's
      display(Markdown) does not show the produced local plots

- [ ] maybe create handle 'bipartite' that allows to compute all metrics and plots for each
      class of nodes individually

## Finding relevant repositories: [method 1]

- [ ] _(Add relevant todos)_

## Finding relevant repositories: [method 2]

- [ ] _(Add relevant todos)_

## Community discovery

### On projected graphs

- [x] Random walk
- [x] Label propagation
- [_] Mutual information

### Metrics to evaluate communities

- [x] Modularity
- [x] Coverage
- [x] Performance

### On the original bi-partite network

- [ ] _(Add relevant methods here)_

### Summary of the findings

- [ ] _(Add relevant todos)_

_(Note that there might be additional sections added to here)_

## Other

- [x] make helperfunction to produce metadata about computationally heavy runs
- [x] after done: rerun those computations and produce the metadata

  - [x] projections
  - [ ] summary of projections (fix some bugs, see below)
        -> Fix plotting of edge weight distribution (sort by value in counter dict)
  - [ ] backboned graphs
  - [ ] summary of backboned graphs

- [ ] move projection methods into csripts (?)

## Visualisation

- [ ] Basic Visualisation of structure of Graph -> very small subgraph -> library that is able to plot bipartite structure
- [ ] Interactive Network Visualisation -> pyvis.Network
