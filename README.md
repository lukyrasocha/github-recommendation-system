# :globe_with_meridians: REPOmmend
## Network Analysis Project: Building a Recommendation System from a Bipartite Network

This repository is used to save the progress of the Fall 2021 Network Analysis Project. The goal of this project was to build a recommendation system for github repositories, based on the 2009 GitHub bipartite network, representing User-Repository-Watches (unweighted) relationships. A similar pipeline as used within this project can be applied generically to any bipartite graph, to build a recommendation for either of the two classes.

While the focus of this project was on understanding, applying and argue in favor or against theoretical concepts of network analysis using real-life data, the final product - a recommendation graph (that was statically saved for a max of 5 recommendations) - was  translated into a simple web-app, that can be visited via the following link:

:arrow_forward: **[https://na-project.netlify.app/](https://na-project.netlify.app/)**

# Contributers

<table>
  <tr>
    <td align="center"><a href="https://github.com/LudekCizinsky"><img src="https://github.com/LudekCizinsky.png?size=50" width="100px;" alt=""/><br /><sub><b>Ludek Cizinsky</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/jonas-mika"><img src="https://github.com/jonas-mika.png?size=50" width="100px;" alt=""/><br /><sub><b>Jonas-Mika Senghaas</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/lukyrasocha"><img src="https://github.com/lukyrasocha.png?size=50" width="100px;" alt=""/><br /><sub><b>Lukas Rasocha</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/louisbrandt"><img src="https://github.com/louisbrandt.png?size=50" width="100px;" alt=""/><br /><sub><b>Louis Brandt</b></sub></a><br /></td>
  </tr>
</table>


# Get started

## Virtual Environment (Dependencies)

The project was (excluding the web-app) entirely written in `Python` and makes use of several external libraries. If you want to run the scripts and notebooks yourself, it is recommened to create a virtual environment (using the python environment manager) of you choice and then install all dependencies of it from the `requirements.txt`. Follow the following steps for create a stadard python `venv`:

1. Create a virtual environemnt: `python3 -m venv [name of venv]`

2. Activate the venv using: `source [name of env]/bin/activate`. You can decativate using the command `deactivate`

3. Update `pip`: `pip install --upgrade pip`

4. Install all dependencies: `pip install -r <path/to/requirement.txt>`

## Github API

We use the public GitHub API to dynamically query additional metadata to be displayed in our web-app and to gain additional metadata for our recommendation system. While the API has free access, using an API token increases the number of API requests to 5000/hour. If you want to run the scripts yourself, you must create your own free, GitHub API token. Follow the following steps:

1. Visit your personal [GitHub Token Settings](https://github.com/settings/tokens)
2. Create a new personal token and set the scope to `public_repo`.
3. Copy the token and save it into a python file in the following location `csripts/envvars.py`. Format your file as follows:

	```
	GITHUB=TOKEN=[your_token]
	```
4. The file is automatically ignored by `.gitignore`.

## Folder structure
Last Checked: 29. November 23:55
```
.
├── .gitignore
├── README.md
├── compare_networks.ipynb
├── cscripts
│   ├── __init__.py
│   ├── backboning.py
│   ├── evaluation.py
│   ├── github_api.py
│   ├── handle_timeout.py
│   ├── metrics.py
│   ├── plotting.py
│   ├── projections.py
│   ├── recommendation.py
│   ├── similarity.py
│   └── summarise.py
├── data
│   ├── figures
│   │   ├── component_size_vs_count.jpg
│   │   ├── dd_bipartite_ccdf_loglog.jpg
│   │   ├── dd_bipartite_count.jpg
│   │   ├── dd_bipartite_count_loglog.jpg
│   │   ├── most_used_lang.jpg
│   │   ├── one_giant_component.png
│   │   ├── power_law_fit_bipartite.jpg
│   │   ├── projections_weight_dist.jpg
│   │   ├── screenshot_132559.png
│   │   ├── screenshot_133054.png
│   │   └── weight_dist_simple_proj.jpg
│   ├── graph_summaries
│   │   ├── backboned_projections
│   │   │   ├── heats
│   │   │   │   ├── disparity_filter
│   │   │   │   │   ├── assets
│   │   │   │   │   │   ├── ccdf_degree_distribution.jpg
│   │   │   │   │   │   ├── degree_distribution.jpg
│   │   │   │   │   │   └── edge_weight_distribution.jpg
│   │   │   │   │   └── disparity_filter_0.95.md
│   │   │   │   └── noise_corrected
│   │   │   │       ├── assets
│   │   │   │       │   ├── ccdf_degree_distribution.jpg
│   │   │   │       │   ├── degree_distribution.jpg
│   │   │   │       │   └── edge_weight_distribution.jpg
│   │   │   │       └── noise_corrected_0.95.md
│   │   │   ├── hyperbolic
│   │   │   │   ├── disparity_filter
│   │   │   │   │   ├── assets
│   │   │   │   │   │   ├── ccdf_degree_distribution.jpg
│   │   │   │   │   │   ├── degree_distribution.jpg
│   │   │   │   │   │   └── edge_weight_distribution.jpg
│   │   │   │   │   └── disparity_filter_0.95.md
│   │   │   │   └── noise_corrected
│   │   │   │       ├── assets
│   │   │   │       │   ├── ccdf_degree_distribution.jpg
│   │   │   │       │   ├── degree_distribution.jpg
│   │   │   │       │   └── edge_weight_distribution.jpg
│   │   │   │       └── noise_corrected_0.95.md
│   │   │   ├── jaccard
│   │   │   │   ├── disparity_filter
│   │   │   │   │   ├── assets
│   │   │   │   │   │   ├── ccdf_degree_distribution.jpg
│   │   │   │   │   │   ├── degree_distribution.jpg
│   │   │   │   │   │   └── edge_weight_distribution.jpg
│   │   │   │   │   └── disparity_filter_0.95.md
│   │   │   │   └── noise_corrected
│   │   │   │       ├── assets
│   │   │   │       │   ├── ccdf_degree_distribution.jpg
│   │   │   │       │   ├── degree_distribution.jpg
│   │   │   │       │   └── edge_weight_distribution.jpg
│   │   │   │       └── noise_corrected_0.95.md
│   │   │   ├── probs
│   │   │   │   ├── disparity_filter
│   │   │   │   │   ├── assets
│   │   │   │   │   │   ├── ccdf_degree_distribution.jpg
│   │   │   │   │   │   ├── degree_distribution.jpg
│   │   │   │   │   │   └── edge_weight_distribution.jpg
│   │   │   │   │   └── disparity_filter_0.95.md
│   │   │   │   └── noise_corrected
│   │   │   │       ├── assets
│   │   │   │       │   ├── ccdf_degree_distribution.jpg
│   │   │   │       │   ├── degree_distribution.jpg
│   │   │   │       │   └── edge_weight_distribution.jpg
│   │   │   │       └── noise_corrected_0.95.md
│   │   │   └── simple_weight
│   │   │       ├── disparity_filter
│   │   │       │   ├── assets
│   │   │       │   │   ├── ccdf_degree_distribution.jpg
│   │   │       │   │   ├── degree_distribution.jpg
│   │   │       │   │   └── edge_weight_distribution.jpg
│   │   │       │   └── disparity_filter_0.95.md
│   │   │       └── noise_corrected
│   │   │           ├── assets
│   │   │           │   ├── ccdf_degree_distribution.jpg
│   │   │           │   ├── degree_distribution.jpg
│   │   │           │   └── edge_weight_distribution.jpg
│   │   │           └── noise_corrected_0.95.md
│   │   ├── karate
│   │   │   ├── assets
│   │   │   │   ├── ccdf_degree_distribution.jpg
│   │   │   │   ├── degree_distribution.jpg
│   │   │   │   └── edge_weight_distribution.jpg
│   │   │   ├── karate.md
│   │   │   └── karate_plain.md
│   │   ├── load_md.ipynb
│   │   ├── original_bipartite
│   │   │   ├── assets
│   │   │   │   └── degree_distribution.jpg
│   │   │   ├── original_bipartite.md
│   │   │   └── original_bipartite_plain.md
│   │   └── projections
│   │       ├── heats
│   │       │   ├── assets
│   │       │   │   ├── ccdf_degree_distribution.jpg
│   │       │   │   ├── degree_distribution.jpg
│   │       │   │   └── edge_weight_distribution.jpg
│   │       │   └── heats.md
│   │       ├── hyperbolic
│   │       │   ├── assets
│   │       │   │   ├── ccdf_degree_distribution.jpg
│   │       │   │   ├── degree_distribution.jpg
│   │       │   │   └── edge_weight_distribution.jpg
│   │       │   └── hyperbolic.md
│   │       ├── jaccard
│   │       │   ├── assets
│   │       │   │   ├── ccdf_degree_distribution.jpg
│   │       │   │   ├── degree_distribution.jpg
│   │       │   │   └── edge_weight_distribution.jpg
│   │       │   └── jaccard.md
│   │       ├── probs
│   │       │   ├── assets
│   │       │   │   ├── ccdf_degree_distribution.jpg
│   │       │   │   ├── degree_distribution.jpg
│   │       │   │   └── edge_weight_distribution.jpg
│   │       │   └── probs.md
│   │       └── simple_weight
│   │           ├── assets
│   │           │   ├── ccdf_degree_distribution.jpg
│   │           │   ├── degree_distribution.jpg
│   │           │   └── edge_weight_distribution.jpg
│   │           └── simple_weight.md
│   ├── metadata
│   │   ├── backboning.txt
│   │   ├── projections.txt
│   │   ├── projections_backboning_summaries.txt
│   │   └── projections_summaries.txt
│   ├── raw
│   │   ├── data.txt
│   │   ├── lang.txt
│   │   ├── repos.txt
│   │   └── test.txt
│   ├── recommendations
│   │   └── simple_weight
│   │       └── single_recommend5.json
│   ├── sampled
│   │   ├── degree-distribution.png
│   │   ├── desc_of_the_sample.txt
│   │   ├── jaccard_sample.csv
│   │   ├── one_giant_component.png
│   │   ├── screenshot_132559.png
│   │   └── screenshot_133054.png
│   └── transformed
│       ├── data.txt
│       ├── metadata.json
│       └── mismatches.csv
├── main.ipynb
├── other
│   ├── community_discovery.py
│   ├── looking_for_dataset.ipynb
│   ├── metadata.py
│   └── old_code_from_main.ipynb
├── project_info
│   ├── GithubContestInfo.txt
│   ├── TODO.md
│   └── reading_notes.md
├── requirements.txt
└── webapp
    ├── README.md
    ├── package-lock.json
    ├── package.json
    ├── public
    │   ├── data
    │   │   ├── naive_recommend.json
    │   │   ├── search_depth.json
    │   │   └── test2.json
    │   ├── favicon.ico
    │   ├── github-icon.png
    │   ├── index.html
    │   ├── manifest.json
    │   └── robots.txt
    └── src
        ├── App.js
        ├── components
        │   ├── Repo.js
        │   └── Search.js
        ├── index.css
        ├── index.js
        └── setupTests.js
```
