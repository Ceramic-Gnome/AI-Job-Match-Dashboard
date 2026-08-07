# AI Job Match Dashboard

An end-to-end data engineering and AI portfolio project that automates the process of collecting, storing, analyzing, and matching job postings to a candidate's skills and experience.

The long-term goal of this project is to create an intelligent job search assistant that collects jobs from multiple sources, stores them in a local database, analyzes how well each position matches a resume, and provides an interactive dashboard for tracking opportunities.

---

## Project Goals

This project is designed to demonstrate practical software engineering and data engineering skills, including:

- Python application development
- SQLAlchemy ORM
- SQLite and relational databases
- ETL pipeline design
- REST API integration
- Streamlit dashboards and data visualization
- Analytics and reporting workflows
- AI-assisted resume and job matching

---

## Current Capabilities

The current version of the application can:

### Data Pipeline

- Import job postings from JSON
- Store jobs in SQLite
- Prevent duplicate imports
- Use a modular collector/importer architecture
- Separate database access through a repository layer

### Streamlit Dashboard

- Display job postings through an interactive dashboard
- Display weighted AI job match scores
- Visualize match progress with progress bars
- Expand job cards to view matched and missing skills
- Search jobs by keyword
- Filter jobs by:
  - Company
  - Location
  - Minimum Match Score
- Sort jobs by:
  - Match Score
  - Posting date
  - Company name
  - Job title
- Display analytics visualizations:
  - Match score distribution
  - Average match score
  - Highest match score
  - Jobs by company
  - Jobs by location
  - Jobs by source
  - Jobs added over time
- Resume Gap Analysis with weighted skill prioritization

---

## Planned Features

- Interactive Job Details page
- Resume parsing
- AI resume optimization recommendations
- AI-generated cover letters
- Application tracking
- Workday collector
- Additional job source integrations

---

## Project Status

**Current Version**

**v0.7.0 - Interactive Job Analysis and Resume Gap Insights**

### Completed

- Project structure
- SQLite database
- SQLAlchemy models
- JobData dataclass
- Sample job collector
- Job importer
- Duplicate detection
- Utility functions
- Streamlit dashboard
- Dashboard analytics and data visualization
- Greenhouse API collectors
- Lever API collector
- Multi-source job ingestion
- Source tracking
- Source analytics
- Candidate profile support
- Configurable skill database
- Weighted keyword matching
- Match score calculation
- Match progress bars
- Match score sorting
- Match score filtering
- Match analytics dashboard
- Resume gap analysis
- Weighted gap prioritization
- Interactive Job Details
- Match Analysis
- Resume Gap Impact
- Resume Strengths
- HTML Description Cleaning

### Currently Working On

- Advanced Filtering
- Saved Jobs
- Resume Optimizer
- Company Insights
- AI Resume Suggestions

---

## Roadmap

| Version | Milestone | Status |
|----------|-----------|--------|
| v0.1.0 | ETL Foundation | ✅ Complete |
| v0.2.0 | Streamlit Dashboard Foundation | ✅ Complete |
| v0.3.0 | Dashboard Search, Filtering, Sorting, and Job Badges | ✅ Complete |
| v0.4.0 | Analytics Dashboard | ✅ Complete |
| v0.5.0 | Live Job Collectors | ✅ Complete |
| v0.6.0 | AI Job Matching & Resume Gap Analysis | ✅ Complete |
| v0.7.0 | Interactive Job Analysis & Resume Gap Insights | ✅ Complete |
| v0.8.0 | AI Cover Letter Generation | 🚧 In Progress |
| v1.0.0 | Stable Public Release | 📅 Planned |

---

## Architecture

```
               +----------------------+
               |     Job Sources      |
               | JSON • APIs • Files  |
               +----------+-----------+
                          |
                          v
               +----------------------+
               |      Collectors      |
               +----------+-----------+
                          |
                          v
               +----------------------+
               |       JobData        |
               +----------+-----------+
                          |
                          v
               +----------------------+
               |    Job Importer      |
               +----------+-----------+
                          |
                          v
               +----------------------+
               |   SQLite Database    |
               +----------+-----------+
                          |
                          v
               +----------------------+
               | Candidate Profile    |
               +----------+-----------+
                          |
                          v
               +----------------------+
               | AI Job Matcher       |
               +----------+-----------+
                          |
                          v
               +----------------------+
               | Streamlit Dashboard  |
               | Analytics & Gap      |
               | Analysis             |
               +----------------------+
```

---

## Project Structure

```
AI-Job-Match-Dashboard/
│
├── app/              # Streamlit application
├── collectors/       # Job collectors
├── data/             # Sample and imported data
├── database/         # SQLAlchemy models and database connection
├── matcher/          # AI job matching logic
├── models/           # Application data models
├── scripts/          # Utility scripts
├── services/         # Business logic
├── tests/            # Unit tests
├── utils/            # Helper functions
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Technologies

### Current

- Python
- Streamlit
- SQLAlchemy
- SQLite
- Pandas
- JSON
- Regular Expressions (re)
- Git
- GitHub

### Planned

- OpenAI API
- LangChain (possibly)
- PostgreSQL
- Docker
- Additional job APIs

---

## Installation

Clone the repository.

```bash
git clone https://github.com/Ceramic-Gnome/AI-Job-Match-Dashboard.git
```

Navigate to the project.

```bash
cd AI-Job-Match-Dashboard
```

Create a virtual environment.

```bash
py -m venv .venv
```

Activate it.

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create the database.

```bash
py -m database.setup
```

---

## Running the Project

### Activate the Virtual Environment

Activate the Python virtual environment before running the application.

```powershell
.\.venv\Scripts\Activate.ps1
```

### Initialize the Database

Create the SQLite database and tables.

```bash
py -m database.setup
```

### Import Sample Jobs

Load sample job postings into the database.

```bash
py -m scripts.import_jobs
```

### View Imported Jobs (Optional)

Verify imported jobs from the command line.

```bash
py -m scripts.view_jobs
```

### Launch the Dashboard

Start the Streamlit dashboard.

```bash
py -m streamlit run app/main.py
```

The dashboard provides:

- AI-powered job matching
- Match score progress bars
- Matched and missing skill breakdowns
- Resume Gap Analysis
- Match analytics
- Keyword search
- Company filtering
- Location filtering
- Minimum Match Score filtering
- Job sorting
- Job freshness indicators

---

## Why I Built This Project

As I transition from Network Operations into Data Analytics and AI, I wanted to build a project that combines software engineering, databases, ETL pipelines, dashboards, and AI into a practical application.

Rather than building isolated examples, this project demonstrates how these technologies work together to solve a real-world problem.

---

## License

This project is licensed under the MIT License.
