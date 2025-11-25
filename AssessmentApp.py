import streamlit as st
import datetime

st.set_page_config(page_title="Bankruptcy Assessment Chatbot")

# --- Title ---
st.title("Bankruptcy Assessment Chatbot")
st.write("""
Are you contemplating filing for bankruptcy? Take this brief assessment to see if you would be a good candidate for bankruptcy.  
If you answer “yes” to more than **7 questions**, you should consider contacting an attorney to discuss filing for bankruptcy.
""")
st.write("Please answer the following questions:")

# --- Original Questions (unchanged) ---
script_questions = [
    {"id": "q1", "text": "Do you own a home?", 
     "note": "Note: Iowa recognizes the Homestead Exemption, which protects a home of an unlimited value during the course of a bankruptcy, with a few exceptions."},

    {"id": "q2", "text": "Do you have any garnishable income?", 
     "note": "Note: garnishable income includes wages, salaries, commissions and bonuses but does NOT include government benefits like Social Security, workers' compensation and child or spousal support."},

    {"id": "q3", "text": "Has any creditor sued you or obtained a judgment against you for unpaid debts?"},

    {"id": "q4", "text": "Are you currently losing income because of your debts?"},

    {"id": "q5", "text": "Is this your first time filing for bankruptcy? If not, has it at least been eight years since your last filing?", 
     "note": "Note: you may only file for Chapter 7 bankruptcy once every eight years."},

    {"id": "q6", "text": "Is most of your debt all one kind (credit card, student loans, medical bills, personal loans, etc.)?"},

    {"id": "q7", "text": "Do you have one debt in particular that is causing you barriers?"},

    {"id": "q8", "text": "Are your wages currently being garnished?", 
     "note": "Note: this means that a judgment has already been entered against you by a creditor who is actively collecting from your income, typically through paychecks by your employer."},

    {"id": "q9", "text": "Do you have any upcoming court hearings related to your debts?"},

    {"id": "q10", "text": "Are you up-to-date on your child support or alimony payments (if applicable)?"},

    {"id": "q11", "text": "Is your driver's license currently suspended due to court debt or getting into an auto accident without auto insurance?"},

    {"id": "q12", "text": "Are you anticipating maintaining a job and having a steady income for the next two years?", 
     "note": "Note: The timing of filing bankruptcy is very important. If you know you won’t have an income in the foreseeable future (whether it be due to going to school full time, staying home with the kids, etc.), it might be best to wait to file since you won’t have any income to lose."},

    {"id": "q13", "text": "Did you incur any of your debt through fraudulent activity?", 
     "note": "Note: Any debts incurred through fraud are not dischargeable."},

    {"id": "q14", "text": "Are all of your past-due taxes paid and current?"},

    {"id": "q15", "text": "Do you own a vehicle?"},

    {"id": "q16", "text": "Do you only own one vehicle?", 
     "note": "Note: You may only own one vehicle with equity worth $7,000 when you file bankruptcy."}
]

user_answers = {}

# --- Display questions ---
st.write("---")

for q in script_questions:
    st.subheader(q["text"])

    if "note" in q:
        st.info(q["note"])

    # Radio button with no default selection
    answer = st.radio(
        f"Your answer to: **{q['text']}**",
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
        msg = ("Based on the interview questions, it is recommended to file for bankruptcy, "
               "and an ILA legal attorney will reach out to you soon.")
        st.success(msg)
        output_lines.append(msg)
        output_lines.append("")

    elif no_count >= 7:
        msg = ("Your situation does not seem the best suited for bankruptcy, but your results "
               "have been recorded and will be passed along to an attorney.")
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
