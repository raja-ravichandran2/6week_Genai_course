import streamlit as st

# ----------------------------------------
# Quiz Questions
# ----------------------------------------

questions = [

    {
        "question": "1. Who is known as the God of Cricket?",
        "options": [
            "Virat Kohli",
            "MS Dhoni",
            "Sachin Tendulkar",
            "Rohit Sharma"
        ],
        "answer": "Sachin Tendulkar"
    },

    {
        "question": "2. Which country won 2011 Cricket World Cup?",
        "options": [
            "India",
            "Australia",
            "England",
            "Pakistan"
        ],
        "answer": "India"
    },

    {
        "question": "3. How many players are there in cricket team?",
        "options": [
            "10",
            "11",
            "12",
            "9"
        ],
        "answer": "11"
    },

    {
        "question": "4. Which format contains 20 overs?",
        "options": [
            "ODI",
            "Test",
            "T20",
            "Ranji"
        ],
        "answer": "T20"
    },

    {
        "question": "5. Who is called Captain Cool?",
        "options": [
            "Virat Kohli",
            "MS Dhoni",
            "Rohit Sharma",
            "Gill"
        ],
        "answer": "MS Dhoni"
    },

    {
        "question": "6. Which country plays Ashes series?",
        "options": [
            "India vs Pakistan",
            "England vs Australia",
            "India vs England",
            "Australia vs NZ"
        ],
        "answer": "England vs Australia"
    },

    {
        "question": "7. What is maximum overs in ODI?",
        "options": [
            "20",
            "40",
            "50",
            "90"
        ],
        "answer": "50"
    },

    {
        "question": "8. Which player is called Hitman?",
        "options": [
            "Rohit Sharma",
            "Virat Kohli",
            "Dhoni",
            "Hardik"
        ],
        "answer": "Rohit Sharma"
    },

    {
        "question": "9. IPL stands for?",
        "options": [
            "Indian Premier League",
            "International Premier League",
            "Indian Power League",
            "International Power League"
        ],
        "answer": "Indian Premier League"
    },

    {
        "question": "10. How many wickets in cricket?",
        "options": [
            "8",
            "9",
            "10",
            "11"
        ],
        "answer": "10"
    }

]

# ----------------------------------------
# Streamlit UI
# ----------------------------------------

st.title("🏏 Cricket Sports Quiz")

st.write("Test your cricket knowledge!")

score = 0

user_answers = []

# ----------------------------------------
# Display Questions
# ----------------------------------------

for i, q in enumerate(questions):

    answer = st.radio(
        q["question"],
        q["options"],
        key=i
    )

    user_answers.append(answer)

# ----------------------------------------
# Submit Button
# ----------------------------------------

if st.button("Submit Quiz"):

    for i in range(len(questions)):

        if user_answers[i] == questions[i]["answer"]:
            score += 1

    st.success(f"🏏 Your Score: {score}/10")

    # Performance message
    if score >= 8:
        st.balloons()
        st.write("🔥 Excellent Cricket Knowledge!")

    elif score >= 5:
        st.write("👍 Good Job!")

    else:
        st.write("📚 Keep Learning Cricket!")