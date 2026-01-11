import config as cfg

def generate_alerts(today_total, avg_total, cash, credit, pending, avg_pending, tot_pending):
    alerts = []

    # --- Pending Overview (Context First) ---
    alerts.append(
        f"Pending Overview: {pending} pending today | \n "
        f"7-day average: {avg_pending} | \n"
        f"Total pending (7 days): {tot_pending} | \n")

    # --- Sales Drop Alert ---
    if today_total < (avg_total * cfg.ALERT_DROP_THRESHOLD):
        drop_pct = round((1 - (today_total / avg_total)) * 100, 1)
        alerts.append(
            f"WARNING: Sales dropped by {drop_pct}% compared to 6-day average.\n"
            f"Impact: Lower daily revenue.\n"
            f"Action: Review low-performing customers or orders today.")

    # --- Credit Dependency Alert ---
    if (cash + credit) > 0:
        credit_ratio = credit / (cash + credit)
        if credit_ratio > cfg.CREDIT_RATIO_LIMIT:
            alerts.append(
                f"RISK: High dependency on credit sales ({round(credit_ratio*100,1)}%).\n"
                f"Impact: Cash flow delay.\n"
                f"Action: Follow up with top credit customers for collections.")

    # --- Average Pending Alert ---
    if avg_pending > cfg.AVG_PENDING_LIMIT:
        alerts.append(
            f"WARNING: Average pending orders over last 7 days is high ({round(avg_pending,1)}).\n"
            f"Impact: Increased operational backlog.\n"
            f"Action: Identify and clear orders older than 3 days.")

    # --- Critical Pending Alert ---
    if tot_pending > cfg.PENDING_LIMIT:
        alerts.append(
            f"CRITICAL: Total Pending orders today crossed limit ({tot_pending}).\n"
            f"Impact: High risk of cash blockage.\n"
            f"Action: Immediate collection follow-up required.")

    return alerts
