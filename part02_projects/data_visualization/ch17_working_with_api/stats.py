import requests

USERNAME = "lucienhoang"


def get_user_repos(username):
    """Get all public repositories from a given user."""
    url = f"https://api.github.com/users/{username}/repos"
    r = requests.get(url, timeout=10)
    return r


def main():
    r = get_user_repos(USERNAME)
    print("Status code: ", r.status_code)

    repos = r.json()
    print("Number of repos:", len(repos))
    for repo in repos:
        print("-", repo["name"])


if __name__ == "__main__":
    main()
