## Ideas/Notes to the readings

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

## Useful resources

- Michele's [code page](https://www.michelecoscia.com/?page_id=25) with useful algorithms
