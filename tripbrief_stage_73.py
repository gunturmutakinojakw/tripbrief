# === Stage 73: Add a lightweight HTML report export ===
# Project: TripBrief
def export_html_report(brief):
    html = []
    html.append("<html><head><title>TripBrief</title>")
    html.append("<style>body{font-family:monospace;margin:20px}table{border-collapse:collapse;width:100%%}.trav{padding:4px 8px;border-bottom:1px solid #ccc}</style>")
    html.append("</head><body>")
    html.append(f"<h1>Trip to {brief.get('destination', 'Unknown')}</h1>")
    for section, items in brief.items():
        if isinstance(items, dict):
            html.append(f"<h2>{section}</h2><table><tr><th>Item</th><th>Detail</th></tr>")
            for k, v in items.items():
                html.append(f"<tr class='trav'><td>{k}</td><td>{v}</td></tr>")
            html.append("</table>")
    html.append("</body></html>")
    return "\n".join(html)
