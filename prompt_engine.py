def build_prompt(problem, users, data_input, output, automation):

    prompt = f"""
You are a senior AI systems architect.

Design a GenAI solution based on the following idea:

Problem to solve:
{problem}

Target users:
{users}

Data input:
{data_input}

Expected output:
{output}

Automation level:
{automation}

Provide:

1. Solution overview
2. System architecture components
3. Recommended tech stack
4. Example AI prompts
5. Step-by-step development roadmap

Explain clearly and professionally.
"""
    return prompt