## #04 Numerical Summaries

Learnit: Basic network statistics of your data (number of nodes, edges, clustering, degree distribution, etc). In practice, the result of project phase #2 (exploratory data analysis).

- [x] Plots of Degree Distribution (how to plot dd of bipartite network?) -> histogram of degrees
- [x] CCDF (inverse/ complement cumulative distribution function)
- [ ] Power Law Fitting (how does it work with bipartite network?)
- [ ] Stationary Matrix

## #05 Visualisation

- [ ] Basic Visualisation of structure of Graph -> very small subgraph -> library that is able to plot bipartite structure
- [ ] Interactive Network Visualisation -> pyvis.Network

## #06 Projection

- [ ] Apply different methods of bipartite projectin (simple weighting, hyperbolic, hyperbolic2, vectorised projection, random walk)
- [ ] Analyse each method (using edge weight distribution, ...)
- [ ] Argue for which projection to use for recommendation system

## #7 Using Projected Graph

- [ ] Make some inital network statistics
- [ ] Backboning of out network (try out different methods for backboning - argue for them)

## #07 Recommendation system

- [ ] Write for each node adjacent nodes ordered by decreasing edge weight

## #08 Research question phrasing

## #09 Final

- [ ] Cleanup main notebook
- [ ] Presentation
- [ ] Reherse Presentation

## # Drafts of a research question

- "How can we use bipartite network to make accurate recommendations of github repositories?"

## #0X Ideas/Notes to the readings

### Comunnity Discovery 1

#### Chapter 31

- Since we have a lot of disconnected components, we should examine first their size and then perhaps figure out if it even makes sense to actually do community discovery. In other words, if we decide to do community discovery, then we should indeed do it on the largest components

- Algorithms that we could use for community discovery:

  - Label propagation, here is NetworkX [method](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.label_propagation.label_propagation_communities.html#networkx.algorithms.community.label_propagation.label_propagation_communities)
  - InfoMap algorithm, we could use this [library](https://mapequation.github.io/infomap/index.html)

- There is also a mention regards to evolving networks in time, but that does not apply to our network as we have only one concrete snapshot

#### Chapter 32

- General summary to the use case for our project: This chapter focuses on methods to evaluate partitions into communities. In addition, some methods can be used as cost/utility function in order to optimize our partition.

- Methods we should consider for our community detection evaluation:
  - Modularity
  - Normalized mutual information
  - Normalized mincut
  - Out degree fraction

## #0X Useful resources

- Michele's [code page](https://www.michelecoscia.com/?page_id=25) with useful algorithms
