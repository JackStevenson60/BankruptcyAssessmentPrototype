import streamlit as st
import datetime

st.set_page_config(page_title="Bankruptcy Assessment Tool")

# --- Title ---
st.title("Bankruptcy Assessment Tool")
st.write("""
Are you contemplating filing for bankruptcy? Take this brief assessment to see if you would be a good candidate for bankruptcy.  

Disclaimer: The use of the Bankruptcy Assessment Tool is not a substitute for legal advice from a licensed attourney.
""")
st.write("Please answer the following questions:")

# --- Original Questions (unchanged) ---
script_questions = [
    {"id": "q1", "text": "Do you own a home?"}, 

    {"id": "q2", "text": "Do you own a vehicle?"}, 

    {"id": "q3", "text": "Do you own one vehicle worth up to $7,000?"},

    {"id": "q4", "text": "Do you have a job that pays you? (e.g. salaries, bonueses, commissions, wages)"},

    {"id": "q5", "text": "Do you plan to keep a job?"},

    {"id": "q6", "text": "Are you up-to-date on your child support or alimony payments (if applicable)?"},

    {"id": "q7", "text": "Are all of your past-due taxes paid?"},

    {"id": "q8", "text": "Do you have a debt that is causing you barriers?"}, 

    {"id": "q9", "text": "Is this your first time filing for bankruptcy? If not, has it at least been eight years since your last filing?"},

    {"id": "q10", "text": "Is most of your debt all one kind (credit card, student loans, medical bills, personal loans, etc.)?"},

    {"id": "q11", "text": "Is part of your income being taken due to debts you owe?"},

    {"id": "q12", "text": "Is your driver's license currently suspended due to court debt?"}, 
    
    {"id": "q13", "text": "Did you incur any of your debt through fraudulent activity?"}, 

    {"id": "q14", "text": "Do you have any upcoming court hearings related to your debts?"},

    {"id": "q15", "text": "Has any creditor sued you or obtained a judgment against you for unpaid debts?"}, 

]

user_answers = {}

# --- Display questions ---
st.write("---")

for q in script_questions:
    st.subheader(q["text"])

    # Radio button with no default selection
    answer = st.radio(
        f"",
        ["Yes", "No"],
        index=None,
        key=q["id"]
    )

    user_answers[q["id"]] = answer

st.write("---")

# --- Process when button is clicked ---
if st.button("Submit Assessment"):

    # Count yes/no answers
    yes_count = sum(1 for a in user_answers.values() if a == "Yes")
    no_count = sum(1 for a in user_answers.values() if a == "No")

    st.subheader("Interview Complete!")

    # Recommendation logic
    output_lines = []
    output_lines.append("--- Chatbot Interview Summary ---")
    output_lines.append(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    if yes_count >= 7:
        msg = ("Based on your answers, bankruptcy may help you with your debt. "
               "Contact Iowa Legal Aid or Iowa Find A Lawyer, to be refered to a bankruptcy attorney."
               "Representation is not guaranteed.")
        st.success(msg)
        output_lines.append(msg)
        output_lines.append("")

    elif no_count >= 7:
        msg = ("Your situation does not seem the best suited for bankruptcy."
               "Contact Iowa Legal Aid or Iowa Find A Lawyer, for further questions.")
        
        st.warning(msg)
        output_lines.append(msg)
        output_lines.append("")

    # Display summary
    st.write("### Here are the recorded answers:")
    for q in script_questions:
        line = f"- {q['text']}: {user_answers[q['id']].upper() if user_answers[q['id']] else 'N/A'}"
        st.write(line)
        output_lines.append(line)

    # Save results file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"bankruptcy_assessment_results_{timestamp}.txt"
    file_content = "\n".join(output_lines)

    st.download_button(
        label="Download Results File",
        data=file_content,
        file_name=filename,
        mime="text/plain"
    )

    st.success("Assessment complete. You may download your results file now.")

