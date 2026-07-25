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
        locations = len(set(job.location for job in filtered_jobs if job.location))

        st.metric(label="Locations", value=locations)
