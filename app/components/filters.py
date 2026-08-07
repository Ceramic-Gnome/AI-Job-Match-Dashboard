import streamlit as st


def display_filters(all_jobs):

    st.sidebar.header("Job Filters")

    st.sidebar.caption(f"{len(all_jobs)} jobs available")

    search_term = st.sidebar.text_input("Search keywords")

    companies = sorted({job.company for job in all_jobs})

    selected_company = st.sidebar.selectbox("Company", ["All"] + companies)

    locations = sorted({job.location for job in all_jobs if job.location})

    selected_location = st.sidebar.selectbox("Location", ["All"] + locations)

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

    return {
        "search": search_term,
        "company": selected_company,
        "location": selected_location,
        "sort": sort_option,
        "min_match": min_match,
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
    if filters["min_match"] > 0:

        filtered_jobs = [
            job for job in filtered_jobs if job.match.score >= filters["min_match"]
        ]

    # Sort the filtered jobs
    if filters["sort"] == "Match Score":
        filtered_jobs = sorted(
            filtered_jobs,
            key=lambda job: (
                job.match.score,
                job.date_posted or job.date_added,
            ),
            reverse=True,
        )
    elif filters["sort"] == "Newest First":
        filtered_jobs = sorted(
            filtered_jobs,
            key=lambda job: job.date_posted or job.date_added,
            reverse=True,
        )

    elif filters["sort"] == "Oldest First":
        filtered_jobs = sorted(
            filtered_jobs,
            key=lambda job: job.date_posted or job.date_added,
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
