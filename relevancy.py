"""
Relevancy Metric
This module provides prompt to analyze call transcripts
and check if an AI Agent's (here called Main Agent) gave relevant responses in a conversation

Args:
    transcript: are expected to be labelled with speakers as main agent and testing agent. Refer here for some transcript examples - https://docs.cekura.ai/documentation/advanced/transcript-format

Copyright (c) 2025
Licensed under the Apache License - see LICENSE file for details
"""

from typing import str

def get_relevancy_score_prompt(transcript: str):
    return f"""You are an expert AI system designed to evaluate the quality of AI-assisted customer service conversations. Your task is to analyze whether the Main agent responses are relevant given the transcript of the conversation.

Here is the transcript of the conversation:

<transcript>
{transcript}
</transcript>

Please follow these steps to evaluate the conversation:

1. Review the transcript carefully.

2. In your evaluation, wrapped in <thinking> tags:
   a. Identify and list the main user intents (both explicit questions and implied goals).
   b. List out each Main agent response, numbering them sequentially.
   c. For each response:
      - Explicitly state whether it's relevant or irrelevant to the conversation.
      - Provide a concise justification for your classification.
      - Responses are irrelevant if they contain:
        1. Out of context text
        2. Contain function call code or code snippets
        3. Contains incomplete sentences which does not make any sense.
        4. Contains random formatting charcters (eg: read asterisk asterisk, underscore etc)
      - Ensure that even a part of the response contains any of the above four things then it should be marked as irrelevant
      - Any reponse that cannot be marked as irrelevant is a relevant response
      - Keep a running count of relevant and irrelevant responses.
   d. At the end, provide the final count of relevant and irrelevant responses.

3. Determine the final score:
   - True if ALL responses are relevant
   - False if there is even ONE irrelevant response

4. Provide a concise explanation for your final score, mentioning any irrelevant responses with their reasons.

Important notes:
- Responses related to the user's recent intent should be classified as relevant.
- If the Main agent continues to ask questions when the user has indicated they can't talk, classify these responses as irrelevant.
- Responses due to technical difficulties should not be considered irrelevant
"""
