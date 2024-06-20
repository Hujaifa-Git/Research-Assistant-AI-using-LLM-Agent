# LLM Research Assistant

Welcome to LLM Research Assistant. You can use this application as a research assitant. You can ask any question and the LLM will retrieve answers for you from variour sources.

## Table of Contents

- Iroduction
- Used Tools
- Installation
- Configuration
- Inference Terminal
- Inference UI
- Demo

## Introduction

The LLM (Large Language Model) React JSON Agent is a concept and framework that allows a large language model to interact with external tools and data sources via a structured JSON interface. This approach leverages the capabilities of large language models to perform tasks that require interacting with APIs, databases, or other external systems, effectively turning the model into an agent that can react to JSON-formatted requests and responses.

Here an Open-Sourced LLM is used "OpenHermes-2.5-Mistral-7B". The task of an agent is a complicated one so usually ChatGPT-4 is used for this task. But here an open-sourced LLM is used and it performs fairly well.

## Used Tools
Here 4 different tools are used. You can specify the LLM to use any particular tool or you can let the LLM decide which tool it'll use. Given below are the tools used here,

- Search [SearpAPI]
- Wikipedia
- PubMed
- ArXiv

## Installation

To get started, you need to set up the Conda environment.

### Step 1: Install Conda

If you haven't already, install Conda from the [official Anaconda website](https://www.anaconda.com/products/distribution) and follow the installation instructions.

### Step 2: Create the Conda environment

Once Conda is installed, create a new environment named `llm_module` using the provided `.yml` file and activate that environment:

```bash
conda env create -f environment.yml
conda activate llm_module
```

Then you have to select which LLM you want to use, put your Huggingface Token and SerpAPI key in 'config.py' file

```python
model_id = "teknium/OpenHermes-2.5-Mistral-7B"
token = <HUGGINGFACE_TOKEN>
serp_api= <SerpAPI_TOKEN>
```
You can select any Huggingface LLM here. But not many open-souced LLM can do Agent related task so be careful. "OpenHermes-2.5-Mistral-7B" is an open sourced LLM Model that can be used as an agent you can just use this model.
## Configuration

You can change configurations according to your need. You just need to edit the 'config.py' file.
```python
max_new_tokens=512
prompt_template_id = 'hwchase17/react-json'
query = 'Explain in details what causes lung cancer. Use Pubmed to get your answer'
```
You can also change the prompt format used here and even edit the prompt template.

## Inference Terminal

It is recommended to use terminal to run this application because if you run this application using termal you can see the entire log of model. You can see the thoughts of the model, what tool the model is using, what is the reponse from each tool and even the number of times tools were used.

To run this application using terminal just put the following command,

```bash
python main_terminal.py
```
Here is a demo which show how this application works in the terminal,

![Demo Terminal](Demo/LLM_AGENT_TERMINAL.gif)

## Inference UI
If you use the UI (FastAPI Application) to run this application, you'll only see the final output from the model. You will be able to see the logs in the terminal but not in the UI.

To run this application using FastAPI, just run the following command,
```bash
uvicorn main:app
```
After the application has loaded go to http://127.0.0.1:8000/

Here is a demo which show how this application works in FastAPI,

![Demo UI](Demo/LLM_AGENT_UI.gif)

