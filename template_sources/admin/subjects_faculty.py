"""Python source for the admin/subjects_faculty.html page template."""

TEMPLATE_SOURCE = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subjects &amp; Faculty - SectionSync</title>
    <style>
        * { box-sizing: border-box; font-family: Arial, sans-serif; }
        body { margin: 0; background: #f4f6fa; color: #18345d; }
        .header { height: 76px; background: #fff; border-bottom: 1px solid #dfe3ea; display: flex; align-items: center; justify-content: space-between; padding: 0 35px; }
        .header h1 { margin: 0; font-size: 25px; color: #15365f; }
        .header-right { font-size: 14px; color: #15365f; }
        .header-right span { margin: 0 10px; color: #777; }
        .main { max-width: 1500px; margin: auto; padding: 30px; }
        .page-heading { display: flex; justify-content: space-between; align-items: center; gap: 18px; margin-bottom: 24px; }
        .page-heading h2 { margin: 0 0 6px; font-size: 24px; }
        .page-heading p { margin: 0; color: #64748b; font-size: 15px; }
        .back-btn, .primary-btn { display: inline-block; border: 0; border-radius: 8px; padding: 12px 20px; background: #2874d8; color: white; text-decoration: none; font-size: 14px; font-weight: 600; cursor: pointer; white-space: nowrap; }
        .primary-btn { background: #17375e; }
        .back-btn:hover { background: #1f63bd; }
        .primary-btn:hover { background: #102c4d; }
        .notice { padding: 14px 16px; border-radius: 8px; margin-bottom: 18px; background: #eaf2ff; color: #17375e; }
        .notice.error { background: #fff0f0; color: #a52b2b; }
        .card, .basket { background: #fff; border: 1px solid #dfe3ea; border-radius: 10px; margin-bottom: 22px; }
        .card { padding: 22px; }
        .card h3, .basket h3 { margin: 0 0 8px; color: #17375e; font-size: 17px; }
        .subtext { margin: 0 0 18px; color: #64748b; font-size: 13px; }
        .form-grid { display: grid; grid-template-columns: 1.2fr .6fr .9fr 1.4fr repeat(4, minmax(70px, .55fr)) auto; gap: 11px; align-items: end; }
        .field label { display: block; margin-bottom: 7px; color: #52647d; font-size: 12px; font-weight: 600; }
        .field input, .field select { width: 100%; min-width: 0; padding: 10px 11px; background: #fff; border: 1px solid #cfd6e0; border-radius: 7px; color: #17375e; font-size: 13px; }
        .basket { overflow: hidden; }
        .basket-heading { padding: 18px 20px; background: #fff500; color: #101010; text-align: center; border-bottom: 1px solid #d5d5d5; }
        .basket-heading h3 { margin: 0; color: #101010; font-size: 16px; }
        .basket-heading p { margin: 5px 0 0; font-size: 12px; }
        .table-scroll { overflow-x: auto; }
        table { width: 100%; min-width: 850px; border-collapse: collapse; }
        th, td { border: 1px solid #cdd3dc; padding: 8px 9px; text-align: left; font-size: 12px; }
        th { background: #f7f8fa; color: #17375e; font-weight: 700; white-space: nowrap; }
        th.subject-col { min-width: 235px; }
        th.ltp-col { min-width: 72px; }
        th.section-col { min-width: 145px; text-align: center; }
        td.subject { font-weight: 600; }
        td.ltp { white-space: nowrap; font-variant-numeric: tabular-nums; }
        .faculty-input { width: 100%; min-width: 120px; padding: 7px 8px; border: 1px solid #d2d8e2; border-radius: 5px; color: #17375e; font-size: 12px; }
        .basket-actions { display: flex; justify-content: flex-end; padding: 12px 16px; border-top: 1px solid #e8ebef; }
        .empty { padding: 28px; color: #7b8798; text-align: center; font-size: 14px; }
        @media (max-width: 1100px) { .form-grid { grid-template-columns: repeat(4, minmax(120px, 1fr)); } }
        @media (max-width: 700px) {
            .header { padding: 0 18px; }
            .header h1 { font-size: 20px; }
            .main { padding: 20px; }
            .page-heading { align-items: flex-start; flex-direction: column; }
            .form-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .form-grid .primary-btn { grid-column: 1 / -1; }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>Subjects &amp; Faculty</h1>
        <div class="header-right">Admin <span>|</span> SectionSync</div>
    </header>
    <main class="main">
        <div class="page-heading">
            <div>
                <h2>Program Subject Baskets</h2>
                <p>Organize subjects and assign faculty to each section in the program basket.</p>
            </div>
            <a class="back-btn" href="{{ url_for('admin_dashboard') }}">Back to Dashboard</a>
        </div>

        {% if message %}<div class="notice">{{ message }}</div>{% endif %}
        {% if error %}<div class="notice error">{{ error }}</div>{% endif %}

        <section class="card">
            <h3>Add a Subject</h3>
            <p class="subtext">Enter the course details first, then assign a faculty member in each section column below.</p>
            <form method="POST" action="{{ url_for('subjects_faculty') }}" class="form-grid">
                <input type="hidden" name="action" value="add_subject">
                <div class="field">
                    <label for="program">Program</label>
                    <select id="program" name="program" required>
                        <option value="">Select program</option>
                        {% for program in programs %}<option value="{{ program }}">{{ program }}</option>{% endfor %}
                    </select>
                </div>
                <div class="field"><label for="semester">Semester</label><input id="semester" name="semester" value="III" required></div>
                <div class="field"><label for="batch">Batch</label><input id="batch" name="batch" value="2024-2028" required></div>
                <div class="field"><label for="subject_name">Subject</label><input id="subject_name" name="subject_name" placeholder="Subject name" required></div>
                <div class="field"><label for="lecture">L</label><input id="lecture" name="lecture" type="number" min="0" value="0" required></div>
                <div class="field"><label for="tutorial">T</label><input id="tutorial" name="tutorial" type="number" min="0" value="0" required></div>
                <div class="field"><label for="practical">P</label><input id="practical" name="practical" type="number" min="0" value="0" required></div>
                <div class="field"><label for="credits">C</label><input id="credits" name="credits" type="number" min="0" value="0" required></div>
                <button class="primary-btn" type="submit">Add Subject</button>
            </form>
        </section>

        {% for basket in baskets %}
        <section class="basket">
            <div class="basket-heading">
                <h3>{{ basket['semester'] }} B.Tech ({{ basket['program'] }}) ({{ basket['batch'] }}) - {{ basket['student_count'] }}</h3>
                <p>Subjects are listed by row; each section column shows the faculty assigned to that subject.</p>
            </div>
            <form method="POST" action="{{ url_for('subjects_faculty') }}">
                <input type="hidden" name="action" value="save_faculty">
                <input type="hidden" name="program" value="{{ basket['program'] }}">
                <input type="hidden" name="semester" value="{{ basket['semester'] }}">
                <input type="hidden" name="batch" value="{{ basket['batch'] }}">
                <div class="table-scroll">
                    <table>
                        <thead>
                            <tr>
                                <th class="subject-col">Subject</th>
                                <th class="ltp-col">L T P C</th>
                                {% for section in basket['sections'] %}
                                <th class="section-col">Section {{ section['name'] }} - {{ section['capacity'] if section['capacity'] else '—' }}</th>
                                {% endfor %}
                            </tr>
                        </thead>
                        <tbody>
                            {% for subject in basket['subjects'] %}
                            <tr>
                                <td class="subject">{{ subject['subject_name'] }}</td>
                                <td class="ltp">{{ subject['lecture'] }} {{ subject['tutorial'] }} {{ subject['practical'] }} {{ subject['credits'] }}</td>
                                {% for section in basket['sections'] %}
                                <td><input class="faculty-input" type="text" name="faculty_{{ subject['id'] }}_{{ section['name'] }}" value="{{ subject['faculty'].get(section['name'], '') }}" placeholder="Faculty name" aria-label="{{ subject['subject_name'] }} faculty for Section {{ section['name'] }}"></td>
                                {% endfor %}
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
                <div class="basket-actions"><button class="primary-btn" type="submit">Save Faculty Assignments</button></div>
            </form>
        </section>
        {% else %}
        <section class="basket"><div class="empty">No subject baskets yet. Add a subject above to create a program basket.</div></section>
        {% endfor %}
    </main>
</body>
</html>
"""
