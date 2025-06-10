import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_V1_API_ENDPOINT"),
    default_query={"api-version": "preview"}, 
)

response = client.responses.create(
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    input=[
        {"role": "system", "content": "Create a structured event object for a blog post."},
        {"role": "user", "content": "A blog about Azure AI Foundry."}
    ],
    text={
        "format": {
            "type": "json_schema",
            "name": "blog_post",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the blog post"
                    },
                    "date": {
                        "type": "string",
                        "description": "Publication date in YYYY-MM-DD format"
                    },
                    "category": {
                        "type": "string",
                        "description": "The category under which this post is filed"
                    },
                    "tags": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "A list of tags for this post"
                    },
                    "slug": {
                        "type": "string",
                        "description": "URL‐safe identifier for the post"
                    },
                    "author": {
                        "type": "string",
                        "description": "Name of the post’s author"
                    },
                    "summary": {
                        "type": "string",
                        "description": "Short summary or excerpt of the post"
                    },
                    "body": {
                        "type": "string",
                        "description": "Full content of the post (e.g. Markdown)"
                    }
                },
                "required": [
                    "title",
                    "date",
                    "category",
                    "tags",
                    "slug",
                    "author",
                    "summary",
                    "body"
                ],
                "additionalProperties": False
            }
        }
    }
)

blog = json.loads(response.output_text)

print(blog)

# Convert blog dict to markdown string
markdown_content = f"""---
title: "{blog['title']}"
date: {blog['date']}
category: {blog['category']}
tags: {blog['tags']}
slug: {blog['slug']}
author: {blog['author']}
summary: "{blog['summary']}"
---

{blog['body']}
"""

# Write markdown to file named <slug>.md in current folder
filename = f"{blog['slug']}.md"
with open(filename, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_content)
print(f"Markdown file '{filename}' created.")