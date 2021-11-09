## Problem analysis

### `Problem statement, RQ, understanding the problem`

- See [this](https://docs.google.com/presentation/d/13dyLBafxCt2VNjRtrBzkrYpuNhHQViyT52FdB1JcBHQ/edit#slide=id.g100a2b6b40c_0_0) slide

### `Possible ways to solve the problem`

- See [this](https://docs.google.com/presentation/d/13dyLBafxCt2VNjRtrBzkrYpuNhHQViyT52FdB1JcBHQ/edit#slide=id.g100b71d134b_0_0) and following couple slides

## Ideas/Notes to the readings

### Comunnity Discovery 1


#### Chapter 2

- Talks about probability theory to make inferences about uncertain events

- Mentions frequenist approach and bayesian approach 

- Markov processes which are sotchastic processes (changes over time)

- Mutual information tells how related two random variables are

#### Chapter 3 simple graphs

- Introduction to the different graphs


#### Chapter 4 Extended graphs

- talks about biparte networks and all the other types of networks

#### Chapter 5 Matrices

- Mentions all the different types of matrices

- transposing a matrix means mirroring it on its main diagonal and can be used to look at two different modes of connection in a biparte network

#### Chapter 7 Paths & walks

- introduction to the different properties of graphs such as cyclic, acyclic, tree etc.

- "You can count the number of connected components in a graph by counting the number of eigenvalues equal to one of its stochastic adjacency matrix. The non-zero entries in the corresponding eigenvectors tell you which nodes are in which connected component" taken from the book (might be worth remembering for the exam)

- Mentions strong and weak components (strong abide by the edge direction and weak ignore the edge direction)

#### Chapter 8 Random walk

- 

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

### Comunnity Discovery 2

#### Chapter 33

- This chapter focuses on hiearchical community discovery. This in practice means for example finding a community of a community.

- There are two approaches to do so, which we also know from ML lecture about clustering. Bottom up and top down approach where the latter is more computationally expensive.

- **Application to our project**

  - I can imagine that we could first have a community of all repositories that are written in a given language (or at least the majority is written for a certain language). For instance all repositories for `Ruby` developers. Then, this community could be perhaps split into the utility of the repository such as authentication, testing framework etc.

  - Again, we core challenge will be probably to figure out how to deal with disconnected components, e.g., select the largest and treat them as a separate network and then perform the hiearchical community discovery on them..?

#### Chapter 34

- This chapter extends the concept of community discovery in a sense that node can be part of more than one communities

- The above assumption seems indeed more realistic for a real world network.

- The introduced algorithms were mostly extensions of algorithms from chapter 32 (see above). Therefore, I **would suggest** to pick the relevant ones and try it out on our projected networks.

- In addition, I feel like this type of community detection seems more relevant than the one introduced in chapter 33, i.e. hiearchical.

#### Chapter 35

- This chapter is **the most relevant** chapter from all the chapters related to community discovery since it talks about community discovery for bipartite networks

- Two main approaches are:

  - Do the community discovery within the bi-partite network
    - In this case, you need to use a some extended algorithms
  - Project the network and then use algorithms which you would have used on a unipartite network

    - The problem with this approach is that you are losing information using the projection which then leads for poorer estimates of communities

    - Another problem is that when you find communities of lets say repos, then you might want to know to which users they belong to. I guess for our application, this is not a problem.

#### Chapter 36

- not applicable to our project since it talks about community discovery within multi-layer networks

## Useful resources

- Michele's [code page](https://www.michelecoscia.com/?page_id=25) with useful algorithms
