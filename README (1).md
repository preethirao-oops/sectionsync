# SectionSync

SectionSync is a Flask application for managing students, programs, section capacities, student section preferences, and final section allocations.

## Live demo

**Live demo:** [https://sectionsync-z5dw.onrender.com](https://sectionsync-z5dw.onrender.com)

## GitHub repository

[https://github.com/preethirao-oops/Multi-Section-Managment](https://github.com/preethirao-oops/Multi-Section-Managment)

## Features

- Admin dashboard and student management
- Program, section capacity, and CGPA allocation rule management
- Student section preferences
- Final allocation and allocation status views
- Student payment verification and live basket pages
- SQLite database storage

## Requirements

- Python 3.12 (recommended; the Render Blueprint uses Python 3.12.8)
- Git

## Run locally

Clone the repository and enter its directory:

```bash
git clone https://github.com/preethirao-oops/Multi-Section-Managment.git
cd Multi-Section-Managment
```

Create and activate a virtual environment.

**Windows PowerShell:**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install the project libraries, initialize the database, and start the development server:

```bash
python -m pip install -r requirements.txt
python -c "from app import create_database; create_database()"
python app.py
```

Open <http://127.0.0.1:5000> in your browser. The database is created at `database/section_management.db` by default.

## Deploy to Render

This repository includes a `render.yaml` Blueprint. Push the repository to GitHub, then create a new **Blueprint** in Render and connect the repository. Render will install the requirements, initialize the database, and start the app with Gunicorn. The Blueprint configures a persistent disk for the SQLite database; keep that disk attached to retain data across deploys.

For manual configuration, use:

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `python -c "from app import create_database; create_database()" && gunicorn app:app`

Set `SECTION_SYNC_SECRET_KEY` to a long random value and set `SECTION_SYNC_DATABASE_PATH` to a file path on persistent storage. See [DEPLOYMENT.md](DEPLOYMENT.md) for details.

## Demo account and security

The app seeds a demo administrator account for local preview: `admin01` / `admin123`. Change or remove demo credentials before exposing an instance publicly. This project currently includes temporary demo authentication behavior and does not store passwords using a password hash, so treat public deployments as private previews until authentication is made production-ready. Do not use real student or payment data in a public demo.

## Dependencies

Dependencies are listed in [`requirements.txt`](requirements.txt): Flask, Gunicorn, and OpenPyXL.
