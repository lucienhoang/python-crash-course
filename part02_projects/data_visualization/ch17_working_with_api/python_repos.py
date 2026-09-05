import pygal
import requests
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)
# Status code: 200

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict["total_count"])

# Explore information about the repositories.

# print(response_dict.keys())
# dict_keys(['total_count', 'incomplete_results', 'items'])

repo_dicts = response_dict["items"]
print("Repositories returned:", len(repo_dicts))

# Examine the first repository.
# repo_dict = repo_dicts[0]

# print("\nKey:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print("\nName:", repo_dict["name"])
#     print("Owner:", repo_dict["owner"]["login"])
#     print("Starts:", repo_dict["stargazers_count"])
#     print("Repository:", repo_dict["html_url"])
#     print("Description:", repo_dict["description"])

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

# Make visualization.
my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names

chart.add("", stars)
chart.render_to_file("files/python_repos.svg")
