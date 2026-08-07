import streamlit as st

from utils.formatting import (
    format_datetime,
    get_job_badge,
    get_match_color,
)


def display_job_card(job):

    with st.container():

        st.markdown(f"### {job.title}")

        color = get_match_color(job.match.score)

        st.progress(job.match.score / 100)

        st.markdown(f"🎯 **Match Score:** :{color}[{job.match.score:.0f}%]")

        with st.expander("View skill match"):
            st.write("**Matched Skills**")
            st.write(", ".join(job.match.matched_skills) or "None")

            st.write("**Missing Skills**")
            st.write(", ".join(job.match.missing_skills) or "None")

        badge_text, badge_color = get_job_badge(job.date_posted)

        st.markdown(f":{badge_color}[{badge_text}]")

        st.write(f"🏢 **Company:** {job.company}")

        if job.location:
            st.write(f"📍 **Location:** {job.location}")
        else:
            st.write("📍 **Location:** Not specified")

        st.write(f"🔗 **Source:** {job.source}")

        if job.date_posted:
            st.write(f"📅 **Posted:** {format_datetime(job.date_posted)}")

        if job.url:
            st.link_button("🌐 Apply on Company Website", job.url)

        if st.button("View Job Details", key=f"details_{job.url}"):
            st.session_state.selected_job = job

        st.markdown("---")
