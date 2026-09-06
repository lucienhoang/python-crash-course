import requests

USERNAME = "lucienhoang"


def get_user_repos(username):
    """Get all public repositories from a given user."""
    url = f"https://api.github.com/users/{username}/repos"
    r = requests.get(url, timeout=10)
    return r


def get_repo_languages(username, language):
    """Get language byte breakdown for a single repository."""
    url = f"https://api.github.com/repos/{username}/{language}/languages"
    r = requests.get(url, timeout=10)
    return r


def main():
    r = get_user_repos(USERNAME)
    print("Status code: ", r.status_code)

    repos = r.json()
    print("Number of repos:", len(repos))
    for repo in repos:
        repo_name = repo["name"]
        lang_response = get_repo_languages(USERNAME, repo_name)

        if lang_response.status_code == 200:
            languages = lang_response.json()
            print(f"\n{repo_name}: {languages}")
        else:
            print(
                f"\n{repo_name}: could not fetch languages (status {lang_response.status_code})."
            )


if __name__ == "__main__":
    main()
