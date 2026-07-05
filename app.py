import streamlit as st
from semantic_analysis import analyze

st.set_page_config(page_title="voice based concept understanding analyser")

st.title("Semantic Concept Analysis")

st.markdown("Compare a student's answer with the reference answer using AI semantic similarity.")

reference = st.text_area("Reference Answer")

student = st.text_area("Student Answer")

if st.button("Analyze"):
    if reference.strip() == '''or student.strip() ==''':
        st.warning("please enter both Reference Answer and Student Answer.")
        st.stop()

    score = analyze(reference, student)

    st.subheader("Result")

    st.write(f"Similarity Score :{score:.2f}%")

    st.progress(score/100)

    st.subheader("AI Feedback")

    if score > 80:
        feedback = "Excellent! Your answer matches the reference answer very well"
    elif score > 50:
        feedback = "Good attempt. Some important concepts are missings"
    else:
        feedback = "Your answer is quit differnce from the reference answer. Please review the topic."

    st.write(feedback)

    reference_words = set(reference.lower().split())
    student_words = set(student.lower().split())

    missing = reference_words-student_words

    st.subheader("Missing Concepts")

    if missing:
        for word in list(missing)[:10]:
            st.write("*"+ word)
    else:
        st.success("No major concepts missing.")

    if score > 80:
        st.success("Strong Understanding")
    elif score > 50:
        st.warning("Moderate Understnding")
    else:
        st.error("poor Understanding")

st.markdown("---")
st.caption("Developed by Team")
