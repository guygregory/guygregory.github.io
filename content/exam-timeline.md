Title: AI-powered exam dashboard
Date: 2025-07-23
Category: Blog
Tags: github, mslearn, azure
Slug: exam-timeline
Author: Guy Gregory
Summary: How to build yourself a free, AI-powered Microsoft exam dashboard, using Python, GitHub Actions, GitHub Models, and Azure Static Web Apps

<a href="https://exams.guygregory.com"><img width="2217" height="1503" alt="image" src="https://github.com/user-attachments/assets/3aef88b7-aa2e-4d25-9d3b-b0d76bdd7766" /></a>


After over 20 years spent earning Microsoft certifications, and with my recent success on the [GH-900](https://learn.microsoft.com/credentials/certifications/github-foundations/) exam, I started reflecting on just how far I’ve come. That’s when the idea for [`exam-timeline`](https://github.com/guygregory/exam-timeline) was born. I wanted a fun, interactive way to visualise my certification journey and to try building a simple AI app that used LLMs from [GitHub Models](https://gh.io/models).

The initial prototype came together in under half an hour of vibe-coding, thanks to [GitHub Copilot](https://github.com/copilot) for the coding assist and using the Free tier of [Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/overview) for the super-quick deployment and tight GitHub integration. From there, I spent a few more hours automating the extraction of exam data, and wiring up [GitHub Actions](https://docs.github.com/en/actions) - mainly delegating the hard work to the [GitHub Coding Agent](https://docs.github.com/en/copilot/how-tos/agents/copilot-coding-agent). A few days later, I added the "AI recommendation" feature, using a few lines of Python. The end result is a project that’s both personal and practical, with a workflow that anyone can replicate.

### How it works - AI-powered recommendation via GitHub Models
Let's start with the the element I'm personally most excited about - The AI recommendation to recommend the 'next logical exam'.

- After the transcript is downloaded from Microsoft Learn, the workflow calls [a Python script](https://github.com/guygregory/exam-timeline/blob/main/ai_exam_recommender.py), and this inserts the learner's transcript into the user prompt of the LLM.
- The system prompt guides the LLM to make a recommendation for a next logical exam, and to avoid choosing an exam that the learner has already completed.
- The script uses OpenAI's gpt-4o model, which is hosted by GitHub Models (on Azure AI)
- Because this script is called directly from GitHub Actions, [auth works seamlessly](https://docs.github.com/en/github-models/use-github-models/integrating-ai-models-into-your-development-workflow#using-ai-models-with-github-actions). I only had to add `models: read` into the `permissions` section of the workflow for it to work.
- In order to return a consistent response, [Structured Outputs](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/structured-outputs?tabs=python-secure%2Cdotnet-entra-id&pivots=programming-language-python) are used with the [enum type](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/structured-outputs?tabs=python-secure%2Cdotnet-entra-id&pivots=programming-language-python#supported-schemas-and-limitations) to only return an answer from the [list of prioritised exams](https://github.com/guygregory/exam-timeline/blob/main/priority_ARB_exams.csv).
- Leverages the [GitHub Models quota, included in the GitHub Copilot plans (including free)](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits)
- The output of this script is a JSON object which includes the recommendation: `{"exam_code":"AZ-305"}`, which is then inserted into the button in [`index.html`](https://github.com/guygregory/exam-timeline/blob/main/index.html)

### How it works - Data extraction from Microsoft Learn
To extract the exam information, the project uses a [Python script](https://github.com/guygregory/exam-timeline/blob/main/passed_exams.py) to download the Microsoft certification transcript, based on the [Transcript sharing code](https://learn.microsoft.com/users/me/transcript).

> **Disclaimer:** The use of the Microsoft Learn API in this way is **not officially supported or documented**, and while suitable for a simple hobby project, is **not appropriate for a production application**. Future API availability is not guaranteed. For commercial integrations, please contact your Microsoft representative.

You can run this script independently if you just want a quick export for your own records or to feed into another tool. But if you’re feeling ambitious, you can [clone the entire repo](https://github.com/guygregory/exam-timeline), customise it, and deploy your own version in minutes. The daily automation fetches your latest transcript, stores it in the repo as a .csv file, which feeds a simple Plotly-powered (JS) dashboard. Here's how it gets the transcript from Microsoft Learn:

```python
API_ENDPOINT_TEMPLATE = "https://learn.microsoft.com/api/profiles/transcript/share/{share_id}?locale={locale}"

url = API_ENDPOINT_TEMPLATE.format(share_id=share_id, locale=locale)
headers = {
     # Provide a User‑Agent to avoid potential filtering of generic requests
     "User-Agent": "Mozilla/5.0 (compatible; MSFTTranscriptFetcher/1.0)"
}
response = requests.get(url, headers=headers)
response.raise_for_status()
return response.json()
```
alternatively, using cURL
```bash
curl -f -H "User-Agent: Mozilla/5.0 (compatible; MSFTTranscriptFetcher/1.0)" "https://learn.microsoft.com/api/profiles/transcript/share/${share_id}?locale=${locale}"
```

If you want to try this yourself, just remember: your Microsoft transcript may contain sensitive personal information, like your name and email address. Thankfully, [Microsoft Learn](https://learn.microsoft.com/users/me/transcript) lets you adjust this before sharing anything publicly.

<img width="756" height="452" alt="image" src="https://github.com/user-attachments/assets/ccaca094-8d3f-41e5-9095-1d145bb80559" />

Spending time on this project really helped me deepen my knowledge around GitHub Actions, and especially how they can be integrated with GitHub Models for ["Continuous AI"](https://githubnext.com/projects/continuous-ai/). It also made me consider how in future, we might AI-enable data like this using broadly adopted standards like MCP. Big thanks to a couple of colleagues for their input and advice on this project, namely fellow PSA, Bojan Vrhovnik and Allison Waldmann from the Microsoft Learn platform team.

Finally, if you're looking to experiment with Python, GitHub Actions, GitHub Models, and Azure Static Websites, I hope my little `exam-timeline` project inspires you to take pride in your learning journey. Contributions welcome!
