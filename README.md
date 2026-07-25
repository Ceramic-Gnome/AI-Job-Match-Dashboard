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
- Streamlit dashboards
- AI-assisted resume and job matching
- Git and GitHub workflow

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
- Show job summary metrics
- Search jobs by keyword
- Filter jobs by company and location
- Sort jobs by:
  - Posting date
  - Company name
  - Job title
- Display job freshness indicators:
  - New Today
  - This Week
  - Older

---

## Planned Features

- Streamlit dashboard
- Greenhouse API collector
- Lever API collector
- Workday collector
- Resume parsing
- AI-powered job matching
- Cover letter generation
- Application tracking
- Dashboard analytics

---

## Project Status

**Current Version**

**v0.3.0 (Pre-release)**

### Completed

- Project structure
- SQLite database
- SQLAlchemy models
- JobData dataclass
- Sample job collector
- Job importer
- Duplicate detection
- Utility functions

### Currently Working On

- Analytics

---

## Roadmap

| Version | Milestone | Status |
|----------|-----------|--------|
| v0.1.0 | ETL Foundation | ✅ Complete |
| v0.2.0 | Streamlit Dashboard Foundation | ✅ Complete |
| v0.3.0 | Dashboard Search, Filtering, Sorting, and Job Badges | ✅ Complete |
| v0.4.0 | Analytics Dashboard | 📅 Planned |
| v0.5.0 | Live Job Collectors | 📅 Planned |
| v0.6.0 | AI Job Matching | 📅 Planned |
| v0.7.0 | Resume Optimization | 📅 Planned |
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
               |  Streamlit Dashboard |
               +----------+-----------+
                          |
                          v
               +----------------------+
               |   AI Job Matching    |
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

The dashboard will open in your browser and provide:

- Job summary metrics
- Keyword search
- Company filtering
- Location filtering
- Job sorting
- Job freshness indicators

---

## Why I Built This Project

As I transition from Network Operations into Data Analytics and AI, I wanted to build a project that combines software engineering, databases, ETL pipelines, dashboards, and AI into a practical application.

Rather than building isolated examples, this project demonstrates how these technologies work together to solve a real-world problem.

---

## License

This project is licensed under the MIT License.
