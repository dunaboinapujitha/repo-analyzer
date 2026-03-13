import requests

def get_repo_details(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Repository not found")
        return

    data = response.json()

    name = data["name"]
    description = data["description"]
    stars = data["stargazers_count"]
    forks = data["forks_count"]
    issues = data["open_issues_count"]
    language = data["language"]
    created = data["created_at"]
    size = data["size"]

    print("\n----- Repository Details -----")
    print("Name:", name)
    print("Description:", description)
    print("Language:", language)
    print("Stars:", stars)
    print("Forks:", forks)
    print("Open Issues:", issues)
    print("Created On:", created)
    print("Repository Size:", size, "KB")

    save_report(name, description, language, stars, forks, issues, created, size)


def get_contributors(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    response = requests.get(url)

    if response.status_code != 200:
        print("Could not fetch contributors")
        return

    data = response.json()

    print("\nTop Contributors:")

    for contributor in data[:5]:
        print(contributor["login"], "-", contributor["contributions"], "contributions")


def save_report(name, description, language, stars, forks, issues, created, size):

    with open("repo_report.txt", "w") as file:
        file.write("GitHub Repository Report\n\n")
        file.write(f"Name: {name}\n")
        file.write(f"Description: {description}\n")
        file.write(f"Language: {language}\n")
        file.write(f"Stars: {stars}\n")
        file.write(f"Forks: {forks}\n")
        file.write(f"Open Issues: {issues}\n")
        file.write(f"Created On: {created}\n")
        file.write(f"Size: {size} KB\n")

    print("\nReport saved as repo_report.txt")


repo_url = input("Enter GitHub Repository URL: ")

parts = repo_url.rstrip("/").split("/")
owner = parts[-2]
repo = parts[-1]

get_repo_details(owner, repo)
get_contributors(owner, repo)