import streamlit as st

from components.skill_badges import skill_badge
from utils.formatting import (
    get_job_badge,
    get_match_color,
)


def display_job_details(job, gap_summary):

    st.header("📄 Job Details")

    st.subheader(job.title)

    badge_text, badge_color = get_job_badge(job.date_posted)

    st.markdown(f":{badge_color}[{badge_text}]")

    st.write(f"**Company:** {job.company}")

    if job.location:
        st.write(f"**Location:** {job.location}")

    st.write(f"**Source:** {job.source}")

    st.divider()

    st.subheader("🎯 Match Analysis")

    color = get_match_color(job.match.score)

    st.markdown(f"### 🎯 Match Score: :{color}[{job.match.score:.0f}%]")

    st.progress(job.match.score / 100)

    st.subheader("📊 Match Breakdown")

    st.write(
        f"Matched **{job.match.matched_count}** of "
        f"**{job.match.required_count}** required skills."
    )

    left, right = st.columns(2)

    with left:
        st.markdown("#### ✅ Matched Skills")

        if job.match.matched_skills:
            for skill in job.match.matched_skills:
                skill_badge(skill, matched=True)
        else:
            st.caption("No matched skills")

    with right:
        st.markdown("#### ❌ Missing Skills")

        if job.match.missing_skills:
            for skill in job.match.missing_skills:
                skill_badge(skill, matched=False)
        else:
            st.caption("None")

    st.divider()

    st.subheader("📈 Resume Gap Impact")

    gaps = gap_summary[gap_summary["Skill"].isin(job.match.missing_skills)].sort_values(
        "Gap Priority",
        ascending=False,
    )

    if gaps.empty:
        st.caption("No prioritized gaps found.")

    else:
        for _, row in gaps.iterrows():

            skill = row["Skill"]
            priority = int(row["Gap Priority"])
            count = int(row["Missing_Count"])

            if priority >= 15:
                icon = "🔴"
                level = "High priority gap"
            elif priority >= 8:
                icon = "🟡"
                level = "Medium priority gap"
            else:
                icon = "🟢"
                level = "Low priority gap"

            st.markdown(f"### {icon} {skill}")

            st.caption(level)

            st.write(f"Missing in **{count}** imported jobs")

    st.divider()

    st.header("💪 Resume Strengths")

    if job.match.matched_skills:

        st.write("Your current resume already aligns well with these skills:")

        for skill in job.match.matched_skills:
            skill_badge(skill, matched=True)

    else:

        st.caption("No matching skills identified.")

    st.divider()

    st.subheader("Description")

    st.write(job.description or "No description available.")

    if job.url:
        st.link_button("🌐 Apply on Company Website", job.url)
