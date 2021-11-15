import requests
from envvars import GITHUB_TOKEN
from datetime import date
from time import time
import os
import sys

local_path = os.path.dirname(os.path.realpath(__file__))
if local_path not in sys.path:
    sys.path.append(local_path)


class Markdown:

    def __init__(self) -> None:
        self.header = f"# Repository overview\nCreated: {date.today().strftime('%d/%m/%y')}\n\nComputation Time: [comp_time] sec\n"
        self.content = f"""{self.header}\n"""

    def add_section_title(self, title):
        self.content += f"## {title}\n---\n"

    def add_repo_section(self, title, repo):

        self.add_section_title(title)

        if repo:
            self.content += f"""**Description**\n\n{repo.description}\n\n**Homepage**\n\n{repo.homepage}\n\n**Key highlights**\n\n- Number of watches: {repo.watchers_count}\n\n- Number of forks: {repo.forks_count}\n\n- Star gazers count: {repo.stargazers_count}\n\n- Open issues count: {repo.open_issues_count}\n\n- Topics: {repo.topics}\n\n- Has a wiki: {repo.has_wiki}\n\n- Language: {repo.language}\n\n"""
        else:
            self.content += """An error occured when fetching data from api.\n"""


class Repo:

    def __init__(self, data) -> None:
        self.name = data.get("name")
        self.description = data.get("description")
        self.forks_count = data.get("forks_count")
        self.stargazers_count = data.get("stargazers_count")
        self.watchers_count = data.get("watchers_count")
        self.open_issues_count = data.get("open_issues_count")
        self.topics = data.get("topics")
        self.has_wiki = data.get("has_wiki")
        self.language = data.get("language")
        self.homepage = data.get("homepage")


class GithubApi:

    def __init__(self, token) -> None:
        self.token = token

    def get_repo_data(self, repo_name):
        """
        Returns raw repo metda data.
        :repo_name: [owner_name]/[actual_repo_name], str
        :return: dict or None (in vase of a problem)
        """
        print("="*10)
        print(f"Fetching data from Github API for: {repo_name}\n")
        # Define parameters
        owner, repo = repo_name.split("/")

        # Define query
        query_url = f"https://api.github.com/repos/{owner}/{repo}"

        # Define headers
        headers = {'Authorization': f'token {GITHUB_TOKEN}'}

        # Send a request
        r = requests.get(query_url, headers=headers)

        # Return proper response
        if r.status_code == 200:
            print(self.get_error_response(r.status_code))
            print("="*10)
            return r.json()

        else:
            print(self.get_error_response(r.status_code))
            print("="*10)
            return None

    def get_error_response(self, status_code):
        """
        Returns an appropriate response based on provided status_code.
        :status_code: int
        :return: str  
        """

        if status_code == 401:
            return "Access denied. Probably invalid token."
        elif status_code == 200:
            return "Request successful."
        else:
            return "Unknown error."


class ReposSummary(GithubApi):

    def __init__(self, repositories, name, path, token=GITHUB_TOKEN) -> None:

        # Inherit from the parent class
        super().__init__(token)

        # Define this class' properties
        self.repositories = repositories
        self.path = path  # where to save the summary
        self.name = name

    def generate_summary(self):

        print("="*10)
        print("Started summary generation")
        print("="*10 + "\n")

        # Measure the computation
        start = time()

        # Save the data to a string
        M = Markdown()

        for repo_name in self.repositories:

            # Fetch data from API
            repo = self.get_relevant_repo_info(repo_name)

            # Add it to the markdown
            M.add_repo_section(repo_name, repo)

        end = time()

        # Add computational time
        M.content = M.content.replace(
            "[comp_time]", f"{round(end - start, 2)}")

        # Save it
        with open(f'{self.path}/{self.name}.md', 'w') as outfile:
            outfile.write(M.content)

    def get_relevant_repo_info(self, repo_name):
        """
        Returns selected info about repo.
        :repo_name: str
        :return: None or Repo object
        """

        # Get raw data
        raw_data = self.get_repo_data(repo_name)
        if not raw_data:
            return None

        # Select relevant data
        r = Repo(raw_data)

        return r
