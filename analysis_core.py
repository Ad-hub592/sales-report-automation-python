from datetime import datetime
import os
import config as cfg

REPORTS_DIR = cfg.REPORTS_DIR

def extract_summary(file_path):
    total = cash = credit = pending = 0.0

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith("Total Sales") and "--" in line:
                total = float(line.split("--")[1])

            elif line.startswith("Total Cash Sales") and "--" in line:
                cash = float(line.split("--")[1])

            elif line.startswith("Total Credit Sales") and "--" in line:
                credit = float(line.split("--")[1])

            elif line.startswith("Pending Sales") and "--" in line:
                pending = int(line.split("--")[1].split()[0])

    return total, cash, credit, pending


def run_analysis():
    files = sorted(f for f in os.listdir(REPORTS_DIR) if f.endswith(".txt"))

    if len(files) < 2:
        raise Exception("Not enough reports for analysis")

    totals, cashs, credits, pendings = [], [], [], []

    for file in files:
        t, c, cr, p = extract_summary(os.path.join(REPORTS_DIR, file))
        totals.append(t)
        cashs.append(c)
        credits.append(cr)
        pendings.append(p)

    # ---- today & averages ----
    today = {
        "total": totals[-1],
        "cash": cashs[-1],
        "credit": credits[-1],
        "pending": pendings[-1]
    }

    average = {
        "total": sum(totals[:-1]) / len(totals[:-1]),
        "cash": sum(cashs[:-1]) / len(cashs[:-1]),
        "credit": sum(credits[:-1]) / len(credits[:-1]),
        "pending":sum(pendings[:-1])/ len(pendings[:-1]),
        "tot_pending":sum(pendings[:-1])
    }

    # ---- build report text ----
    report_lines = [
        f"Business Analysis Report : {datetime.now().date()}",
        "-" * 50,
        f"Total Sales Today : {today['total']}",
        f"6-Day Average Sales : {average['total']}",
        f"Cash Sales Today : {today['cash']}",
        f"6-Day Avg Cash Sales : {average['cash']}",
        f"Credit Sales Today : {today['credit']}",
        f"6-Day Avg Credit Sales : {average['credit']}",
        f"Pending Orders Today : {today['pending']}",
        "",
        "*Automation by System Admin",
        '-'*50
    ]

    report_text = "\n".join(report_lines)

    return {
        "report": report_text,
        "today": today,
        "average": average
    }
