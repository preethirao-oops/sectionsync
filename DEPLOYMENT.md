# Deploying SectionSync on Render

This repository includes a Render Blueprint in `render.yaml`. The service uses
Gunicorn and stores its SQLite database on a persistent disk mounted at
`/var/data`.

## Deploy

1. Push this project to a GitHub repository.
2. In Render, choose **New + → Blueprint** and connect that repository.
3. Review the `sectionsync` web service and create it. The Blueprint generates
   `SECTION_SYNC_SECRET_KEY` and initializes the database before Gunicorn starts.
4. Open the service URL from the Render dashboard after the deploy finishes.

The persistent disk must remain attached to preserve student and allocation
data between deploys. Render may charge for persistent disks depending on the
selected plan.

## Before making it public

The current application seeds demo accounts, including the administrator
`admin01` / `admin123`, and student test accounts. The student login page also
contains temporary client-side login behavior. Treat this deployment as a
private preview until authentication is replaced with production authentication,
demo credentials are removed, and passwords are stored using a password hash.

Set these environment variables in Render if you deploy without the Blueprint:

- `SECTION_SYNC_SECRET_KEY`: a long random value used to sign sessions.
- `SECTION_SYNC_DATABASE_PATH`: a path on an attached persistent disk, such as
  `/var/data/section_management.db`.

Use `pip install -r requirements.txt` to install dependencies, then
`python -c "from app import create_database; create_database()" && gunicorn app:app`
to start the service.
