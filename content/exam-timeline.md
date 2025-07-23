Title: Visualising Microsoft exams
Date: 2025-07-23
Category: Blog
Tags: github, mslearn, azure
Slug: exam-timeline
Author: Guy Gregory
Summary: How to build yourself a free automated Microsoft exam dashboard, using Python, GitHub Actions, and Azure Static Web Apps

<a href="https://exams.guygregory.com" target="_blank" rel="noopener noreferrer"><img width="1802" height="723" alt="image" src="https://github.com/user-attachments/assets/4f00d296-6e40-45fe-a6b1-1b4354264d7f"/></a>

After over 20 years spent earning Microsoft certifications, and with my recent success on the GH-900 exam—I started reflecting on just how far I’ve come. That’s when the idea for [`exam-timeline`](https://github.com/guygregory/exam-timeline) was born. I wanted a fun, interactive way to visualise my certification journey and maybe inspire others who are on a similar path. There’s something satisfying about seeing all those milestones lined up, and I thought: why not make it easy for anyone to do the same?

The initial prototype came together in under half an hour of vibe-coding, thanks to GitHub Copilot for the coding assist and Azure Static Websites for the super-quick deployment and GitHub integration. From there, I spent a few more hours automating the access to exam data, and wiring up GitHub Actions - mainly delegating the hard work to the GitHub Coding Agent. The end result is a project that’s both personal and practical, with a workflow that anyone can replicate.

Here’s how it all works: at its core, the project uses a [Python script](https://github.com/guygregory/exam-timeline/blob/main/passed_exams.py) to download your Microsoft certification transcript, based on your [Transcript sharing code](https://learn.microsoft.com/users/me/transcript). You can run this script independently if you just want a quick export for your own records or to feed into another tool. But if you’re feeling ambitious, you can [clone the entire repo](https://github.com/guygregory/exam-timeline), customise it, and deploy your own exam timeline website in minutes. The automation pipeline fetches your latest transcript, updates the timeline, and pushes the changes live with minimal fuss.

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

If you want to try this yourself, just remember: your Microsoft transcript may contain sensitive personal information, like your name and email address. Luckily, Microsoft Learn lets you adjust this before sharing anything publicly.

<img width="756" height="452" alt="image" src="https://github.com/user-attachments/assets/ccaca094-8d3f-41e5-9095-1d145bb80559" />

Whether you’re looking to track your own certification milestones, show off your progress, or just experiment with Python, GitHub Actions, and Azure Static Websites, I hope my fun `exam-timeline` inspires you to take pride in your learning journey. Contributions welcome - let’s celebrate our wins together!
