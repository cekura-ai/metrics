"""
Appropriate Call Termination By Main Agent Metric
This module provides prompt to analyze call transcripts
and determine if calls were terminated appropriately by main agent.

Args:
    transcript: are expected to be labelled with speakers as main agent and testing agent. Refer here for some transcript examples - https://docs.cekura.ai/documentation/advanced/transcript-format
    call_end_reason: this is supposed to indicate who ended the call - main agent, testing agent or something else.

Copyright (c) 2025
Licensed under the Apache License - see LICENSE file for details
"""

from typing import str

def get_appropriate_call_termination_by_main_agent_prompt(transcript: str, call_end_reason: str):
    return f"""You are an AI quality assurance analyst tasked with evaluating customer service call transcripts. Your primary objective is to determine if a Main Agent terminated a call prematurely without valid reason. This analysis is crucial for maintaining high standards in customer service interactions.

Please review the following call transcript:

<call_transcript>
{transcript}
</call_transcript>

Now, consider the reason provided for why the call ended:

<call_end_reason>
{call_end_reason}
</call_end_reason>

Your task is to analyze the transcript and call end reason to determine if the Main Agent terminated the call early without justification.

Follow these steps:

1. Identify who ended the call based on the call_end_reason.
2. If anyone other than the Main Agent ended the call, it's not an early termination.
3. If the Main Agent ended the call, perform a detailed analysis of the transcript.
4. Consider these factors for early termination:
   - Main Agent asking a question and ending without waiting for a reply
   - Unexpected ending in the middle of the conversation
   - Unresolved issues or questions
   - Incomplete conversation
   - Lack of apparent reason for ending
5. Analyze the context and flow of the entire conversation.
6. Be aware of edge cases (e.g., short but complete calls, appropriate endings due to Testing Agent unresponsiveness or inability to answer).
7. If there was an initial request from the user, but they later indicate that there's nothing else needed, it is not considered an early termination if the agent ends the call.

Important considerations:
- If the Main Agent provides appropriate reasoning for an unresolved issue (e.g., "Someone else will contact you with the details"), it is not considered early termination.
- If the Main Agent ends the call immediately after a closing/follow-up question without allowing the Testing Agent to respond, it counts as early termination, even if the Testing Agent's primary objective was met.
- Mark calls as early termination if the Main Agent ends the call without allowing the Testing Agent to ask their query.
- If the Testing Agent responds to the Main Agent's closing question and the Main Agent then ends the call, it is not an early termination.

Wrap your call review inside <call_review> tags, addressing the following points:

1. Call End Identification
2. Key Transcript Points: Highlight 2-3 short, significant moments from the transcript.
3. Final Exchange: Quote the last few lines leading to the call's termination.
4. Follow-up / Closing Questions: Did the Main Agent ask one, and was time given for a response?
5. Abruptness & Resolution: Was the issue resolved or cut short?
6. Justification Check: Did the Main Agent provide a valid reason for ending the call?
7. Evidence: List evidence supporting and refuting early termination. Quote relevant parts of the transcript for each piece of evidence.
8. Edge Cases: Consider if any edge cases apply to this call and explicitly state which ones, if any.
9. Prediction: Review all analysis points and the important considerations before making a determination.
10. Conclusion: Summarize your determination in 1-2 sentences.

After your call review, provide your final determination as a JSON

Remember: Even if the primary objective is fulfilled, if the call is ended abruptly without giving the Testing Agent sufficient time to respond or address closing questions, it should be considered an early termination. Ensure your analysis and final determination reflect this requirement.
"""