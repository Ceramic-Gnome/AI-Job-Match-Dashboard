from datetime import datetime, timedelta

import streamlit as st

from utils.formatting import ensure_utc


def get_job_datetime(job):

    return ensure_utc(job.date_posted or job.date_added)


def display_filters(all_jobs):

    st.sidebar.header("Job Filters")

    st.sidebar.caption(f"{len(all_jobs)} jobs available")

    search_term = st.sidebar.text_input("Search keywords")

    companies = sorted({job.company for job in all_jobs})

    selected_company = st.sidebar.selectbox("Company", ["All"] + companies)

    locations = sorted({job.location for job in all_jobs if job.location})

    selected_location = st.sidebar.selectbox("Location", ["All"] + locations)

    work_type_options = sorted({job.work_type for job in all_jobs if job.work_type})

    selected_work_types = st.sidebar.multiselect(
        "Work Arrangement",
        work_type_options,
    )

    sort_option = st.sidebar.selectbox(
        "Sort By",
        [
            "Match Score",
            "Newest First",
            "Oldest First",
            "Company (A–Z)",
            "Company (Z–A)",
            "Job Title (A–Z)",
            "Job Title (Z–A)",
        ],
    )

    min_match = st.sidebar.slider(
        "Minimum Match Score (%)",
        min_value=0,
        max_value=100,
        value=0,
        step=5,
    )

    missing_skill_options = sorted(
        {
            skill
            for job in all_jobs
            if hasattr(job, "match")
            for skill in job.match.missing_skills
        }
    )

    selected_missing_skills = st.sidebar.multiselect(
        "Missing Skills",
        missing_skill_options,
    )

    posted_within = st.sidebar.selectbox(
        "Posted Within",
        [
            "Any Time",
            "Last 24 Hours",
            "Last 7 Days",
            "Last 30 Days",
            "Last 90 Days",
        ],
    )

    return {
        "search": search_term,
        "company": selected_company,
        "location": selected_location,
        "work_types": selected_work_types,
        "sort": sort_option,
        "min_match": min_match,
        "missing_skills": selected_missing_skills,
        "posted_within": posted_within,
    }


def apply_filters(jobs, filters):

    filtered_jobs = jobs

    if filters["search"]:
        search = filters["search"].lower()

        filtered_jobs = [
            job
            for job in filtered_jobs
            if (
                search in job.title.lower()
                or search in job.company.lower()
                or search in (job.description or "").lower()
            )
        ]

    if filters["company"] != "All":

        filtered_jobs = [
            job for job in filtered_jobs if job.company == filters["company"]
        ]

    if filters["location"] != "All":

        filtered_jobs = [
            job for job in filtered_jobs if job.location == filters["location"]
        ]

    if filters["work_types"]:

        filtered_jobs = [
            job for job in filtered_jobs if job.work_type in filters["work_types"]
        ]

    if filters["min_match"] > 0:

        filtered_jobs = [
            job for job in filtered_jobs if job.match.score >= filters["min_match"]
        ]

    if filters["missing_skills"]:

        filtered_jobs = [
            job
            for job in filtered_jobs
            if any(
                skill in job.match.missing_skills for skill in filters["missing_skills"]
            )
        ]

    if filters["posted_within"] != "Any Time":

        now = datetime.now().astimezone()

        days = {
            "Last 24 Hours": 1,
            "Last 7 Days": 7,
            "Last 30 Days": 30,
            "Last 90 Days": 90,
        }

        cutoff = now - timedelta(days=days[filters["posted_within"]])

        filtered_jobs = [
            job
            for job in filtered_jobs
            if get_job_datetime(job) and get_job_datetime(job) >= cutoff
        ]

    # Sort the filtered jobs
    if filters["sort"] == "Match Score":
        filtered_jobs = sorted(
            filtered_jobs,
            key=lambda job: (
                job.match.score,
                get_job_datetime(job),
            ),
            reverse=True,
        )
    elif filters["sort"] == "Newest First":
        filtered_jobs = sorted(
            filtered_jobs,
            key=get_job_datetime,
            reverse=True,
        )

    elif filters["sort"] == "Oldest First":
        filtered_jobs = sorted(
            filtered_jobs,
            key=get_job_datetime,
        )

    elif filters["sort"] == "Company (A–Z)":
        filtered_jobs = sorted(
            filtered_jobs,
            key=lambda job: job.company.lower(),
        )

    elif filters["sort"] == "Company (Z–A)":
        filtered_jobs = sorted(
            filtered_jobs,
            key=lambda job: job.company.lower(),
            reverse=True,
        )

    elif filters["sort"] == "Job Title (A–Z)":
        filtered_jobs = sorted(
            filtered_jobs,
            key=lambda job: job.title.lower(),
        )

    elif filters["sort"] == "Job Title (Z–A)":
        filtered_jobs = sorted(
            filtered_jobs,
            key=lambda job: job.title.lower(),
            reverse=True,
        )

    return filtered_jobs
