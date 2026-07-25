import streamlit as st
from components.filters import apply_filters, display_filters
from components.job_card import display_job_card
from components.metrics import display_metrics

from repositories.job_repository import JobRepository


def main():
    st.set_page_config(
        page_title="AI Job Match Dashboard",
        page_icon="💼",
        layout="wide",
    )

    st.title("💼 AI Job Match Dashboard")
    st.caption("Version 0.2.0 (In Development)")

    repository = JobRepository()

    all_jobs = repository.get_all_jobs()

    filters = display_filters(all_jobs)

    filtered_jobs = apply_filters(all_jobs, filters)

    display_metrics(all_jobs, filtered_jobs)

    st.caption(f"Showing {len(filtered_jobs)} of {len(all_jobs)} jobs")

    for job in filtered_jobs:
        display_job_card(job)


if __name__ == "__main__":
    main()
