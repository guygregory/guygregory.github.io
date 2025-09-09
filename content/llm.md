Title: Using LLM with Azure AI Foundry
Date: 2025-09-09
Category: Blog
Tags: azure
Slug: llm
Author: Guy Gregory
Summary: How to configure Simon Willison's popular LLM CLI tool with Azure AI Foundry models

### Getting Started with LLM

I'm a big fan of [Simon Willison's](https://simonwillison.net/) work, and recently, I had a need to do some simple inference using gpt-5 on Azure AI Foundry. In the past I've used GitHub Models for this type of work, and that works pretty well up to a certain point:

```bash
gh models run openai/gpt-4.1 "Tell me a joke"
```

However, I was running into a few challenges with token limits, and usage limits on GitHub Models, so I wanted to switch to Azure AI Foundry instead - I thought it'd be a great opportunity to try out [Simon's hugely popular LLM CLI tool](https://github.com/simonw/llm).

```bash
llm "Tell me a joke"
```


### 1. Installation

Installation was a breeze - with a simple:

```bash
pip install llm
```

### 2. Storing an API key

Next, I needed to store my Azure AI Foundry API key, retrieved from the [Azure AI Foundry project overview:](https://ai.azure.com/foundryProject/overview)

<img width="1025" height="425" alt="image" src="https://github.com/user-attachments/assets/60b03e48-598a-42fc-a447-9747559bae23" />

By default, `llm keys set` will store an OpenAI API key, so adding `azure` on the end allowed me to differenciate it later

```bash
llm keys set azure
```
When entering the key, the text isn't echoed back to the console, but you can check the keys.json file in the next step if you need to confirm.

### 3. Configuring the Azure AI Foundry Models

Before the next step, you'll want to check the path to your llm configuration files:

```bash
PS C:\Users\gugregor> llm keys path
C:\Users\gugregor\AppData\Roaming\io.datasette.llm\keys.json
```

...so you can open the folder, and create a new (blank text) file called `extra-openai-models.yaml`. This file will be used to define any models from Azure AI Foundry.

<img width="978" height="474" alt="image" src="https://github.com/user-attachments/assets/942e1fcc-d1ae-44c1-8707-b70cb64b2aac" />

In this YAML file, you'll want to provide the details of your Azure AI Foundry model deployments:

```yaml
- model_id: aoai/gpt-5
  model_name: gpt-5
  api_base: https://<foundry resource>.openai.azure.com/openai/v1/
  api_key_name: azure

- model_id: aoai/gpt-5-mini
  model_name: gpt-5-mini
  api_base: https://<foundry resource>.openai.azure.com/openai/v1/
  api_key_name: azure

- model_id: aoai/gpt-5-nano
  model_name: gpt-5-nano
  api_base: https://<foundry resource>.openai.azure.com/openai/v1/
  api_key_name: azure

- model_id: aoai/gpt-4.1
  model_name: gpt-4.1
  api_base: https://<foundry resource>.openai.azure.com/openai/v1/
  api_key_name: azure
```
Some important Azure-specific considerations:
- `model_id` is essentially the 'friendly name' for the model within the LLM tool. I chose a `aoai/` prefix, so I could differenciate between Azure models, and OpenAI API models.
- `model_name` is the Azure deployment name - which _could_ be different from the model name (although it makes sense to keep it the same where possible).
- `api_base` needs to include the `openai/v1/` suffix, because the LLM tool isn't able to accept the `api_version` from the legacy API. If you're not sure where to find the <foundry resource>, check in the [Azure AI Foundry project overview:](https://ai.azure.com/foundryProject/overview)
- `api_key_name` is the name of the key you stored in step 2 (I used `azure`, but you can use whatever you like, as long as they match)

Don't forget to save the YAML file, once you've added all the above details.

### 4. Testing the Azure AI Foundry model

Now that you've configured the extra models, you should be able to run `llm` using the following command:

```bash
llm "Tell me a joke" -m aoai/gpt-5-mini
```
the `-m` parameter specifies the model that you've defined in the YAML file from step 3.

### 5. Setting the default model (optional, recommended)

If you're going to use Azure AI Foundry models regularly, then you may want to change the default model over like this:
```bash
llm models default aoai/gpt-5-mini
```

That way, you don't need to specify the model using the `-m` parameter each time, so you get an easy to remember, concise command:

```bash
llm "Tell me a joke"
```

### Conclusion

LLM is a super handy utility which can easily be configured to use Azure AI Foundry models with minimal effort. I can see myself using it for a range of simple command-line tasks, and potentially even for more advanced scripting. It doesn't have the power or advanced features of something like Semantic Kernel, but that level of functionality isn't always required. Try it out today!

LLM - GitHub.com<br>
https://github.com/simonw/llm
