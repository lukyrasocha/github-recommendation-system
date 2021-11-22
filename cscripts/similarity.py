# Utility functions
import backboning  # michele
import github_api

# Standard libraries
import pandas as pd
import networkx as nx
import json
from pathlib import Path
from datetime import date


class Similarity:

    def __init__(self, path, thrs, meta_path) -> None:
        self.path = path
        self.thrs = thrs
        self.meta_path = meta_path
        self.G = None

    def load_graph(self):

        # Load given network and filter our irrelevant edges
        df = backboning.thresholding(pd.read_csv(self.path), self.thrs)

        # Load it into networkX graph
        self.G = nx.convert_matrix.from_pandas_edgelist(
            df, source="src", target="trg", edge_attr="nij")

    def add_meta_data(self):

        # load metadata
        with open(self.meta_path, "r") as fp:
            metadata = json.load(fp)

        # add metadata to graph nodes
        for repo_id, vals in metadata.items():
            to_add = {repo_id: vals}
            nx.set_node_attributes(self.G, to_add, "metadata")

    def get_node_id(self, node_name):
        """
        Returns node_id based on the provided node name.
        :node_name: str
        :return: str
        """

        return [key for key, info in dict(self.G.nodes).items() if "metadata" in info and info["metadata"]["repo_name"] == node_name][0]

    def naive_approach(self, how_many, repo_name):
        """

        Algorithm
        ---
        Find N most similar repositories based on the weight of the connections. The higher the better.

        Attributes
        ---
        :how_many: int (> 0), how many repos do you want to return
        :repo_name: str, for which repository do you want to find most similar repositories ([user_name/repo_name])
        :return: None
        """

        # Get top neighbors using a naive approach
        top_edges = sorted([edge for edge in self.G.edges(self.get_node_id(repo_name), data=True)],
                           reverse=True,
                           key=lambda edge: edge[-1]["nij"])[:how_many]

        # Get the top repo names
        top_repo_names = [self.G.nodes[edge[1]]["metadata"]
                          ["repo_name"] for edge in top_edges]

        # Define where to save the summary
        filename = date.today().strftime("summmary_%d_%m_%y-%H:%M:%S")
        folder_path = '../data/recommend_summary/naive/'

        # Check if path exists, if not, create the missing repos
        path = Path(f"{folder_path}{filename}")
        path.parent.mkdir(parents=True, exist_ok=True)

        # Create a md summary
        github_api.ReposSummary(top_repo_names, filename, folder_path)


if __name__ == "__main__":
    pass
