

# SectionSync

**Student section allocation, made simple.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-46E3B7?logo=render&logoColor=white)](https://sectionsync-z5dw.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)



---

## About the Project

SectionSync is a Flask web application that helps institutions manage students, programs, section capacities, and student section preferences, and produces final section allocations based on capacity limits and CGPA-based allocation rules.

## Project Repository

🔗 **GitHub:** [https://github.com/preethirao-oops/sectionsync](https://github.com/preethirao-oops/sectionsync)

## Live Demo

🚀 **Live Demo:** [https://sectionsync-z5dw.onrender.com](https://sectionsync-z5dw.onrender.com)

> The demo is a private preview. See [Demo Account and Security](#demo-account-and-security) before using it.

---

## Table of Contents

- [Folder Structure](#folder-structure)
- [Modules](#modules)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Demo Account and Security](#demo-account-and-security)
- [Contributing](#contributing)

---

## Folder Structure

```text
sectionsync/
├── database/                              # SQLite database storage
├── static/                                # Static assets (CSS, JavaScript, images)
├── template_sources/                      # HTML template sources
├── .gitignore                             # Files and folders ignored by Git
├── DEPLOYMENT.md                          # Detailed deployment guide
├── README.md                              # Project documentation
├── app.py                                 # Flask application, routes, and database setup
├── render.yaml                            # Render Blueprint for deployment
├── requirements.txt                       # Python dependencies
├── sample_allocation_students.xlsx        # Sample student data for allocation
└── sample_students_allocation_test.xlsx   # Sample student data for allocation testing
```

## Modules

| Module                    | Description                                                                 |
| ------------------------- | --------------------------------------------------------------------------- |
| **Admin Dashboard**       | Central overview and control panel for administrators                       |
| **Student Management**    | Add, view, and manage student records                                       |
| **Program Management**    | Create and maintain academic programs                                       |
| **Section Capacity**      | Define the seat capacity of each section                                    |
| **Allocation Rules**      | Configure CGPA-based rules used to allocate sections                        |
| **Student Preferences**   | Let students submit their preferred sections                                |
| **Final Allocation**      | Generate final section allocations and view allocation status               |
| **Payment Verification**  | Verify student payments                                                     |
| **Live Basket**           | Live basket pages for students                                              |

## Features

- **Admin dashboard** with student, program, and section management
- **Configurable capacities** for every section
- **CGPA allocation rules** to drive fair, rule-based allocation
- **Student preference submission** for sections
- **Final allocation and status views** for transparent results
- **Payment verification** and **live basket** pages for students
- **SQLite storage** for a simple, zero-configuration database
- **One-click deployment** to Render using a Blueprint

## Tech Stack

| Layer          | Technology            |
| -------------- | --------------------- |
| Language       | Python 3.12           |
| Backend        | Flask                 |
| Database       | SQLite                |
| Excel handling | OpenPyXL              |
| Web server     | Gunicorn              |
| Hosting        | Render                |

---

## Getting Started

### Prerequisites

- [Python 3.12](https://www.python.org/downloads/) (recommended; the Render Blueprint uses Python 3.12.8)
- [Git](https://git-scm.com/)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/preethirao-oops/sectionsync.git
cd sectionsync
```

**2. Create and activate a virtual environment**

Windows (PowerShell):

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Initialize the database**

```bash
python -c "from app import create_database; create_database()"
```

**5. Start the development server**

```bash
python app.py
```

Open <http://127.0.0.1:5000> in your browser. By default, the database is created at `database/section_management.db`.

## Configuration

| Variable                     | Description                                               | Required in production |
| ---------------------------- | --------------------------------------------------------- | :--------------------: |
| `SECTION_SYNC_SECRET_KEY`    | Long, random secret used to sign sessions                 |           Yes          |
| `SECTION_SYNC_DATABASE_PATH` | File path of the SQLite database (use persistent storage) |           Yes          |

## Deployment

### Deploy to Render (recommended)

The repository includes a `render.yaml` Blueprint.

1. Push the repository to GitHub.
2. In Render, create a new **Blueprint** and connect the repository.
3. Render installs the requirements, initializes the database, and starts the app with Gunicorn.

The Blueprint configures a persistent disk for the SQLite database. Keep this disk attached to retain data across deploys.

### Manual configuration

| Setting       | Value                                                                                |
| ------------- | ------------------------------------------------------------------------------------ |
| Build command | `pip install -r requirements.txt`                                                    |
| Start command | `python -c "from app import create_database; create_database()" && gunicorn app:app` |

Set the variables from [Configuration](#configuration). For more details, see [DEPLOYMENT.md](DEPLOYMENT.md).

## Demo Account and Security

> [!WARNING]
> This project currently uses temporary demo authentication and does **not** store passwords as hashes. Treat public deployments as private previews until authentication is made production-ready.

The app seeds a demo administrator account for local preview:

| Username  | Password   |
| --------- | ---------- |
| `admin01` | `admin123` |

Before exposing an instance publicly:

- Change or remove the demo credentials.
- Set a strong `SECTION_SYNC_SECRET_KEY`.
- Do not use real student or payment data in a public demo.

## Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

You can also browse [open issues](https://github.com/preethirao-oops/sectionsync/issues).

---

<div align="center">

Built with Flask · [Live Demo](https://sectionsync-z5dw.onrender.com) · [GitHub](https://github.com/preethirao-oops/sectionsync)

</div>
