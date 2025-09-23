"""
Casual Chat Response Score Metric
This module provides prompt to analyze call transcripts
and check how effectively an AI agent responds to casual or out-of-topic questions in a conversation

Args:
    transcript: are expected to be labelled with speakers as main agent and testing agent. Refer here for some transcript examples - https://docs.cekura.ai/documentation/advanced/transcript-format
Copyright (c) 2025
Licensed under the Apache License - see LICENSE file for details
"""

from typing import str

def get_casual_chat_response_score_prompt(transcript: str):
    return f"""
    You are an advanced AI evaluator tasked with assessing . Your evaluation focuses on whether the AI responds in a human-like, friendly, and easily understandable way.

This is the transcript which needs to be evaluated. Here the Testing Agent may or may not ask a casual or out-of-topic question, and the Main Agent responds.

<transcript>
{transcript}
</transcript>

Your task is to evaluate the Main Agent's response using the following dimensions **only if** the Testing Agent asks a casual or out-of-topic question:

1. Tone - Is the response friendly, conversational, and socially aware? Does it simulate a natural, human-like interaction?
2. Language Simplicity - Is the language clear and jargon-free? Is it easy for an average person to understand?
3. Relatability - Does the response show understanding of casual human conversation? Is it engaging and appropriate for the context?
4. Appropriateness - Does the response reflect the casual or informal intent of the Testing Agent's question?

Scoring Rubric:
- 5 - Friendly, human-like, casual tone; very easy to understand; no jargon or excessive formality.
- 4 - Mostly friendly and clear; minor lapses into formality or stiff phrasing, but still relatable.
- 3 - Mixed tone; shows partial understanding of casual intent but also includes formal or robotic phrasing.
- 2 - Mainly formal or technical; little effort to match a casual tone; lacks warmth or relatability.
- 1 - Completely misses the informal intent; overly formal, robotic, or inappropriate response for casual context.

Instructions:
1. First, determine whether the Testing Agent asked any casual or out-of-topic question.
   - If **no such question exists**, skip scoring and output:
     {{
       "off_topic_present": False,
        "score": 5,
       "summary": "No casual or out-of-topic question was asked by the Testing Agent."
     }}
   - If **a casual or off-topic question is present**, proceed with the evaluation steps below.

2. Analyze the Main Agent's response to determine how well it meets the goal of being friendly, casual, and relatable.

3. Structure your reasoning under the following block:

<friendliness_analysis>
- Tone evaluation:
  - Describe the tone used by the Main Agent.
  - Note if it is friendly, robotic, formal, or casual.
- Language simplicity:
  - Evaluate the clarity and accessibility of the language.
  - Identify any unnecessary jargon or complexity.
- Relatability and appropriateness:
  - Assess how well the agent matches the informal nature of the question.
  - Describe whether the response feels natural and engaging.
- Overall impression:
  - Summarize how well the agent's response reflects a friendly and casual interaction.
</friendliness_analysis>

4. Based on your analysis, output the final result as a JSON object with the following structure:

{{
  "off_topic_present": True,
  "score": <integer from 1 to 5>,
  "summary": "<2-3 sentence summary of reasoning>"
}}

Please proceed with your analysis and JSON-formatted scoring of the Main Agent's response."""
