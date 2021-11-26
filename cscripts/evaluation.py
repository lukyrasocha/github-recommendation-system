# evaluation.py 
# script holding function to evaluate the quality of recommendation based on queried metadata

# last modified     : 26/11/21
# author            : jonas-mika senghaas

import json
import os

from envvars import GITHUB_TOKEN
from github_api import ReposSummary

# expected format for recommendations
"""
metadata = {'luky/na': {'languages': [['Python', 550], ['Java', 220]]}, 
            'jonas-mika/eduml': {'languages': [['Python', 2000]]},
            'ludek/dotfiles': {'languages': [['vim', 220], ['Python', 100]]}
           }

recommend = {'rails/rails': ['technoweenie/restful-authentication']}
"""

def evaluate_recommendation(recommendations, attributes):
    """
    function to evaluate the quality of the recommendation based on metadata.
    reads in underlying datastructure of the recommendation system (a dictionary that 
    for each repo stores a list of n recommended repos, each being stored as a dictionary
    themselves with key being the recommended repo name and values being a dict of the metadata.

    Algorithmic Idea for Evaluation:
    A 'good recommendation' is defined to be a repository that is similar in some instances to 
    the source repository. Thus, the idea is to assign a score of similarity 
    for different features of the recommended repositories, namely for:
    - languages ( len of intersection / length of union of languages for each repo)
    - tags ( len of intersectio / length of union of repos for each repo)

    the score is averaged over the n recommended repository, the per repo score is a weighted
    average. the total score is averaged over all recommendations.
    """
    total_score = 0
    missing_metadata = 0

    n_recommend = len(list(recommendations.values())[0])
    n_repos = len(recommendations)
    n_attributes = len(attributes)

    api = ReposSummary(GITHUB_TOKEN)

    for repo in recommendations: # maybe: subset of repos
        repo_score = 0
        src_res = api.get_relevant_repo_info(repo)

        print(getattr(src_res, 'language'))
        if not src_res.has_meta:
            missing_metadata += 1
            break

        recommend_missing_metadata = 0
        scores = {attribute: 0 for attribute in attributes}

        for recommended in recommendations[repo]:
            trg_res = api.get_relevant_repo_info(recommended)

            if not trg_res.has_meta:
                recommend_missing_metadata += 1
                break

            for attribute in attributes:
                src_attr = getattr(src_res, attribute)
                trg_attr = getattr(trg_res, attribute)
                scores[attribute] = len(src_attr & trg_attr) / len(src_attr | trg_attr)

        # normalise all score
        for score in scores:
            scores[score] /= (n_recommend - recommend_missing_metadata) 

        # normalise summed attributes score and add total score
        total_score += sum(scores.values()) / n_attributes

    # normalise total score and return
    return total_score / (n_repos - missing_metadata)

if __name__ == '__main__':
    print(evaluate_recommendation(recommend, ['language']))
