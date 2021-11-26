# metadata.py 
# script that includes functions to generate the metadata dict used for evaluation and within the webapp

# last modified     : 26/11/21
# author            : jonas-mika senghaas

import os
import json

def generate_metadata(repos, filepath='.', name='untitled'):
    """
    Generate metadata dictionary with key=reponame and value=all relevant metadata both
    from raw data and queried github api. combines raw metadata and queried metadata from
    github that are both statically saved in one metadata set for a give set of repos 
    of interest (to reduce file size) and outputs as a json file to the specified path.
    """
    # make savepath if not existent
    os.makedirs(filepath) if not os.path.exists(filepath) else None

    # transform array of repos into a set for fast querying
    REPOS = set(repos)
    METADATA = {}

    # iterate over raw metadata and add relevant information
    with open('../data/transformed/metadata.json', 'r') as infile:
        data = json.load(infile)

        for values in data.values():
            name = values.pop('repo_name')
            if name in REPOS:
                METADATA[name] = values

    # iterate over queried github metadata and add relevant information
    with open('../data/tranformed/github_metadata.json', 'r') as infile:
        data = json.load(infile)

        for 


    # write to json file
    with open(f'{filepath}/{name}.json', 'w') as outfile:
        json.dump(METADATA, outfile)
