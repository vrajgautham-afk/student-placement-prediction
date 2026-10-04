# ============================================================
# AI PLACEMENT ADVISOR
# ============================================================


def generate_advice(
    student_data,
    placement_probability
):

    cgpa = student_data.get(
        "CGPA", 0
    )

    tenth = student_data.get(
        "10th_Percentage", 0
    )

    twelfth = student_data.get(
        "12th_Percentage", 0
    )

    backlogs = student_data.get(
        "Backlogs", 0
    )

    internships = student_data.get(
        "Internships", 0
    )

    projects = student_data.get(
        "Projects", 0
    )

    certifications = student_data.get(
        "Certifications", 0
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

    attendance = student_data.get(
        "Attendance", 0
    )


    # ========================================================
    # PROBABILITY
    # ========================================================

    if placement_probability is None:

        probability_text = (
            "Placement probability could not be calculated."
        )

    else:

        probability_text = (
            f"{placement_probability:.2f}%"
        )


    # ========================================================
    # DETERMINE PROFILE
    # ========================================================

    strengths = []

    weaknesses = []

    recommendations = []


    # CGPA

    if cgpa >= 8.0:

        strengths.append(
            "Strong academic CGPA"
        )

    elif cgpa < 6.0:

        weaknesses.append(
            "Low CGPA"
        )

        recommendations.append(
            "Focus on improving academic performance."
        )


    # Internships

    if internships >= 1:

        strengths.append(
            "Has internship experience"
        )

    else:

        weaknesses.append(
            "No internship experience"
        )

        recommendations.append(
            "Try to complete at least one internship."
        )


    # Projects

    if projects >= 2:

        strengths.append(
            "Good project experience"
        )

    else:

        weaknesses.append(
            "Limited project experience"
        )

        recommendations.append(
            "Build 2-3 practical projects."
        )


    # Coding

    if coding >= 70:

        strengths.append(
            "Good coding skills"
        )

    else:

        weaknesses.append(
            "Coding skills need improvement"
        )

        recommendations.append(
            "Practice DSA and coding problems regularly."
        )


    # Communication

    if communication >= 70:

        strengths.append(
            "Good communication skills"
        )

    else:

        weaknesses.append(
            "Communication skills need improvement"
        )

        recommendations.append(
            "Practice speaking, HR questions and mock interviews."
        )


    # Aptitude

    if aptitude >= 70:

        strengths.append(
            "Good aptitude performance"
        )

    else:

        weaknesses.append(
            "Aptitude needs improvement"
        )

        recommendations.append(
            "Practice quantitative aptitude and logical reasoning."
        )


    # Backlogs

    if backlogs > 0:

        weaknesses.append(
            f"{backlogs} active/previous backlog(s)"
        )

        recommendations.append(
            "Clear all backlogs as early as possible."
        )


    # Certifications

    if certifications >= 2:

        strengths.append(
            "Good certification profile"
        )

    else:

        recommendations.append(
            "Consider completing relevant technical certifications."
        )


    # ========================================================
    # BUILD RESPONSE
    # ========================================================

    advice = f"""
## 🤖 AI Placement Analysis

### 📊 Placement Probability

**{probability_text}**

---

### 👨‍🎓 Student Profile

- **CGPA:** {cgpa}
- **10th Percentage:** {tenth}%
- **12th Percentage:** {twelfth}%
- **Backlogs:** {backlogs}
- **Internships:** {internships}
- **Projects:** {projects}
- **Certifications:** {certifications}
- **Coding Score:** {coding}
- **Communication Score:** {communication}
- **Aptitude Score:** {aptitude}
- **Attendance:** {attendance}%

---

### ✅ Strengths

"""

    if strengths:

        for item in strengths:

            advice += f"- {item}\n"

    else:

        advice += "- No major strengths identified yet.\n"


    advice += """

### ⚠️ Areas to Improve

"""

    if weaknesses:

        for item in weaknesses:

            advice += f"- {item}\n"

    else:

        advice += "- No major weaknesses identified.\n"


    advice += """

### 🚀 Recommended Actions

"""

    if recommendations:

        for i, item in enumerate(
            recommendations,
            1
        ):

            advice += f"{i}. {item}\n"

    else:

        advice += (
            "Your profile is already strong. "
            "Focus on interview preparation and placement-specific practice.\n"
        )


    advice += """

### 🎯 30-Day Placement Plan

**Week 1**
- Revise programming fundamentals.
- Start daily aptitude practice.
- Improve your resume.

**Week 2**
- Practice DSA.
- Work on your strongest project.
- Practice communication.

**Week 3**
- Take mock coding tests.
- Practice technical interview questions.
- Practice HR questions.

**Week 4**
- Conduct complete mock interviews.
- Apply for suitable jobs.
- Review weak areas.

### 💡 Final Advice

Focus on improving your weakest areas while maintaining your current strengths.
A good placement profile requires a combination of academics, technical skills,
projects, communication, aptitude and interview preparation.
"""

    return advice