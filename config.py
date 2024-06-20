model_id = "teknium/OpenHermes-2.5-Mistral-7B"
token = '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'
serp_api='fed3a01a75056e37f7648eb9821d63b13850e8dda4c17c473d8567392b9e740a'
max_new_tokens=512
prompt_template_id = 'hwchase17/react-json'
query = 'Explain in details what causes lung cancer. Use Pubmed to get your answer'



prompt_template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

The way you use the tools is by specifying a json blob.
Specifically, this json should have a `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are: {tool_names}

Be Careful while choosing "action". If the question related to medical field use only use pub_med not wikipedia or Search. Search should be used only if the question is related to some latest news / event / information or if the information from wikipedia are not relevent enough. Only use arxiv if the query contains the paper id.

The $JSON_BLOB should only contain a SINGLE action, do NOT return a list of multiple actions. Here is an example of a valid $JSON_BLOB:

```
{{
"action": $TOOL_NAME,
"action_input": $INPUT
}}
```

ALWAYS use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action:
```
$JSON_BLOB
```
Observation: the result of the action
... (this Thought/Action/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin! Reminder to always use the exact characters `Final Answer` when responding."""

option = """Select which tool you want the LLM to use,
1. Search. [Use If you think the answer to your question can be found on the Internet]
2. wikipedia. [Use If you think the answer to your question can be found on the Wikipedia]
3. pub_med. [Use If your question is related to medical field and you think the answer to your question can be found on the PubMed]
4. arxiv. [Use If you want to know about any paper uploded in ArXiv]
5. Let the model decide. [RECCOMENDED. If you are unsure about the above option and want the model to decide which tool to use]
6. Exit.
Select any Option between 1 to 6: 
"""

option_dict = {
    1 : ". Use Search to get your answer",
    2 : ". Use wikipedia to get your answer",
    3 : ". Use pub_med to get your answer",
    4 : ". Use arxiv to get your answer",
    5 : "."
}
option_dict_for_web = {
    'Search' : ". Use Search to get your answer",
    'wikipedia' : ". Use wikipedia to get your answer",
    'pub_med' : ". Use pub_med to get your answer",
    'arxiv' : ". Use arxiv to get your answer",
    'Let the model decide.' : "."
}
