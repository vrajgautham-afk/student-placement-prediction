import streamlit as st
import joblib

from llm import generate_advice
from chatbot import ask_ai
from auth import sign_up, sign_in, logout
# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None


# ==========================================
# LOGIN / SIGNUP PAGE
# ==========================================

if not st.session_state.logged_in:

    st.title("🎓 AI Student Placement Predictor")

    st.write("Please sign in to continue.")

    tab1, tab2 = st.tabs([
        "🔐 Sign In",
        "📝 Create Account"
    ])

    # --------------------------------------
    # SIGN IN
    # --------------------------------------

    with tab1:

        st.subheader("Sign In")

        email = st.text_input(
            "Email",
            placeholder="Enter your email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            key="login_password"
        )

        if st.button(
            "Sign In",
            type="primary",
            use_container_width=True
        ):

            if not email or not password:

                st.error("Please enter your email and password.")

            else:

                response, error = sign_in(
                    email,
                    password
                )

                if error:

                    st.error("Invalid email or password.")

                else:

                    st.session_state.logged_in = True
                    st.session_state.user = response.user

                    st.success("Login successful!")

                    st.rerun()


    # --------------------------------------
    # CREATE ACCOUNT
    # --------------------------------------

    with tab2:

        st.subheader("Create Account")

        signup_email = st.text_input(
            "Email",
            placeholder="Enter your email",
            key="signup_email"
        )

        signup_password = st.text_input(
            "Password",
            type="password",
            placeholder="Create a password",
            key="signup_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Confirm password",
            key="confirm_password"
        )

        if st.button(
            "Create Account",
            type="primary",
            use_container_width=True
        ):

            if not signup_email or not signup_password:

                st.error("Please enter all fields.")

            elif signup_password != confirm_password:

                st.error("Passwords do not match.")

            elif len(signup_password) < 6:

                st.error(
                    "Password must contain at least 6 characters."
                )

            else:

                response, error = sign_up(
                    signup_email,
                    signup_password
                )

                if error:

                    st.error(
                        f"Account creation failed: {error}"
                    )

                else:

                    st.success(
                        "Account created successfully!"
                    )

                    st.info(
                        "Check your email to verify your account."
                    )

    # Stop the rest of the app from displaying
    st.stop()

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Student Placement Predictor",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_models():

    model = joblib.load(
        "placement_model.pkl"
    )

    scaler = joblib.load(
        "scaler.pkl"
    )

    return model, scaler


try:

    model, scaler = load_models()

except Exception as e:

    st.error(
        "❌ Could not load the ML model."
    )

    st.error(str(e))

    st.stop()


# ============================================================
# TITLE
# ============================================================

st.title(
    "🎓 AI Student Placement Prediction System"
)

st.write(
    "Predict placement chances and get personalized AI career advice."
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title(
    "🎓 YOUR PLACEMENT PREDICTION"
)


# ============================================================
# INPUTS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.5,
        step=0.1
    )

    tenth = st.number_input(
        "10th Percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.1
    )

    twelfth = st.number_input(
        "12th Percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.1
    )

    backlogs = st.number_input(
        "Backlogs",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )


with col2:

    internships = st.number_input(
        "Internships",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

    projects = st.number_input(
        "Projects",
        min_value=0,
        max_value=20,
        value=2,
        step=1
    )

    certifications = st.number_input(
        "Certifications",
        min_value=0,
        max_value=20,
        value=2,
        step=1
    )

    coding = st.slider(
        "Coding Score",
        min_value=0,
        max_value=100,
        value=70
    )


with col3:

    communication = st.slider(
        "Communication Score",
        min_value=0,
        max_value=100,
        value=70
    )

    aptitude = st.slider(
        "Aptitude Score",
        min_value=0,
        max_value=100,
        value=70
    )

    attendance = st.slider(
        "Attendance",
        min_value=0,
        max_value=100,
        value=80
    )


# ============================================================
# MODEL INPUT
# ============================================================

feature_names = [
    "CGPA",
    "10th_Percentage",
    "12th_Percentage",
    "Backlogs",
    "Internships",
    "Projects",
    "Certifications",
    "Coding_Score",
    "Communication_Score",
    "Aptitude_Score",
    "Attendance"
]


input_data = [[
    cgpa,
    tenth,
    twelfth,
    backlogs,
    internships,
    projects,
    certifications,
    coding,
    communication,
    aptitude,
    attendance
]]


# ============================================================
# MODEL DEBUG
# ============================================================

with st.expander(
    "🔧 Model Debug Information"
):

    st.write(
        "Expected features:",
        getattr(
            model,
            "n_features_in_",
            "Unknown"
        )
    )

    st.write(
        "Input features:",
        len(input_data[0])
    )

    st.write(
        "Feature names:",
        getattr(
            model,
            "feature_names_in_",
            feature_names
        )
    )

    st.write(
        "Input data:",
        input_data
    )


# ============================================================
# CHECK FEATURE COUNT
# ============================================================

expected_features = getattr(
    model,
    "n_features_in_",
    len(input_data[0])
)


if expected_features != len(input_data[0]):

    st.error(
        f"""
        ❌ Feature mismatch!

        Model expects {expected_features} features,
        but the application is sending {len(input_data[0])} features.

        Make sure the features used here are exactly the same
        as the features used when training the model.
        """
    )

    st.stop()


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

if st.button(
    "🔮 Predict Placement",
    type="primary"
):

    try:

        # Scale input
        scaled_input = scaler.transform(
            input_data
        )

        # Prediction
        prediction = model.predict(
            scaled_input
        )[0]


        # Probability
        placement_probability = None

        if hasattr(
            model,
            "predict_proba"
        ):

            probabilities = model.predict_proba(
                scaled_input
            )

            # Find probability for class 1
            classes = list(
                model.classes_
            )

            if 1 in classes:

                index = classes.index(1)

                placement_probability = (
                    probabilities[0][index] * 100
                )


        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.subheader(
            "🎯 Prediction Result"
        )


        if prediction == 1:

            st.success(
                "🎉 Student is predicted to be PLACED!"
            )

        else:

            st.warning(
                "⚠️ Student is predicted to be NOT PLACED."
            )


        if placement_probability is not None:

            st.metric(
                "Placement Probability",
                f"{placement_probability:.2f}%"
            )


        # Save probability in session
        st.session_state[
            "placement_probability"
        ] = placement_probability

        st.session_state[
            "prediction"
        ] = prediction


    except Exception as e:

        st.error(
            "❌ Prediction error"
        )

        st.exception(e)

        st.stop()


# ============================================================
# GET STORED PREDICTION
# ============================================================

placement_probability = st.session_state.get(
    "placement_probability",
    None
)


# ============================================================
# AI PLACEMENT ADVISOR
# ============================================================

st.divider()

st.header(
    "🤖 AI Placement Advisor"
)


if st.button(
    "✨ Generate AI Advice"
):

    student_data = {

        "CGPA": cgpa,

        "10th_Percentage": tenth,

        "12th_Percentage": twelfth,

        "Backlogs": backlogs,

        "Internships": internships,

        "Projects": projects,

        "Certifications": certifications,

        "Coding_Score": coding,

        "Communication_Score": communication,

        "Aptitude_Score": aptitude,

        "Attendance": attendance
    }


    with st.spinner(
        "🤖 AI is analyzing your profile..."
    ):

        try:

            advice = generate_advice(
                student_data,
                placement_probability
            )

            st.success(
                "AI analysis completed!"
            )

            st.markdown(
                advice
            )

        except Exception as e:

            st.error(
                "❌ AI Advisor Error"
            )

            st.exception(e)


# ============================================================
# AI CHATBOT
# ============================================================

st.divider()

st.header(
    "💬 AI Placement Chatbot"
)

st.write(
    "Ask questions about your placement preparation."
)


question = st.text_input(
    "Ask your question",
    placeholder=(
        "Example: How can I improve my coding skills?"
    )
)


if st.button(
    "🤖 Ask AI"
):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        student_data = {

            "CGPA": cgpa,

            "10th_Percentage": tenth,

            "12th_Percentage": twelfth,

            "Backlogs": backlogs,

            "Internships": internships,

            "Projects": projects,

            "Certifications": certifications,

            "Coding_Score": coding,

            "Communication_Score": communication,

            "Aptitude_Score": aptitude,

            "Attendance": attendance
        }


        with st.spinner(
            "🤖 AI is thinking..."
        ):

            try:

                answer = ask_ai(
                    question,
                    student_data
                )

                st.markdown(
                    "### 🤖 AI Response"
                )

                st.markdown(
                    answer
                )

            except Exception as e:

                st.error(
                    "❌ Chatbot Error"
                )

                st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎓 AI Student Placement Prediction System"
)
