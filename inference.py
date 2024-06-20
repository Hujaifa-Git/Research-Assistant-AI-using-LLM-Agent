import os
token = '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'
serp_api='fed3a01a75056e37f7648eb9821d63b13850e8dda4c17c473d8567392b9e740a'
os.environ['HUGGINGFACEHUB_API_TOKEN'] = token
os.environ['SERPAPI_API_KEY'] = serp_api

import config as ctg
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_huggingface import ChatHuggingFace
from langchain import hub
from langchain.agents import AgentExecutor, load_tools
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import (
    ReActJsonSingleInputOutputParser,
)
from langchain.tools.render import render_text_description
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain_community.tools.pubmed.tool import PubmedQueryRun

from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper, PubMedAPIWrapper

def create_agent():
    tokenizer = AutoTokenizer.from_pretrained(ctg.model_id)
    model = AutoModelForCausalLM.from_pretrained(ctg.model_id, device_map='auto')
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=ctg.max_new_tokens)
    llm = HuggingFacePipeline(pipeline=pipe)

    chat_model = ChatHuggingFace(llm=llm)

    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    pubmed = PubmedQueryRun(api_wrapper=PubMedAPIWrapper())
    arxiv = ArxivQueryRun(api_wrapper=ArxivAPIWrapper())

    tools = load_tools(["serpapi"], llm=llm)
    tools.append(wikipedia)
    tools.append(pubmed)
    tools.append(arxiv)

    prompt = hub.pull(ctg.prompt_template_id)
    prompt.messages[0].prompt.template = ctg.prompt_template
    prompt = prompt.partial(
        tools=render_text_description(tools),
        tool_names=", ".join([t.name for t in tools]),
    )

    chat_model_with_stop = chat_model.bind(stop=["\nObservation"])
    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_log_to_str(x["intermediate_steps"]),
        }
        | prompt
        | chat_model_with_stop
        | ReActJsonSingleInputOutputParser()
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True).with_config({"run_name" : "Agent"})
    return agent_executor


def generate(agent_executor, query):
    response = agent_executor.invoke(
        {
            "input": query
        }
    )
    return response


if __name__ == '__main__':
    query = ctg.query
    agent_executor = create_agent()
    response = generate(agent_executor,query)
    print(response['output'])


