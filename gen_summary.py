import json

with open("blog_post.json", "r") as file:
    data = json.load(file)

posts_summary = []
for post in data["posts"]:
    post_summary = {
        "title": post["title"],
        "author": post["author"],
        "number_of_comments": len(post["comments"]),
    }
    posts_summary.append(post_summary)

with open("posts_summary.json", "w") as file:
    json.dump({"posts_summary": posts_summary}, file, indent=4)
