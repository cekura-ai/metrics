"""
DropOff Point Metric
This module provides prompt to analyze call transcripts
and check if the user (called Testing Agent here) drops off the conversation.

Args:
    transcript: are expected to be labelled with speakers as main agent and testing agent. Refer here for some transcript examples - https://docs.cekura.ai/documentation/advanced/transcript-format
    nodes: These are the nodes where a user can dropoff

Copyright (c) 2025
Licensed under the Apache License - see LICENSE file for details
"""

from typing import str

def get_dropoff_point_prompt(transcript: str, nodes: str):
    return f"""
    You are an AI assistant specializing in analyzing conversation flows. Your task is to examine a conversation transcript and a description of conversation nodes to determine the last node where the conversation ended or was dropped off.

First, review the following conversation transcript:

<conversation_transcript>
{transcript}
</conversation_transcript>

Now, examine the description of all conversation nodes:

<node_descriptions>
{nodes}
</node_descriptions>

Your goal is to identify the last node in the conversation and determine if it represents a natural endpoint or an incomplete conversation.

Please follow these steps in your analysis:

1. Read through the conversation transcript and node descriptions carefully.
2. Create a table of all nodes, their usage status, and relevant quotes from the transcript.
3. Count the total number of nodes to ensure all are considered.
4. For each node in the node descriptions, in the order they are presented:
   a. Determine if the node is used in the transcript.
   b. If it is used, identify which part of the conversation corresponds to this node.
   c. Provide your reasoning for why this node matches (or doesn't match) a part of the conversation.
5. After considering all nodes, identify the last node that was reached in the conversation.
6. List out potential indicators of natural endpoints and incomplete conversations.
7. Determine if the conversation ended naturally or was incomplete, considering these conditions:
   a. If the conversation ends with a message like "let me know if you have any further questions", consider it as a natural endpoint.
   b. If the last node is typically used to end conversations (e.g., a conclusion node), consider it as a natural endpoint.

Wrap your analysis in <thinking> tags. Be thorough in your examination but concise in your explanations. In your analysis:

1. Present the table of nodes, their usage status, and relevant quotes.
2. List the total number of nodes considered.
3. For used nodes, quote relevant parts of the conversation and explain why they match.
4. Identify any parts of the conversation that don't seem to match a node.
5. Present the list of potential natural endpoints and incomplete conversation indicators.
6. Evaluate whether the last node reached is a natural endpoint or if the conversation seems incomplete.
7. Pay special attention to cases where the conversation might have ended with "let me know if any further questions" or similar phrases.
8. Summarize any gaps or inconsistencies in the conversation flow.

After your analysis, provide a clear conclusion in <conclusion> tags, stating:
1. The last node reached in the conversation.
2. Whether the conversation ended naturally or was incomplete.
3. The reasoning behind your conclusion.

Before finalizing your answer, double-check your reasoning and conclusions to ensure they are based solely on the information provided in the transcript and node descriptions. Do not make assumptions about information not explicitly stated.
"""