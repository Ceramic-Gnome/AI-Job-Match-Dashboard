import streamlit as st

from utils.formatting import (
    format_datetime,
    get_job_badge,
)


def display_job_card(job):

    with st.container():

        st.markdown(f"### {job.title}")

        badge_text, badge_color = get_job_badge(job.date_posted)

        st.markdown(f":{badge_color}[{badge_text}]")

        st.write(f"🏢 **Company:** {job.company}")

        if job.location:
            st.write(f"📍 **Location:** {job.location}")

        if job.date_posted:
            st.write(f"📅 **Posted:** {format_datetime(job.date_posted)}")

        if job.url:
            st.link_button("View Job Posting", job.url)

        st.markdown("---")
