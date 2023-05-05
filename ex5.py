import httpx

#user = "github"
user = "TymonBar"

response = httpx.get(f"https://api.github.com/users/{user}/repos")
repos = response.json()
print(repos)
