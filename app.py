import streamlit as st
import datetime

st.set_page_config(page_title="Bankruptcy Assessment", page_icon="⚖️", layout="centered")

# --- Title ---
st.title("⚖️ Bankruptcy Assessment Chatbot")
st.write("--- Welcome to the Bankruptcy Assessment Chatbot ---")
st.write(
    "Are you contemplating filing for bankruptcy? Take this brief assessment to see if you would be a good candidate for bankruptcy. "
    "If you answer “yes” to more than 7 questions, you should consider contacting an attorney to discuss filing for bankruptcy."
)

# --- Questions ---
questions = [
    "Have you been unable to make the minimum payments on your credit cards for more than 3 months?",
    "Are you behind on your mortgage or rent payments?",
    "Have you received calls or letters from collection agencies?",
    "Are you using one credit card to pay off another?",
    "Have you taken out payday loans to cover regular expenses?",
    "Are you facing wage garnishment?",
    "Do you have medical bills that you are unable to pay?",
    "Do you owe more on your car than it is worth?",
    "Are you borrowing money from family or friends to cover bills?",
    "Have you recently experienced a job loss or significant drop in income?",
    "Are you facing foreclosure or eviction?",
    "Do you have tax debts you cannot pay?",
    "Have you had utilities shut off due to nonpayment?",
    "Are you considering debt consolidation due to overwhelming debt?",
    "Do you feel stressed or overwhelmed by your financial situation?",
]

st.header("Please answer the following questions:")

responses = {}

# Render questions with Yes/No options
for q in questions:
    responses[q] = st.radio(q, ["Yes", "No"], index=None)

# --- Submit button ---
if st.button("Submit Assessment"):
    if None in responses.values():
        st.error("Please answer all questions before submitting.")
    else:
        yes_count = list(responses.values()).count("Yes")
        no_count = list(responses.values()).count("No")

        st.subheader("Assessment Results")

        if yes_count > 7:
            st.success(
                "Based on the interview questions, it is recommended to file for bankruptcy, "
                "and an ILA legal attorney will reach out to you soon."
            )
        else:
            st.warning(
                "Your situation does not seem the best suited for bankruptcy, but your results have been recorded and will be passed along to an attorney."
            )

        st.write("")  # <-- adds the requested space
        st.write("Here are the recorded answers:")

        for q, ans in responses.items():
            st.write(f"**Q:** {q}")
            st.write(f"**A:** {ans}")
            st.write("---")

        # --- Save results to file ---
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"assessment_results_{timestamp}.txt"

        with open(filename, "w") as f:
            for q, a in responses.items():
                f.write(f"{q}\nAnswer: {a}\n\n")

        st.success(f"Your results have been saved as: {filename}")
        st.download_button(
            "Download Your Results",
            data=open(filename, "rb").read(),
            file_name=filename,
            mime="text/plain"
        )
