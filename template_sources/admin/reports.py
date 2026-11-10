"""Python source for the admin/reports.html page template."""

TEMPLATE_SOURCE = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Allocation Statistics - SectionSync</title>
    <style>
        * { box-sizing: border-box; font-family: Arial, sans-serif; }
        body { margin: 0; background: #f4f6fa; color: #18345d; }
        .header { height: 76px; background: #fff; border-bottom: 1px solid #dfe3ea; display: flex; align-items: center; justify-content: space-between; padding: 0 35px; }
        .header h1 { margin: 0; font-size: 25px; color: #15365f; }
        .header-right { font-size: 14px; color: #15365f; }
        .header-right span { margin: 0 10px; color: #777; }
        .main { max-width: 1400px; margin: auto; padding: 30px; }
        .page-heading { display: flex; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 24px; }
        .page-heading h2 { margin: 0 0 6px; font-size: 24px; }
        .page-heading p { margin: 0; color: #64748b; font-size: 15px; }
        .back-btn { display: inline-block; background: #2874d8; color: #fff; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-size: 14px; font-weight: 600; white-space: nowrap; }
        .back-btn:hover { background: #1f63bd; }
        .summary-grid { display: grid; grid-template-columns: repeat(4, minmax(150px, 1fr)); gap: 16px; margin-bottom: 20px; }
        .summary-card, .panel { background: #fff; border: 1px solid #dfe3ea; border-radius: 10px; }
        .summary-card { padding: 20px; }
        .summary-card span { color: #64748b; font-size: 13px; }
        .summary-card strong { display: block; margin-top: 9px; font-size: 27px; color: #17375e; }
        .summary-card small { display: block; margin-top: 6px; color: #7b8798; }
        .charts-grid { display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(280px, .8fr); gap: 18px; margin-bottom: 20px; }
        .panel { padding: 22px; }
        .panel h3 { margin: 0 0 6px; font-size: 17px; color: #17375e; }
        .panel-subtitle { margin: 0 0 22px; color: #7b8798; font-size: 13px; }
        .program-row { display: grid; grid-template-columns: 76px minmax(100px, 1fr) 92px; align-items: center; gap: 12px; margin: 17px 0; }
        .program-name { font-size: 13px; font-weight: 700; }
        .stacked-bar, .band-track { height: 15px; overflow: hidden; display: flex; background: #edf1f7; border-radius: 10px; }
        .allocated-fill { height: 100%; background: #2874d8; }
        .pending-fill { height: 100%; background: #dce5f2; }
        .program-total { text-align: right; color: #64748b; font-size: 12px; white-space: nowrap; }
        .legend { display: flex; gap: 18px; margin-top: 22px; color: #64748b; font-size: 12px; }
        .legend span { display: inline-flex; align-items: center; gap: 7px; }
        .legend i { width: 10px; height: 10px; border-radius: 3px; display: inline-block; }
        .legend-allocated { background: #2874d8; }
        .legend-pending { background: #dce5f2; }
        .donut-wrap { min-height: 230px; display: flex; align-items: center; justify-content: center; gap: 24px; }
        .donut { --rate: 0%; width: 165px; height: 165px; flex: 0 0 auto; display: grid; place-items: center; border-radius: 50%; background: conic-gradient(#2874d8 var(--rate), #e8edf5 0); }
        .donut::before { content: ""; width: 122px; height: 122px; grid-area: 1 / 1; border-radius: 50%; background: #fff; }
        .donut-center { z-index: 1; grid-area: 1 / 1; text-align: center; }
        .donut-center strong { display: block; font-size: 27px; }
        .donut-center span { color: #7b8798; font-size: 12px; }
        .donut-legend { display: grid; gap: 13px; color: #64748b; font-size: 13px; }
        .donut-legend strong { display: block; color: #17375e; font-size: 17px; margin-top: 3px; }
        .band-row { display: grid; grid-template-columns: 72px 1fr 44px; align-items: center; gap: 12px; margin: 18px 0; }
        .band-name { font-size: 13px; font-weight: 600; }
        .band-fill { height: 100%; border-radius: 10px; background: #6b8fce; }
        .band-row.low .band-fill { background: #5c88d5; }
        .band-row.medium .band-fill { background: #38a3a5; }
        .band-row.high .band-fill { background: #edaa4c; }
        .band-count { text-align: right; font-weight: 700; }
        .table-panel { padding: 0; overflow: hidden; }
        .table-heading { padding: 22px 22px 0; }
        .table-scroll { overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; min-width: 650px; }
        th { padding: 13px 18px; background: #f5f7fa; color: #52647d; text-align: left; font-size: 12px; border-bottom: 1px solid #dfe3ea; }
        td { padding: 14px 18px; border-bottom: 1px solid #e8ebef; font-size: 13px; }
        .occupancy { min-width: 175px; }
        .occupancy-track { height: 8px; background: #edf1f7; border-radius: 8px; overflow: hidden; margin-bottom: 5px; }
        .occupancy-fill { height: 100%; background: #2874d8; border-radius: 8px; }
        .occupancy small { color: #7b8798; }
        .empty { padding: 28px; text-align: center; color: #7b8798; font-size: 14px; }
        @media (max-width: 800px) {
            .charts-grid { grid-template-columns: 1fr; }
            .summary-grid { grid-template-columns: repeat(2, minmax(130px, 1fr)); }
        }
        @media (max-width: 560px) {
            .header { padding: 0 18px; }
            .header h1 { font-size: 20px; }
            .main { padding: 20px; }
            .page-heading { align-items: flex-start; flex-direction: column; }
            .summary-grid { grid-template-columns: 1fr 1fr; gap: 10px; }
            .summary-card { padding: 15px; }
            .summary-card strong { font-size: 23px; }
            .donut-wrap { flex-direction: column; gap: 16px; padding-bottom: 12px; }
            .donut-legend { grid-template-columns: 1fr 1fr; }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>Allocation Statistics</h1>
        <div class="header-right">Admin <span>|</span> SectionSync</div>
    </header>
    <main class="main">
        <div class="page-heading">
            <div>
                <h2>Allocation Insights</h2>
                <p>Visual summary of student assignments, program progress, CGPA groups, and section occupancy.</p>
            </div>
            <a class="back-btn" href="{{ url_for('admin_dashboard') }}">Back to Dashboard</a>
        </div>

        <section class="summary-grid" aria-label="Allocation totals">
            <article class="summary-card"><span>Total students</span><strong>{{ total_students }}</strong><small>Across all programs</small></article>
            <article class="summary-card"><span>Allocated</span><strong>{{ allocated_students }}</strong><small>Students assigned a section</small></article>
            <article class="summary-card"><span>Awaiting allocation</span><strong>{{ unallocated_students }}</strong><small>Students without an assignment</small></article>
            <article class="summary-card"><span>Allocation rate</span><strong>{{ allocation_rate }}%</strong><small>Of all registered students</small></article>
        </section>

        <section class="charts-grid">
            <article class="panel">
                <h3>Allocation by Program</h3>
                <p class="panel-subtitle">Allocated and unallocated students in each program.</p>
                {% if program_stats %}
                    {% for program in program_stats %}
                    <div class="program-row">
                        <div class="program-name">{{ program['program'] }}</div>
                        <div class="stacked-bar" role="img" aria-label="{{ program['program'] }}: {{ program['allocated'] }} allocated, {{ program['unallocated'] }} unallocated">
                            <div class="allocated-fill" style="width:{{ program['allocated_percent'] }}%"></div>
                            <div class="pending-fill" style="width:{{ 100 - program['allocated_percent'] }}%"></div>
                        </div>
                        <div class="program-total">{{ program['allocated'] }} / {{ program['total'] }}</div>
                    </div>
                    {% endfor %}
                    <div class="legend"><span><i class="legend-allocated"></i>Allocated</span><span><i class="legend-pending"></i>Unallocated</span></div>
                {% else %}
                    <div class="empty">Add students to see program allocation insights.</div>
                {% endif %}
            </article>

            <article class="panel">
                <h3>Overall Progress</h3>
                <p class="panel-subtitle">Share of registered students with a section assignment.</p>
                <div class="donut-wrap">
                    <div class="donut" style="--rate:{{ allocation_rate }}%" role="img" aria-label="{{ allocation_rate }} percent allocated">
                        <div class="donut-center"><strong>{{ allocation_rate }}%</strong><span>allocated</span></div>
                    </div>
                    <div class="donut-legend">
                        <div>Allocated<strong>{{ allocated_students }}</strong></div>
                        <div>Unallocated<strong>{{ unallocated_students }}</strong></div>
                    </div>
                </div>
            </article>
        </section>

        <section class="charts-grid">
            <article class="panel">
                <h3>Allocated by CGPA Band</h3>
                <p class="panel-subtitle">Number of students assigned from each configured band.</p>
                {% for band in band_stats %}
                <div class="band-row {{ band['band']|lower }}">
                    <div class="band-name">{{ band['band'] }}</div>
                    <div class="band-track" role="img" aria-label="{{ band['count'] }} {{ band['band'] }} CGPA students allocated">
                        <div class="band-fill" style="width:{{ band['percent'] }}%"></div>
                    </div>
                    <div class="band-count">{{ band['count'] }}</div>
                </div>
                {% endfor %}
            </article>

            <article class="panel">
                <h3>Section Occupancy</h3>
                <p class="panel-subtitle">Filled seats compared with each section's capacity.</p>
                {% if section_stats %}
                    {% for section in section_stats %}
                    <div class="program-row">
                        <div class="program-name">{{ section['program'] }} · {{ section['section_name'] }}</div>
                        <div class="stacked-bar" role="img" aria-label="{{ section['allocated'] }} of {{ section['capacity'] }} seats filled">
                            <div class="allocated-fill" style="width:{{ section['occupancy_percent'] }}%"></div>
                        </div>
                        <div class="program-total">{{ section['allocated'] }} / {{ section['capacity'] }}</div>
                    </div>
                    {% endfor %}
                {% else %}
                    <div class="empty">Add sections to see seat occupancy.</div>
                {% endif %}
            </article>
        </section>

        <section class="panel table-panel">
            <div class="table-heading">
                <h3>Section Capacity Overview</h3>
                <p class="panel-subtitle">Current assigned and available seats by section.</p>
            </div>
            {% if section_stats %}
            <div class="table-scroll">
                <table>
                    <thead><tr><th>Program</th><th>Section</th><th>Capacity</th><th>Allocated</th><th>Occupancy</th></tr></thead>
                    <tbody>
                        {% for section in section_stats %}
                        <tr>
                            <td>{{ section['program'] }}</td>
                            <td>{{ section['section_name'] }}</td>
                            <td>{{ section['capacity'] }}</td>
                            <td>{{ section['allocated'] }}</td>
                            <td class="occupancy">
                                <div class="occupancy-track"><div class="occupancy-fill" style="width:{{ section['occupancy_percent'] }}%"></div></div>
                                <small>{{ section['occupancy_percent'] }}% occupied</small>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            {% else %}<div class="empty">No section capacities have been configured.</div>{% endif %}
        </section>
    </main>
</body>
</html>
"""
