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

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

    plot_dict = {
        "value": repo_dict["stargazers_count"],
        "label": repo_dict["description"],
    }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS("#333366", base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1200

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file("files/python_repos.svg")
