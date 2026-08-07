import streamlit as st
from components.analytics import (
    display_analytics,
    display_resume_gap_analysis,
)
from components.filters import apply_filters, display_filters
from components.job_card import display_job_card
from components.job_details import display_job_details
from components.metrics import display_metrics

from matcher.keyword_matcher import KeywordMatcher
from repositories.job_repository import JobRepository
from services.profile_loader import ProfileLoader


def main():
    st.set_page_config(
        page_title="AI Job Match Dashboard",
        page_icon="💼",
        layout="wide",
    )

    st.title("💼 AI Job Match Dashboard")
    st.caption("Version 0.7.0 (In Development)")

    repository = JobRepository()

    profile = ProfileLoader().load()
    matcher = KeywordMatcher()

    all_jobs = repository.get_all_jobs()

    for job in all_jobs:
        job.match = matcher.calculate_match(profile, job)

    filters = display_filters(all_jobs)

    filtered_jobs = apply_filters(all_jobs, filters)

    if "selected_job" not in st.session_state:
        st.session_state.selected_job = None

    display_metrics(all_jobs, filtered_jobs)

    st.caption(f"Showing {len(filtered_jobs)} of {len(all_jobs)} jobs")

    display_analytics(filtered_jobs)

    gap_summary = display_resume_gap_analysis(all_jobs, matcher)

    left_col, right_col = st.columns([2, 3])

    with left_col:

        st.subheader("Available Jobs")

        for job in filtered_jobs:
            display_job_card(job)

    with right_col:

        if st.session_state.selected_job:

            display_job_details(st.session_state.selected_job, gap_summary)

        else:

            st.info("Select a job to view details.")


if __name__ == "__main__":
    main()
