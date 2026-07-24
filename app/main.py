import streamlit as st
from components.metrics import display_metrics

from repositories.job_repository import JobRepository
from utils.formatting import format_datetime


def main():
    st.set_page_config(
        page_title="AI Job Match Dashboard",
        page_icon="💼",
        layout="wide",
    )

    st.title("💼 AI Job Match Dashboard")
    st.caption("Version 0.2.0 (In Development)")

    repository = JobRepository()
    jobs = repository.get_all_jobs()

    display_metrics(jobs)

    if not jobs:
        st.warning("No jobs found.")
        return

    for job in jobs:
        with st.container():
            st.markdown(f"### {job.title}")
            st.write(f"**Company:** {job.company}")
            st.write(f"**Location:** {job.location}")
            st.write(f"**Posted:** {format_datetime(job.date_posted)}")
            st.markdown("---")


if __name__ == "__main__":
    main()
