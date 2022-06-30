import requests

blogs = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
print(blogs)