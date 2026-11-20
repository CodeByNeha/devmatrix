async function loadDashboard() {
    const res = await fetch('/api/metrics');
    const data = await res.json();
    document.getElementById('metric-logs').innerText = data.total_logs;
    document.getElementById('metric-minutes').innerText = data.total_minutes;
    document.getElementById('metric-sessions').innerText = data.completed_sessions;
}
window.addEventListener('DOMContentLoaded', loadDashboard);
