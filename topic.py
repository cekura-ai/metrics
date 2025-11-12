"""
Topic Metric
This module provides prompt to analyze call transcripts
and checks the main topic of the conversation.

Args:
    transcript: are expected to be labelled with speakers as main agent and testing agent. Refer here for some transcript examples - https://docs.cekura.ai/documentation/advanced/transcript-format
    topic_dict: These are the nodes where a user can dropoff

Copyright (c) 2025
Licensed under the Apache License - see LICENSE file for details
"""

from typing import Dict, str

def get_categorize_topic_prompt(topic_dict: Dict, transcript: str):
    return f"""
    You are an advanced AI assistant specializing in categorizing call transcripts for a voice agent system. Your task is to analyze a given transcript and match it to existing topics. Please follow these instructions carefully:

First, review the call transcript:

<transcript>
{transcript}
</transcript>

Now, consider the current list of topics for this agent:

<existing_topics>
{topic_dict}
</existing_topics>

Your goal is to match the transcript to one of the given topics or, if it doesn't match any existing topics, assign it to category ('other').

Please follow these steps:

1. Analyze the transcript thoroughly, comparing it to each of the given topics.

2. Wrap your topic matching analysis inside <topic_matching_analysis> tags:
   a. List all existing topics with their indices for easy reference.
   b. Summarize the key points of the transcript (3-5 bullet points).
   c. For each existing topic:
      - Quote relevant parts of the transcript that relate to this topic.
      - Explicitly state whether it's a match or not.
      - Rate the relevance of this topic on a scale of 1-10.
   d. Create a table summarizing your findings, including topic index, topic name, relevance score, and a brief comment.
   e. State which topic seems most relevant or if 'other' is the best choice.

3. Based on your analysis, select the most relevant existing topic or choose 'other' if none of the existing topics apply.

4. Provide a brief explanation for your final choice, highlighting the key points that led to your decision.

Output your results in the following format:

<topic_matching_analysis>
[Your detailed analysis as described in steps 2 and 3]
</topic_matching_analysis>

<topic_category_index>
[Insert only the integer representing the chosen category (0-N)]
</topic_category_index>

Remember:
- If the transcript matches an existing topic, return that topic's index.
- Ensure your analysis is thorough and your final decision is well-justified based on the transcript content.
"""
