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
    repos = r.json()

    total_byte = {}

    for repo in repos:
        repo_name = repo["name"]
        lang_response = get_repo_languages(USERNAME, repo_name)

        if lang_response.status_code == 200:
            languages = lang_response.json()
            for language, byte_count in languages.items():
                total_byte[language] = total_byte.get(language, 0) + byte_count

    # Calculating percentages.
    grand_total = sum(total_byte.values())
    percentage = {
        language: (byte_count / grand_total) * 100
        for language, byte_count in total_byte.items()
    }

    # Sort by percentage, descending.
    sorted_langs = sorted(percentage.items(), key=lambda item: item[1], reverse=True)

    print("\nLanguage breakdown across all repos:")
    for language, pct in sorted_langs:
        print(f"{language}: {pct:.1f}%")


if __name__ == "__main__":
    main()
