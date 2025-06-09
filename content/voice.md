Title: Function calling with voice
Date: 2024-10-18
Category: Blog
Tags: azureai, voice
Slug: function-calling-voice
Author: Guy Gregory
Summary: Using Realtime API with gpt-4o to access tools

Last week, after presenting the new Realtime API for speech and audio in Azure OpenAI Service, a Microsoft partner asked me whether it's possible to integrate external tools and services.

The answer? Absolutely! In fact, our public [VoiceRAG demo](https://github.com/Azure-Samples/aisearch-openai-rag-audio) itself uses function calling for Azure AI Search integration, and it's relatively easy to describe your own custom functions (using natural language).

For my own learning, I thought I'd try writing a couple of custom functions myself this week, and I wanted to share the result. The scenario in my new demo is a customer calling a garage, "Fabrikam Motors", to book a car service:

<iframe width="560" height="315" src="https://www.youtube.com/embed/0eZEvEilFBI?si=K8r0JyE4T8qJ4kUU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Here's the actual prompt I'm using:

>"You are an AI assistant working for Fabrikam Motors that helps people book their annual car service and MOT test in the UK. Today's date is " + today_date + ". When looking for available booking dates, you must always use the 'get_available_booking_days' tool. Never make up dates yourself. When looking up car information, you must always use the 'get_car_info' tool. Never make up car information yourself. Follow this script: 1. Greet the caller as soon as the call starts, 'Hi, welcome to Fabrikam Motors, how can I help you today?'2. If the caller would like an MOT or annual car service, please ask them for their vehicle registration number.3. Read back the vehicle registration number to them, and ask them to confirm the details are correct.4. If incorrect repeat steps 2 and 3 until the caller has confirmed the details are correct.5. Use the 'get_car_info' tool to look up the car's colour, manufacturer, and MOT expiry date using the confirmed vehicle registration number. Do not place the caller on hold.6. Wait a few seconds, and then verify the tool output with the caller, confirming the car's colour, manufacturer, and MOT expiry date.7. Use the 'get_available_booking_days' tool to look up available booking dates, and provide these options to the caller.8. Confirm the caller's preferred date, and tell them they'll receive a confirmation text message to their phone.9. Ask if there are any other issues with the car that need to be addressed during the service.10. Close the call, thanking the caller for the booking, and reminding them bring the car's locking wheel nut key and vehicle service logbook.11. Say goodbye."

During the call, the AI agent takes the UK registration plate (step 2), and via a function call, queries an public vehicle information API for the car's details (step 5). There's also a second function call which provides booking availability, which returns some mocked date options (step 7).

**Here are my top ten learnings I wanted to share from trying this out:**

1\. This demo seems daunting, but you can get started in minutes. Simply deploy an Azure OpenAI Service instance in East US 2 or Sweden Central, and use [Azure AI Studio](https://ai.azure.com/) to immediately try the real-time audio service - no code needed. For starters, just use hard-coded values instead of function calls if you want to get a feel for the conversation flow.

![Screenshot of Azure OpenAI Service Realtime API demo](https://media.licdn.com/dms/image/v2/D4E12AQFc83jQtGvKBQ/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1729244709853?e=1753920000&v=beta&t=n6-HBCwUEd67IIYp0l2P9wlAplq1Xaf4MfT23dejGh4)

2\. Cloning the existing [VoiceRAG demo](https://github.com/Azure-Samples/aisearch-openai-rag-audio) repo is a really great way to get a working demo up and running quickly. This sample can now run inside a [GitHub Codespaces](https://github.com/features/codespaces) environment, giving you loads of flexibility and no requirement to install anything locally. It also helps you understand how tools are defined. GitHub Codespaces is free for individual use up to 60 hours a month.

3\. To get the original [VoiceRAG demo](https://github.com/Azure-Samples/aisearch-openai-rag-audio) working with your own Azure OpenAI Service and Azure AI Search instance, you'll need to create a .env file in the /app/backend directory. This is also where I stored my external API key for the vehicle lookup:

```
AZURE_OPENAI_ENDPOINT="https://xxxxxxxxx.openai.azure.com"
AZURE_OPENAI_REALTIME_DEPLOYMENT="gpt-4o-realtime-preview"
AZURE_OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AZURE_SEARCH_ENDPOINT="https://xxxxxxxxxx.search.windows.net"
AZURE_SEARCH_INDEX="<indexname>"
AZURE_SEARCH_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

4\. The Azure AI Search element was the most costly part of this demo for me, and I used the Basic tier (which is [approx. $74/£55](https://azure.microsoft.com/en-us/pricing/details/search/?msockid=3e6f21cebcd26bca2235355ebda86a3f#pricing) at time of writing). If you're building a demo that just calls an API, and doesn't call Azure AI Search at all, then you don't *need *to deploy it.

5\. Multiple tool definitions *are* supported, so if you do want to keep the existing Azure AI Search tool definition from the demo to implement a new one, then it can quite happily exist side-by-side with the custom tools you add.

6\. If you want to create a function call to an API using voice, it can feel quite challenging at first. I broke down the task into smaller tasks to make it more digestible:

- First, get your API working with a simple API call code sample. No AI integration at all.
- Next, build a tool function for your API call, which works with the basic text input/output. This helps build confidence around using a tool to query an API with function calling. If you haven't done this before, there are some great code samples in [Microsoft Learn](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling), and in [GitHub Models](https://gh.io/models).
- Then using the Azure AI Search tool as an example, describe a function which provides a simple, mocked answer without any API call (in my case, the booking dates).
- Building on all of the previous knowledge, now write a function which includes the API call.

7\. I used both GitHub Copilot and o1-preview extensively to help me write and debug the code to define the tools faster. In my tool creation prompts, I would include the existing code for the existing tools (in ragtools.py), and my basic API code, and asked the model to create a new tool based on those inputs.

8\. Creating a prompt for the Realtime API is similar to doing it for text/image, but requires a bit of practice to get right. Especially when it comes to timing, and ensuring the AI doesn't go off-script.

9\. It's worth noting that gpt-4o-realtime-preview is free on Azure OpenAI until the end of October 2024, so now is a great time to experiment with it.

10\. Finally, I haven't been able to get my demo working flawlessly every time yet - I think due to some bugs in my function calls (I'm honestly not an expert developer). I probably need to focus on tightening up the output of the function call to ensure that the tool provides the AI assistant with a more predicable, strictly defined format. However, I'm delighted that I managed to build something that works this well in only a single day of coding.

To wrap up, even though this new Realtime API service is in preview, I think the extensibility aspect opens up some very exciting scenarios, and allows for relatively simple integration with existing systems. If you're a Microsoft partner looking to use this new feature to solve a customer challenge, I'd love to hear from you - please feel to drop me a message on here. Thanks for reading!