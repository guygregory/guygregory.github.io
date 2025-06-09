Title: Hello World!
Date: 2025-06-09
Status: hidden
Category: Blog
Tags: intro, pelican
Slug: test
Author: Guy Gregory
Summary: A new test

Welcome to my new Pelican blog!

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

![Madejski Stadium Aerial, August 2014](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Madejski_Stadium_aerial%2C_August_2014_%28cropped%29.jpg/500px-Madejski_Stadium_aerial%2C_August_2014_%28cropped%29.jpg)

<a href="https://www.google.com" target="_blank" rel="noopener">Google</a>

<script>
function updateUKTime() {
    const ukTime = new Date().toLocaleTimeString('en-GB', { timeZone: 'Europe/London' });
    document.getElementById('uk-time').textContent = ukTime;
}
setInterval(updateUKTime, 1000);
window.onload = updateUKTime;
</script>

**Current UK Time:** <span id="uk-time"></span>

<iframe width="560" height="315" src="https://www.youtube.com/embed/ceV3RsG946s?si=np6Bl53Pa8sqFmgM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>