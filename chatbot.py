# ============================================================
# PLACEMENT CHATBOT
# ============================================================


def ask_ai(
    question,
    student_data
):

    question = question.lower().strip()


    cgpa = student_data.get(
        "CGPA", 0
    )

    internships = student_data.get(
        "Internships", 0
    )

    projects = student_data.get(
        "Projects", 0
    )

    coding = student_data.get(
        "Coding_Score", 0
    )

    communication = student_data.get(
        "Communication_Score", 0
    )

    aptitude = student_data.get(
        "Aptitude_Score", 0
    )

    backlogs = student_data.get(
        "Backlogs", 0
    )


    # ========================================================
    # CGPA
    # ========================================================

    if (
        "cgpa" in question
        or "percentage" in question
        or "academic" in question
    ):

        return f"""
### 📚 Academic Advice

Your current CGPA is **{cgpa}**.

For placement preparation:

- Maintain or improve your CGPA.
- Check the minimum CGPA requirements of companies.
- Focus especially on subjects related to your target job.
- Don't depend only on academics; technical skills and projects are also important.
"""


    # ========================================================
    # INTERNSHIP
    # ========================================================

    if (
        "internship" in question
        or "intern" in question
    ):

        if internships == 0:

            return """
### 💼 Internship Advice

You currently have no internship experience.

Try to complete at least one internship in an area related to your target career.

Good options include:

- Software development
- Data analytics
- Machine learning
- Web development
- Cloud computing
- Cybersecurity

Even a short practical internship can give you useful project and interview experience.
"""

        return f"""
### 💼 Internship Advice

You currently have **{internships} internship(s)**.

That's a positive part of your placement profile.

Focus on:

- Explaining what you actually worked on.
- Knowing the technologies used.
- Preparing questions about your internship.
- Adding measurable achievements to your resume.
"""


    # ========================================================
    # PROJECTS
    # ========================================================

    if (
        "project" in question
        or "projects" in question
    ):

        return f"""
### 🛠️ Project Advice

You currently have **{projects} project(s)**.

For placements, try to have 2-3 strong projects.

Each project should clearly explain:

1. Problem statement
2. Technologies used
3. Your contribution
4. Implementation
5. Results
6. Challenges
7. Future improvements

You should be able to explain every part of your project during an interview.
"""


    # ========================================================
    # CODING
    # ========================================================

    if (
        "coding" in question
        or "programming" in question
        or "dsa" in question
    ):

        return f"""
### 💻 Coding Advice

Your current coding score is **{coding}**.

Focus on:

- Arrays
- Strings
- Linked Lists
- Stacks
- Queues
- Trees
- Graphs
- Sorting
- Searching
- Recursion
- Dynamic Programming

Try solving coding problems every day rather than studying only before interviews.
"""


    # ========================================================
    # COMMUNICATION
    # ========================================================

    if (
        "communication" in question
        or "english" in question
        or "speaking" in question
    ):

        return f"""
### 🗣️ Communication Advice

Your current communication score is **{communication}**.

Practice:

- Self introduction
- Explaining projects
- HR questions
- Group discussions
- Technical explanations
- Speaking clearly and confidently

Record yourself answering interview questions and review your answers.
"""


    # ========================================================
    # APTITUDE
    # ========================================================

    if (
        "aptitude" in question
        or "reasoning" in question
    ):

        return f"""
### 🧠 Aptitude Advice

Your current aptitude score is **{aptitude}**.

Practice:

- Percentages
- Profit and loss
- Time and work
- Time, speed and distance
- Probability
- Permutations and combinations
- Number systems
- Logical reasoning
- Data interpretation

Try taking timed mock tests regularly.
"""


    # ========================================================
    # BACKLOG
    # ========================================================

    if (
        "backlog" in question
        or "arrear" in question
    ):

        return f"""
### 📌 Backlog Advice

Your current backlog count is **{backlogs}**.

Many companies have eligibility criteria related to backlogs.

Your priority should be:

1. Clear active backlogs.
2. Maintain your CGPA.
3. Check individual company eligibility criteria.
4. Continue building technical skills.
"""


    # ========================================================
    # RESUME
    # ========================================================

    if (
        "resume" in question
        or "cv" in question
    ):

        return """
### 📄 Resume Advice

Your resume should ideally contain:

- Contact information
- Education
- Technical skills
- Projects
- Internships
- Certifications
- Achievements

Keep it concise and preferably one page for a fresher.

Most importantly, be prepared to explain everything written on your resume.
"""


    # ========================================================
    # INTERVIEW
    # ========================================================

    if (
        "interview" in question
        or "hr" in question
    ):

        return """
### 🎤 Interview Preparation

Prepare these areas:

**Technical**
- Programming
- DSA
- DBMS
- Operating Systems
- Computer Networks
- OOP

**Project**
- Project architecture
- Technologies
- Your contribution
- Challenges

**HR**
- Tell me about yourself.
- Why should we hire you?
- What are your strengths?
- What are your weaknesses?
- Where do you see yourself in five years?

Practice answering naturally instead of memorizing answers.
"""


    # ========================================================
    # PLACEMENT
    # ========================================================

    if (
        "placement" in question
        or "job" in question
        or "placed" in question
    ):

        return f"""
### 🎯 Placement Advice

Based on your profile:

- CGPA: **{cgpa}**
- Internships: **{internships}**
- Projects: **{projects}**
- Coding Score: **{coding}**
- Communication Score: **{communication}**
- Aptitude Score: **{aptitude}**
- Backlogs: **{backlogs}**

Your main focus should be improving the weakest areas.

A strong placement preparation strategy combines:

**Academics + Coding + Projects + Aptitude + Communication + Interview Preparation**
"""


    # ========================================================
    # DEFAULT RESPONSE
    # ========================================================

    return f"""
### 🤖 Placement Assistant

I can help you with:

- 📚 CGPA and academics
- 💼 Internships
- 🛠️ Projects
- 💻 Coding and DSA
- 🗣️ Communication
- 🧠 Aptitude
- 📄 Resume
- 🎤 Interviews
- 🎯 Placement preparation

For example, ask:

**"How can I improve my coding skills?"**

or

**"How should I prepare for placement interviews?"**

Your current CGPA is **{cgpa}**, so I can also give advice based on your profile.
"""