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
- [ ] Network cleaning
  - Take care of mismatches between repos.txt and lang.txt
  - We should filter out nodes whose edges were randomly removed, see my node in slack channel phase-02-eda

## Do a summary of our bipartite network

- [x] Degree distribution
- [x] Core metrics such as number of nodes, edges, any self-loops etc.
- [ ] (Add more here if needed)

## Network projection

- [x] Apply following methods to project our network onto repositories:
  - Simple weight
  - Jaccard
  - Probs
  - Heats
  - Hyperbolic
  - Vectorised projections (e.g. Cosine) - Implemented but due to performance reasons excluded it

## Network backboning

- [x] Do network backboning using following methods:
  - Disparity filter
  - Noise corrected filter
  - Double Stochastic - attempted but did not converge

## Compute standard network summary metrics

- [ ] Analyse each method (Projection + Backboning) using:
  - Edge weight distribution
  - Degree Distribution
  - Power law degree fit
  - (Add more here if needed)

_(Note that there might be additional sections added to here)_

## Visualisation

- [ ] Basic Visualisation of structure of Graph -> very small subgraph -> library that is able to plot bipartite structure
- [ ] Interactive Network Visualisation -> pyvis.Network
