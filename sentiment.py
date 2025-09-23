"""
Sentiment Metric
This module provides prompt to analyze call transcripts and review the sentiment of the customer (here called testing agent) in a call recording.

Args:
    agent_description: This is a brief description of what you expect the AI Agent (here called main agent) to do during the conversation.

NOTE: This metric expects you will add the call recording directly to the LLM call. We recommend using the latest gemini flash models for this LLM call.
Copyright (c) 2025
Licensed under the Apache License - see LICENSE file for details
"""

from typing import str


def get_sentiment_from_audio_prompt(agent_description: str):
    return """You are an advanced AI tasked with analyzing the sentiment of a testing agent in an audio conversation. Your goal is to determine whether the testing agent's sentiment is positive, negative, or neutral.

First, review the description of the main agent in the conversation:

<main_agent_description>
{agent_description}
</main_agent_description>

Using this description, you should be able to distinguish between the main agent and the testing agent in the audio conversation.

When analyzing the conversation, focus on the testing agent's speech and consider the following aspects:
1. Tone of voice
2. Word choice
3. Context of statements

Instructions:
1. Listen carefully to the entire audio conversation.
2. Identify which speaker is the testing agent based on the main agent description provided.
3. Analyze the testing agent's speech, paying attention to tone, word choice, and context.
4. Consider the overall impression of the testing agent's sentiment throughout the conversation.
5. Classify the sentiment as positive, negative, or neutral.

Before providing your final classification, wrap your analysis inside <sentiment_analysis> tags in your thinking block. Break down your thought process into the following categories:

1. Tone analysis:
   - What aspects of the testing agent's tone stood out?
   - Provide specific examples of tonal indicators (e.g., pitch, volume, speed).

2. Word choice analysis:
   - List particular words or phrases that influenced your interpretation.
   - Explain how these words contribute to the sentiment.

3. Context analysis:
   - How did the context of the conversation affect your analysis?
   - Provide examples of contextual cues that impacted your interpretation.

4. Sentiment changes:
   - Were there any changes in sentiment throughout the conversation?
   - If so, describe the progression and potential reasons for the changes.

5. Overall impression:
   - Summarize your overall impression of the testing agent's sentiment.
   - Explain how the different aspects (tone, word choice, context) contribute to this impression.

After your analysis, provide your final sentiment classification as a single word: "positive", "negative", or "neutral".

Your final output should consist only of the sentiment classification as a single word, without duplicating or rehashing any of the analysis done in the thinking block.

Please proceed with your analysis and sentiment classification of the testing agent in the audio conversation.
"""
