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
            "Match Score": job.match.score,
        }
        for job in jobs
    ]

    df = pd.DataFrame(data)

    st.subheader("🎯 Match Analytics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average Match", f"{df['Match Score'].mean():.0f}%")

    with col2:
        st.metric("Highest Match", f"{df['Match Score'].max():.0f}%")

    with col3:
        excellent = (df["Match Score"] >= 75).sum()

        st.metric("75%+ Matches", excellent)

    st.subheader("Match Score Distribution")

    match_bins = pd.cut(
        df["Match Score"],
        bins=[0, 25, 50, 75, 100],
        labels=["0-25", "26-50", "51-75", "76-100"],
        include_lowest=True,
    )

    st.bar_chart(match_bins.value_counts().sort_index())

    st.subheader("Average Match by Company")

    company_match = (
        df.groupby("Company")["Match Score"].mean().sort_values(ascending=False)
    )

    st.bar_chart(company_match)

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


def display_resume_gap_analysis(jobs, matcher):

    st.subheader("📌 Resume Gap Analysis")

    missing_skills = []

    for job in jobs:

        if hasattr(job, "match"):

            for skill in job.match.missing_skills:

                missing_skills.append(
                    {
                        "Skill": skill,
                        "Weight": matcher.skill_weights.get(skill, 1),
                    }
                )

    if not missing_skills:
        st.success("No skill gaps identified.")
        return

    gap_df = pd.DataFrame(missing_skills)

    gap_summary = gap_df.groupby("Skill").agg(
        Missing_Count=("Skill", "count"),
        Weight=("Weight", "max"),
    )

    gap_summary["Gap Priority"] = gap_summary["Missing_Count"] * gap_summary["Weight"]

    gap_summary = gap_summary.sort_values(
        by="Gap Priority",
        ascending=False,
    )

    st.write(
        "Skills most frequently missing from your profile, "
        "prioritized by importance:"
    )

    st.dataframe(gap_summary)

    st.bar_chart(gap_summary["Gap Priority"])
