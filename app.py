import streamlit as st
import pandas as pd

st.set_page_config(page_title="تحلیل پاسخ آزمون", layout="centered")

st.title("تحلیل پاسخ آزمون چهارگزینه‌ای")
st.write("سؤالات ۱۱ تا ۲۰")

num_students = st.number_input(
    "تعداد دانش‌آموزان را وارد کنید:",
    min_value=1,
    step=1
)

questions = list(range(11, 21))
options = ["الف", "ب", "ج", "د", "نزده"]

responses = []

if num_students > 0:
    st.subheader("ثبت پاسخ‌ها")

    for s in range(int(num_students)):
        st.markdown(f"### دانش‌آموز {s+1}")
        student_answers = []

        for q in questions:
            ans = st.selectbox(
                f"سؤال {q}",
                options,
                key=f"s{s}_q{q}"
            )
            student_answers.append(ans)

        responses.append(student_answers)

    if st.button("نمایش آمار"):
        df = pd.DataFrame(responses, columns=questions)

        st.subheader("آمار نهایی پاسخ‌ها")

        for q in questions:
            st.markdown(f"### سؤال {q}")
            stats = df[q].value_counts().reindex(options, fill_value=0)
            st.table(stats)
