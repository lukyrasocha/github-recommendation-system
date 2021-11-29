# General tasks

## Other

- [ ] adjust folder structure (ie. no need for subfolder `edge_list_format` in `projections`), also in notebook
- [ ] cleanup `main.ipynb` and add descriptions wherever necessary. all results/ plots/ graphs should be produced from main (and only 		use helperfunctions from `cscripts`)

## Bug fixes

- [x] Run backboning and summary again for props and heats (now directed graphs)
- [ ] When running summaries, cancel showing generated graphs

## Figures

- [ ] Add better structure (folder and name wise) to the figures folder --> must adjust code in main

## Questions to ask

- [x] How to deal with too many components in the network? (See slack)
- [ ] p-value in DF and NC (how does it work, how do we use it, dont we simply
      erase edges that are below node's average weight?)
- [ ] Why do we get max for heats and probs 0.5 in terms of weight?

# Building Recommendation Graph 
## Network Selection and basic summary

- [x] Choose a proper network to work on
- [x] Do basic summary:
  - Where the network is from
  - What it represents
  - What are the nodes attributes
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

## Network projection

- [x] Apply following methods to project our network onto repositories:
  - Simple weight
  - Jaccard
  - Probs
  - Heats
  - Hyperbolic
  - Vectorised projections (e.g. Cosine) - Implemented but due to performance reasons excluded it
- [x] Add description/comment to the above defined methods

## Network backboning

- [x] Do network backboning using following methods:

  - Disparity filter
  - Noise corrected filter
  - Double Stochastic - attempted but did not converge

- [x] Save all backboned graphs for the later use

## Analysis of Metrics and Visualising Unipartite Networks (Projection/ Backboned Networks)

- [x] Add further plots to generated markdown (ccdf of dd, power law fit, distribution
      of edge weights, distribution of cc sizes, ...)
- [x] Find way to automatically convert MD into well-formatted PNG, PDF (to load
      file into Jupyter while displaying plots) / alternatively: find out why iPython's
      display(Markdown) does not show the produced local plots

# Recomendation algorithm(s)

## Algorithm 1: Naive Neighborhood Approach

The final recommendation for a single repository is the k neighbors connected to
the queried repository with highest edge weight (descending order).

Runtime: O(log(k)\*k for k being degree of node n for all n in N)

- [x] Implement the method

## Algorithm 2: Search Depth Approach

- [x] Implement the method (VERY NAIVELY SO FAR)
- [ ] improve method (low priority)

## Algorithm 3: LCC

Similar to search depth with p=2 algorithm, but only takes those neighbor neighbors
into consideration that are within the intersection of at least two neighbors of the source node. The edge weight of such LCC (closing triangle) nodes might be computed as a projection
from the source node to the LCC node.

- [ ] Implement the method (low priority)

# Evaluation of Recommendation System

- [x] map metadata from github api to the final recommendation system
	  -> failed on tags because of lack of tags (infeasible to compute)
- [x] ran evaluation on different final recommendation graph and both recommendation algorithms
- [ ] run evluation on all possible recommendation graphs 
- [ ] interpret results (NOTE: no ground truth, higher score not necessarily better recommendation, just higher language similarity)


# Visualisation

- [x] Network Visualisation using Gephi

# Webapp

- [x] Random Search Button
- [x] Add relevant metadata using GithubApi for recommended repos
- [ ] Fix weird wrapping of long titles
- [ ] find more relevant metadata
- [ ] maybe also display metadata of repo that was queried
- [ ] render a loading symbol while metadata is fetching
- [ ] hide github api token

# Presentation

- [ ] slides about projections methods (and how we arrive at the conclusion to use `HeatS`) 
- [ ] slides about backboning methods (and how we arrive at the conclusion to use `noise_corrected`)
- [ ] slides about recommendation algorithms ()
- [ ] slides about evaluation system and their interpretation ()

*Note: Show all these steps on small test graphs that represent our data*

# Future Ideas 

- [ ] Link prediction if we can predict less than required n repositories
      (for around 10% of our nodes)