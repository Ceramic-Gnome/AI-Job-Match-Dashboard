import streamlit as st


def display_metrics(all_jobs, filtered_jobs):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Total Jobs", value=len(all_jobs))

    with col2:
        st.metric(label="Matching Jobs", value=len(filtered_jobs))

    with col3:
        companies = len(set(job.company for job in filtered_jobs))

        st.metric(label="Companies", value=companies)

    with col4:
        average_match = (
            sum(job.match.score for job in filtered_jobs) / len(filtered_jobs)
            if filtered_jobs
            else 0
        )

        st.metric(label="Average Match", value=f"{average_match:.0f}%")
