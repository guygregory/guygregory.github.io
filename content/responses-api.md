Title: Responses API on Azure OpenAI
Date: 2025-03-11
Category: Blog
Tags: azureai, openai
Slug: responses-api
Author: Guy Gregory
Summary: Responses API combines the simplicity of Chat Completions with the tool use and state management of the Assistants API.

The Responses API is a new stateful API from OpenAI. It brings together the best capabilities from the chat completions and assistants API in one unified experience. The Responses API also adds support for the new computer-use-preview model which powers the Computer use capability.

I've shared some basic code samples on my [GitHub repo](https://aka.ms/ResponsesAPI) for those who want to get started using Responses API on Azure OpenAI:

Responses API GitHub repo:<br>
[https://aka.ms/ResponsesAPI](https://aka.ms/ResponsesAPI)

Microsoft Learn Documentation:<br>
[https://aka.ms/ResponsesAPI/Docs](https://aka.ms/ResponsesAPI/Docs)

Announcement blog post:<br>
[https://azure.microsoft.com/blog/announcing-the-responses-api-and-computer-using-agent-in-azure-ai-foundry/](https://azure.microsoft.com/blog/announcing-the-responses-api-and-computer-using-agent-in-azure-ai-foundry/)

Request access to the computer-use-preview model:<br>
[https://aka.ms/oai/cuaaccess](https://aka.ms/oai/cuaaccess)

Here's a basic example from the [repo](https://aka.ms/ResponsesAPI):

```python
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key = os.environ["AZURE_OPENAI_API_KEY"],  
    api_version = os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint = os.environ["AZURE_OPENAI_API_ENDPOINT"]
    )

response = client.responses.create(
    model=os.environ["AZURE_OPENAI_API_MODEL"],
    input="Tell me a joke."

)

print(response.output_text)
```
