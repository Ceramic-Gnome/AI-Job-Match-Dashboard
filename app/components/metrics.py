import streamlit as st


def display_metrics(jobs):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Jobs Imported", value=len(jobs))

    with col2:
        companies = len(set(job.company for job in jobs))

        st.metric(label="Companies", value=companies)

    with col3:
        locations = len(set(job.location for job in jobs))

        st.metric(label="Locations", value=locations)
