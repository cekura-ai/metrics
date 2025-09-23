"""
Hallucination Metric
This module provides prompt to analyze call transcripts
and check if an AI Agent gave hallucinated responses in a conversation

Args:
    transcript: are expected to be labelled with speakers as main agent and testing agent. Refer here for some transcript examples - https://docs.cekura.ai/documentation/advanced/transcript-format

Note: We expect here that you will attach the files directly during LLM calls

Copyright (c) 2025
Licensed under the Apache License - see LICENSE file for details
"""

from typing import str

def get_hallucination_prompt(transcript: str):
    prompt = f"""You are an advanced fact-checking system designed to compare a given conversation transcript against contextual information. Your task is to determine whether the transcript agrees with the provided knowledge base (context) and provide a detailed analysis followed by a concise explanation for your verdict.

Here is the transcript you need to verify against the context:

<transcript>
{transcript}
</transcript>

Instructions:
1. Analyze the context and transcript thoroughly.
2. Determine if the transcript agrees with the context.
3. **Focus on product descriptions**
   - Pay special attention to how products are described. Verify that product attributes, classifications, and characteristics align with the knowledge base. For example:
     If transcript describes "Nike Air Zoom Tempo Next as a fantastic casual shoe" but knowledge base says "Performance Running Shoe", this is a contradiction
   - **Price Consistency**: Ensure that prices presented in transcript are consistent with the knowledge base, accounting for any stated discounts or offers.
   - Note any discrepancies in product features, pricing, availability, etc.
4. Provide a detailed analysis of your findings.
5. If the transcript disagrees with the context, provide a correction if possible.
6. Be forgiving of missing details in the transcript, but strict about contradictions.
7. Rely solely on the given context; do not use any prior knowledge.
8. Treat any additional files provided as context with the same importance as the main context.
9. Allow for repetition or multiple attempts to fulfill requests unless explicitly contradicted by the knowledge base.

Before providing your final output, wrap a detailed fact-checking brea kdown in <detailed_analysis> tags:

a. Summarize the main points of the context
b. Summarize the main claims of the transcript
   - Go through the transcript chronologically and list all factual claims, product descriptions, and assertions made
c. List key claims from both the context and the transcript side by side
d. Quote relevant parts of the context and transcript
e. Compare the quotes, noting similarities and differences
f. Identify potential contradictions, ambiguities, or missing information
g. List and rate potential contradictions (minor, moderate, major)
h. Consider the implications of missing information
i. List arguments for agreement and disagreement
j. Consider alternative interpretations
k. List potential biases or assumptions that might affect the analysis
l. Categorize claims as factual, interpretative, or speculative
m. Assess the overall tone and intent of both the context and transcript
n. Make a preliminary verdict
o. Justify your verdict
p. Assign a confidence rating (low, medium, or high) and explain why
q. For any discrepancies or potential hallucinations, note the corresponding timestamp from the transcript

After completing your analysis, distill your findings into 2-3 key points that form the basis of your verdict. These key points will be used in your final explanation.

Provide your final output as a JSON object with the following structure:

{{
  "explanation": "Concise explanation (2-3 key points) for the verdict, including whether the transcript agrees with the context and why. Include timestamps for any noted discrepancies, e.g., 'Agent provided incorrect address (2:15)'",
  "did_it_perform_as_expected": true/false
}}

The "explanation" field should be a concise summary of your key points, including your verdict and the reasoning behind it. The "did_it_perform_as_expected" field should be set to true if the transcript agrees with the context, and false if it doesn't.

Please proceed with your detailed analysis and final output.
"""
    return prompt