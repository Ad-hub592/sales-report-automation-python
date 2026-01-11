## SALES-ANALYSIS-AUTOMATED ALERT-SYSTEM 
  # Overview
* This project is a afully automated buisness analysis system built in Python that:
  - Reads Daily Sales Summary (.txt)
  - Compares Today V/s Last 6-7 days
  - Generate Buisness Insights
  - Triggers intelliget alerts based on configurable rules
  - Sends a clear, Owner Friendly Email report with attachment
* This is not a Toy Script - it follows real-world modular architecture and buisness logic
# Key Features
 - Multi-day report ingestion (7-Day rolling analysis)
 - Sales Comparison (Total/Cash/Credit)
 - Pending Order tracking (Today,Average,Total)
 - Rule-based alerts(Sales drop, credit risk, pending risk)
 - Automated Email Delivery
 - Modular, production-ready Structure
# Project Structure
  - |- analysis_core.py --->  \ Core data extraction & analysis logic \
  - |-alerts.py ------------>  \ Buisness alert rules & messaging \
  - |-sendmail.py -------->  \ Email Sending Logic \
  - |-config.py ----------->  \ Configuration & thresholds \
  - |-main.py --------------> \ Entry Point ( Orchestrator ) \
  - |-Reports/
    - |- Sales_Summary_YYY-MM-DD.txt
    - |- Analysis.txt

# Buisness Logic Summary
 - Sales Drop ALert
  - Triggered when today's sales fall below a defined percentage of the 6-day average
 - Credit Risk Alert
   - Triggered when credit sales dominated total sales
 - Pending Risk Alerts
   - High Pending today --> Critical risk
   - High 7-day average pending --> Operational Warning
 - Each alert includes
   - What happened
   - Buisness impact
   - Suggested action
# How to Run
 - Ensure that every Python File should be in same Folder
 - Run the main.py
   - It Generate Analysis.txt
   - It Append the Alerts ( if any )
   - Sends the Repot via Email
# Why This Project Matters
 - This System demonstrates :
   - Practical automation
   - Real buisness reasoning
   - Clean Seperation of concerns
   - Owner-focused reporting ( not developer logs )
 - It can be easily extended to :
   - Databases
   - Dashboards
   - Scheduled Jobs ( cron / task schedular )
   - Multi-store analysis
# Author 
 - Aditya .RV Gupta
   - Automation & Buisness Analysis Project
       - (System-generated reports — do not reply)
