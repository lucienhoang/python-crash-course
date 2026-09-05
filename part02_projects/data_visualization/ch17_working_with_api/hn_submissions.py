from operator import itemgetter

import pygal
import requests
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

# Make an API call and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url, timeout=10)
print("Status code:", r.status_code)


# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json"
    submission_r = requests.get(url, timeout=10)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        "title": response_dict.get("title", "No title"),
        "link": "https://news.ycombinator.com/item?id=" + str(submission_id),
        "comments": response_dict.get("descendants", 0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

# for submission_dict in submission_dicts:
#     print("\nTitle:", submission_dict["title"])
#     print("Discussion link:", submission_dict["link"])
#     print("Comments:", submission_dict["comments"])

names, plot_dicts = [], []
for submission_dict in submission_dicts:
    names.append(submission_dict["title"])

    plot_dict = {
        "value": submission_dict["comments"],
        "xlink": submission_dict["link"],
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
chart.title = "Most-Active Discussions on Hacker News"
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file("files/hn_discussions.svg")
