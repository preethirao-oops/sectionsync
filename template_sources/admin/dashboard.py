"""Python source for the admin/dashboard.html page template."""

TEMPLATE_SOURCE = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Admin Dashboard - SectionSync</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f7f7fb;
            color: #27263a;
        }

        /* SIDEBAR */
        .sidebar {
            position: fixed;
            left: 0;
            top: 0;
            width: 250px;
            height: 100vh;
            background: #25233d;
            color: white;
            padding: 25px 15px;
            overflow-y: auto;
        }

        .logo {
            font-size: 25px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 8px;
        }

        .panel-name {
            text-align: center;
            color: #bdb9d2;
            font-size: 13px;
            margin-bottom: 30px;
        }

        .menu-title {
            color: #9692ad;
            font-size: 11px;
            font-weight: bold;
            text-transform: uppercase;
            margin: 18px 10px 8px;
        }

        .sidebar a {
            display: block;
            text-decoration: none;
            color: #d8d5e4;
            padding: 11px 14px;
            margin: 3px 0;
            border-radius: 8px;
            font-size: 14px;
            transition: 0.2s;
        }

        .sidebar a:hover {
            background: #353250;
            color: white;
        }

        .sidebar a.active {
            background: #d8c5ff;
            color: #25233d;
            font-weight: bold;
        }

        .submenu a {
            padding-left: 32px;
            font-size: 13px;
        }

        .logout {
            margin-top: 25px !important;
            color: #ffb6b6 !important;
        }

        /* MAIN CONTENT */
        .main {
            margin-left: 250px;
            padding: 35px 40px;
            min-height: 100vh;
        }

        .top-section {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
        }

        .page-title h1 {
            font-size: 28px;
            margin-bottom: 7px;
        }

        .page-title p {
            color: #77758a;
            font-size: 14px;
        }

        .admin-badge {
            background: white;
            border: 1px solid #e6e3ef;
            padding: 10px 17px;
            border-radius: 10px;
            color: #6240b8;
            font-size: 13px;
            font-weight: bold;
        }

        /* WELCOME CARD */
        .welcome-card {
            background: linear-gradient(135deg, #7845e8, #713ce6);
            color: white;
            border-radius: 16px;
            padding: 32px 35px;
            margin-top: 20px;
            box-shadow: 0 8px 25px rgba(113, 60, 230, 0.15);
        }

        .welcome-card h2 {
            font-size: 23px;
            margin-bottom: 10px;
        }

        .welcome-card p {
            font-size: 14px;
            line-height: 1.6;
            opacity: 0.92;
        }

        .fee-upload-card {
            background: white;
            border: 1px solid #e6e3ef;
            border-radius: 14px;
            padding: 26px 30px;
            margin-top: 24px;
            box-shadow: 0 5px 18px rgba(37, 35, 61, 0.05);
        }

        .fee-upload-card h2 { font-size: 19px; margin-bottom: 8px; }
        .fee-upload-card p { color: #77758a; font-size: 14px; line-height: 1.5; margin-bottom: 16px; }
        .fee-upload-card input[type="file"] { display: block; margin-bottom: 14px; }
        .fee-upload-card button {
            border: 0; border-radius: 8px; padding: 11px 17px;
            background: #713ce6; color: white; font-weight: bold; cursor: pointer;
        }
        .fee-upload-card button:hover { background: #5e2dc7; }
        .upload-message, .upload-error { padding: 12px 15px; border-radius: 8px; margin: 15px 0; font-size: 14px; }
        .upload-message { background: #eaf8ef; color: #216e39; }
        .upload-error { background: #fff0f0; color: #a52b2b; }

        /* RESPONSIVE */
        @media (max-width: 700px) {

            .sidebar {
                width: 210px;
            }

            .main {
                margin-left: 210px;
                padding: 25px 20px;
            }

            .top-section {
                align-items: flex-start;
                gap: 15px;
            }

            .admin-badge {
                display: none;
            }
        }
    </style>
</head>

<body>

    <!-- SIDEBAR -->
    <div class="sidebar">

        <div class="logo">
            SectionSync
        </div>

        <div class="panel-name">
            Administrator Panel
        </div>


        <!-- DASHBOARD -->
        <a href="/admin/dashboard" class="active">
            Dashboard
        </a>


        <!-- ADMIN PROFILE -->
        <a href="/admin/profile">
            Admin Profile
        </a>

<!-- STUDENT MANAGEMENT -->
<div class="menu-title">
    Student Management
</div>

<div class="submenu">
    <a href="{{ url_for('student_management') }}">
        Student Management
    </a>

</div>


        <!-- SECTION MANAGEMENT -->
        <div class="menu-title">
            Section Management
        </div>

        <div class="submenu">

            <a href="/admin/section-capacity">
                Section Capacity
            </a>

            <a href="/admin/cgpa-constraints">
                CGPA Constraints
            </a>

        </div>


        <!-- OTHER ADMIN MODULES -->
        <a href="/admin/preferences">
            Student Preferences
        </a>

        <a href="/admin/allocation">
            Final Allocation
        </a>

        <a href="/admin/subjects-faculty">
            Subjects & Faculty
        </a>

        <a href="/admin/statistics">
            Allocation Statistics
        </a>


        <!-- LOGOUT -->
        <a href="/admin/login" class="logout">
            Logout
        </a>

    </div>


    <!-- MAIN CONTENT -->
    <div class="main">

        <!-- HEADER -->
        <div class="top-section">

            <div class="page-title">

                <h1>
                    Admin Dashboard
                </h1>

                <p>
                    Manage students, sections, preferences and allocation
                    through SectionSync.
                </p>

            </div>


            <div class="admin-badge">
                Administrator
            </div>

        </div>


        {% if message %}<div class="upload-message">{{ message }}</div>{% endif %}
        {% if error %}<div class="upload-error">{{ error }}</div>{% endif %}

        <!-- WELCOME CARD -->
        <div class="welcome-card">

            <h2>
                Welcome to SectionSync Admin Panel
            </h2>

            <p>
                Manage student information, sections, preferences and
                allocation from the administrator panel.
            </p>

        </div>

        <section class="fee-upload-card">
            <h2>Upload Fee Order IDs</h2>
            <p>Upload an .xlsx workbook with an <strong>order_id</strong> column in the first row and one approved order ID per row. Students can use these IDs on the Fee Verification page.</p>
            <form method="POST" action="/admin/dashboard" enctype="multipart/form-data">
                <input type="file" name="excel_file" accept=".xlsx" required>
                <button type="submit">Upload Order IDs</button>
            </form>
        </section>

    </div>

</body>
</html>
"""
