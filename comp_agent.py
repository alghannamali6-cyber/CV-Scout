# comp_agent.py
from config import call_llm, SECTIONS

class ComparisonAgent:
    """
    Compare JD and CV using an LLM and return:
    - Bullet-point explanation per section
    - Tick ✅ or cross ❌
    - Numeric score per section
    - Overall score
    """
    def __init__(self, jd_chunks, cv_chunks):
        self.jd_chunks = jd_chunks
        self.cv_chunks = cv_chunks

    def compare(self):
        prompt = f"""
You are an expert HR evaluator. Compare a candidate's CV against a Job Description and pay attention to each detail in each section.

JD sections (you MUST only use these sections and never invent new ones):
{SECTIONS}

JD content (chunked):
{self.jd_chunks}

CV content (chunked):
{self.cv_chunks}

STRICT RULES:
- You MUST NOT create any new section headers beyond the sections listed in {SECTIONS}.
- All evaluation must occur strictly inside those sections.
- Never introduce headers like “Open-Source Contribution”, “Achievements”, “Extra Skills”, etc.

SCORING LOGIC:
- Some sections might not exist in the CV:
    - If the section has MUST-HAVE requirements → score = 0
    - If it only has PREFERRED/PLUS requirements → do NOT heavily penalize
- Requirement categories:
    - MUST-HAVE → ❌ if missing and reduces score
    - PREFERRED → No ❌ if missing, only mention if relevant
    - PLUS/NICE-TO-HAVE → Do NOT affect score at all

FOR EACH SECTION:
1. Provide hierarchical sub-bullets:
    - ✅ if requirement is present
    - ❌ only if a MUST-HAVE requirement is missing
    - Do NOT use ❌ for PREFERRED or PLUS items
2. Provide a numeric score (0–100)
3. Explain points lost ONLY if MUST-HAVE items were missing
4. Never add commentary outside the section content

EDUCATION RULE:
- Education must be ONLY ONE bullet point.
- If the candidate's Degree is related to the JD required Degree, mark it with ✅.
- If the candidate's Degree is unrelated to the JD required Degree, mark it with ❌ and explain the mismatch clearly.

PROJECTS RULE:
- Be detailed.
- Explicitly state whether each project aligns with JD requirements.
- Mention real-world experience, deployments, tools, or technologies relevant to JD.

FORMATTING:
- Plain text only.
- Hierarchical bullets.
- Do NOT add “None” under any section.
- Do NOT add any explanation or comments outside the structure.
- Do NOT place ticks/crosses on section headers.

At the end, provide an overall score (0–100) based on all section scores.

Example format (follow exactly):

Skills: 66
- ✅ Python
- ✅ Mechatronics basics
- ❌ MATLAB (MUST-HAVE missing)

Experience: 50
- ✅ 1 year backend
- ❌ AI and GenAI projects (MUST-HAVE missing)

Education: 100
- ✅ Bachelor's in Mechatronics Engineering

Projects: 0
- ❌ Industrial automation project (MUST-HAVE missing)

Overall Score: 68

Return ONLY the formatted text. No additional commentary.
"""

        response = call_llm(prompt)
        return response
