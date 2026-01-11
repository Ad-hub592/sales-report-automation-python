from analysis_core import run_analysis
from alerts import generate_alerts
from sendmail import send_email
import config as cfg
def main():
    analysis_data=run_analysis()
    
    today=analysis_data["today"]
    average=analysis_data["average"]
    
    today_total=today['total']
    cash=today['cash']
    credit=today['credit']
    pending=today['pending']
    avg_total=average['total']
    avg_cash=average['cash']
    avg_credit=average['credit']
    avg_pending=round(average['pending'],1)
    tot_pending=average['tot_pending']
    alerts=generate_alerts(today_total, avg_total, cash, credit, pending, avg_pending, tot_pending)
    report=analysis_data["report"]
    
    with open(cfg.ANALYSIS_FILE,"w") as f:
        f.write(report)
        if alerts:
            f.write("\n" + "\n".join(alerts))
    
    send_email(cfg.ANALYSIS_FILE)
    
if __name__ == "__main__":
    main()