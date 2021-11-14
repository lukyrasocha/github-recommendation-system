## Problem analysis

### `Problem statement, RQ, understanding the problem`

- See [this](https://docs.google.com/presentation/d/13dyLBafxCt2VNjRtrBzkrYpuNhHQViyT52FdB1JcBHQ/edit#slide=id.g100a2b6b40c_0_0) slide

### `Possible ways to solve the problem`

- See [this](https://docs.google.com/presentation/d/13dyLBafxCt2VNjRtrBzkrYpuNhHQViyT52FdB1JcBHQ/edit#slide=id.g100b71d134b_0_0) and following couple slides

## Ideas/Notes to the readings

### Comunnity Discovery 1


### Basics

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

### Simple Properties

#### Chapter 6 Degree

- Degree is the nodes most important feature and shows the number of edges connected to a node, although it becomes more than just that in complex graph models such as biparte networks etc.

- mentions degree distributions, which is most often plotted with the compliment of the cumulative distribution shown in a log-log plot

- Introduces power laws which can be difficult to fit (do not use linear regression). If can be useful if the degree follows a power law but isn't crucial imperically

#### Chapter 7 Paths & walks

- introduction to the different properties of graphs such as cyclic, acyclic, tree etc.

- "You can count the number of connected components in a graph by counting the number of eigenvalues equal to one of its stochastic adjacency matrix. The non-zero entries in the corresponding eigenvectors tell you which nodes are in which connected component" taken from the book

- Mentions strong and weak components (strong abide by the edge direction and weak ignore the edge direction)

#### Chapter 8 Random walk

- Explains random walks and the other types such as non-backtracking random walk

- Here it also mentions the normalized cut problem which aims to cut the minimum amount of edges, it uses the n-1 smallest Laplacian eigenvecters to calculate the solution

#### Chapter 9 Density

- a networks density is defined by number of edges divided by number of total possible edges

- introduces clustering coefficient trasitivity (global, local and average) 

- usually networks have very high clustering

- a clique is a subgraph with density = 1 (which means every node is connected to another) biparte networks have bicliques. The opposite is called an independent set

### Centrality

#### Chapter 10 Shortest paths

- Talks about the different algortihms (BFS,DFS, Dijkstra and floyd-warshall) used to calculate the shortest paths ( connecting two arbitrary nodes in the network using the minimum amount of edges)

- two important connectivity meassures are diameter (Length of the longest shortest path) and average path lenght (average of the shortest paths)

- minimum spanning tree is connecting all the nodes in a network with the minimum sum of the weight, the opposite is called a maximum spanning tree

#### Chapter 11 Node ranking

- Introduces alternative methods to measure the nodes degree of importance ex. Betweenness centrality (used to calculate how many shortest paths would become longer if a node is removed)

- eigenvector centrality such as random walk (used in pagerank), HITS (used for directed graphs)

- introduces Harmonic centrality which is a modified version of closeness centrality and Kcore decomposition (recursively removes nodes with increasing degree of thresholds k times) which can be used for networks with multiple connected components

- you can estimate how centralized a network is by comparing the highest found centrality to the maximum theoretical centrality of a network with the same amount of nodes

### Synthetic graph models

#### Chapter 13 Random graphs

- Introduces random graphs as a way to test our written algorithms

- random graphs have a binominal distribution which is different to real world graphs as their neighbours often have corelation


#### Chapter 14 Understanding network properties

- explaining high clustering and small diameters in the real world by using Watts and Strogatz real world model, and clustering with the cave man graph

- using preferential attachment model, link selection or copying models to explain power law degree distributions (watch out for the preferential attachment models node age correlation)


#### Chapter 15 Generating realistic data

- using the configuration model you can approximate a synthetic network with an arbitrary degree distribution

- mentions several models for data generation (Stochastic block models, GN benchmark, LFR benchmark, kronecker graphs and neural networks)

#### Chapter 16 Evaluating statistical significanse

- Introduces network shuffling as a way to create a null version of your network by doing edge swapping

- you can use the generated networks to test properties of interest and see how statistically significant the observation is by checking the number of standard deviations between the observation and the null average

- Exponential random graphs uses characteristics to predict the presence of an edge between 2 nodes which you use to extract random graphs

### Spreading processes

#### Chapter 17 Epidemics

- introduces the SI, SIS and the SIR model (Susceptible, Infected, Removed) 

#### Chapter 18 Complex contagion

- Goes into details of the models from the previous chapters and expands upon them

#### Chapter 19 Catastrophic failures

- Talks about failure in networks and how it affects different networks such as targeted attacks which is particularly dangerous for power law random networks

### Link prediction

#### Chapter 20 For simple graphs

- Introduces link prediction, finding the most likely connection to appear in the future using theory about the topology of the network

- also mentions alternative methods such as mesoscale structures from the network, find overexpressed graph patterns, katz ranking algorithm, random walk hitting time, stochastic blockmodels and mutual information or use them all together.

#### Chapter 21 For multilayer graphs

-Link prediction for multilater graphs is different as you also need to predict which layer the edge will appear between 2 nodes.

- a simplified version can be done with signed networks since real world networks tend to have a balanced structure, which can be used to predict relationships

- mentions alternative approaches such as status theory. For generalized multilayer link prediction you usually create multilayer generalizations of single layer predictors, with some strategy to aggregate multilayer information

#### Chapter 22 Designing an experiment

- Evaluating your link prediction you need to train and test it ie. split the data into training and test sets

- It is recommended to do cross validation (split the data into 10 blocks and use 1 block as test and the other 9 as training then repeat until all data has been tested)

- It is important to balance the test sets with an equal amount of edges and non-edges as real networks are sparse and can create a link prediction only predicting non-edges and getting a decent result

- the classic evaluation strategy is the ROC curve (true positive rate against false positive), the more AUC (area under the curve) the better prediction peformance

- explaining precision (returning only true positives at the price of missing some), recall (returning all positive results at the price of returning lots of false positives) and the precision recall curves with the objective to maximise the AUC


### The hairball

#### Chapter 23 Bipartite projections

-Relevent for our project since we picked a bipartite network

- Most network algorithms work on unipartite networks so it is recommended to transform a bipartite network to a unipartite network using network projection

- in network projections for bipartite networks one of the node types is picked and connected with the nodes that have a common neighbour of the other node type.

- since bipartite networks  often have broadly distributed degrees, the projections can easily become close to one fully connected clique, which you need a weighting scheme to remove weak components

- weighting sceme could be standard vector distances (cosine, euclidiean, correlation) or more specialized network-aware techniques such as hyperbolic (considering nodes as allocating resources to their neighbors, inversely proportional to the number of neighbors they have)

- "In resource allocation, you also have nodes sending resources, but you take two steps instead of one: you’re not discounting only for the degree of nodes of type one, but also for the degree of nodes of type two." taken from the book chapter 23 summary 5

- it is also possible to do resource allocation with infinite length random walks by looking at the stationary distribution.

- The different techniques can produce very different network topologies

#### Chapter 24 Network backboning

- backboning is the process of removing edges in a network

- When doing backboning you should not establish a threshold and remove all edges with a weight below, since edge weights are distributed broadly and can be correlated in different parts of a network.

- doubly stochastic backboning is a method where you transform the adjacency matrix in a doubly stochastic matrix (which means the rows and coloumns both sum to 1) which breaks the local edge correlation (be wary that it might not always be possible)

- another method is the high-salience skeleton which calculates the shortest path tree for each node and then re-weight the edges using the trees calculated and keep the edges most used. This requires a lot of computation power

- the last methods mentioned is the disparity filter and noise corrected, which create a null expectation of the edge weights and keeps the ones whose weight is higher than the expectation. (the difference being the expectation in disparity filter being node-centric and edge-centric in noise corrected)

#### Chapter 25 Network sampling

- Network sampling is a necessary operation if you have a very large amount of data or if you collect it from an API with high latency where you can only collect 1 node at a time. Sampling is not necessary if you collect a sample made by somebody else.

    - The objective of network sampling is to get a network sample that can represent the whole network to check certain properties of the network, an example could be to check whether or not it has a comparable degree distribution (if it is a power law)

- the different types of network sampling methods can be induced (extract a random sample of nodes/edges and collect all that is attached) or topological (exploring the structure one node at a time)

- methods include BFS (snowball (which imposes a maximum number k of explored neighbors) and forest fire (gives a probability of refusing some edges)), Random walk (metropolis-hastings (haves a probability of refusing nodes with high degrees) and Re-weighted (correcting the statistical properties after the network is collected))

- when collecting data be wary of the edges per second as it can give a false indication of the speed in which data is collected


### Mesoscale 

#### Chapter 26 Homophily

- Homophily/assortativity means that nodes of similar attributes tend to connect to each other

- its meso scale properties can be studied by creating ego networks (pick a node as an ego and only view its connecting neighbors)

- to estimate attribute assortativity you can interpret it as a correlation coefficient taking values from 1 (perfect assortativity) to -1 (perfect disassortativity)

- links lowering homophily connect nodes of different attributes which is good for information spreading (ie. "the strenght of weak ties")

#### Chapter 27 Quantitative Assortativity

- Assortativity works on both qualitative and quantitative attributes

- you can calculate degree assortativity/quantitative assortativity by correlating the attribute values at the endpoint of each edge or correlate the nodes attribute value with the average of its neighbour

- OBS. Graph generators usually do not provide degree assortative netoworks and have to be done afterwards using postprocessing techniques

- introduces the friendship paradox ("my friends have more friends than me" and implies that you are less happy than your friends)


#### Chapter 28 Core-Periphery

- A core-periphery structure is a meso-level organisation of complex networks in 2 parts, one being the core, a set of nodes densely connected. The other being the periphery which has a set of nodes with few connections to the core.

- Models such as the discrete model (penalizing periphery-periphery connections) and continuous model can be used to detect these structures

- Core-periphery structures are ubiquitous (constantly encountered/widespread) and a pure core-periphery structure is incompatible with others such as the notion of communities, in reality however they are co-existing.

- Nestedness in ecology and economics is a classical core-periphery structure for bipartite networks.

#### Chapter 29 Hierachies

- There are multiple meanings of "Hierachies" in networks, examples could be Order hierachy is similar to centrality (sorting the nodes from their importance), nested hierachy which is more similar to communities (grouping nodes teams) and flow hierachy (a structural orginazation where nodes work at different levels and information always flows in one direction from high level to low level (works for directed networks))

- A perfect hierachy cannot have cycles (lower level nodes linking to higher level ones), if they exist you can remove them or calculate the agony it brings to the structure

- The head of a hierachy is the node with highest reach

- Arborescenes are perfect hierachies (directed acyclic graphs with all nodes having an in-degree of 1 except for the head of the hierachy which have 0)

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
