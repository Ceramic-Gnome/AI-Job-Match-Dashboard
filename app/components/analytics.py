import pandas as pd
import streamlit as st


def display_analytics(jobs):

    st.header("📊 Job Analytics")

    if not jobs:
        st.info("No jobs available for analysis.")
        return

    data = [
        {
            "Company": job.company,
            "Location": job.location,
            "Source": job.source,
            "Date Added": job.date_added,
        }
        for job in jobs
    ]

    df = pd.DataFrame(data)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Jobs by Company")

        company_counts = df["Company"].value_counts()

        st.bar_chart(company_counts)

    with col2:
        st.subheader("Jobs by Location")

        location_counts = df["Location"].fillna("Unknown").value_counts()

        st.bar_chart(location_counts)

    source_counts = df["Source"].value_counts()

    st.subheader("Jobs by Source")

    st.bar_chart(source_counts)

    st.subheader("Jobs Added Over Time")

    df["Date Added"] = pd.to_datetime(df["Date Added"])

    timeline = df["Date Added"].dt.date.value_counts().sort_index()

    timeline.index = timeline.index.map(lambda x: x.strftime("%m-%d-%Y"))

    st.bar_chart(timeline)
