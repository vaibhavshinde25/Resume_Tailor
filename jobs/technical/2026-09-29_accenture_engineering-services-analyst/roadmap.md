# 🎯 7-Day Technical Interview Roadmap: Accenture

- **Target Company:** Accenture
- **Target Role:** Engineering Services Analyst (Early Career)
- **Job ID:** R00327660
- **Location:** Ebene
- **Date Generated:** 2026-09-29

---

## 🏢 Company Context: Accenture Engineering & Industry X
Accenture's Engineering Services teams work closely with global clients to drive digital transformation in operational, manufacturing, and technology infrastructure. As an **Engineering Services Analyst**, your role focuses on **Data Synthesis** (extracting raw system data and discovering trends) and **Visualization** (delivering automated dashboards to management and engineering leads).

---

## 📅 Day-by-Day Preparation Plan

```
Day 1: Accenture Case Context & Data Synthesis Fundamentals
Day 2: Advanced SQL for Engineering & Multi-System Data Integration
Day 3: Power BI, DAX & Automated Data Ingestion (ETL)
Day 4: Manufacturing & Quality Analytics Crash Course (Bridging the Gap)
Day 5: Python (Pandas/NumPy) for Trend Discovery & Data Cleaning
Day 6: Accenture Mock Scenarios & System Design Interview Drills
Day 7: STAR Behavioral Stories & Leadership Principles
```

---

### 📘 Day 1: Accenture Context & Data Synthesis Fundamentals
- **Focus:** How to structure unstructured data problems from client engineering systems.
- **Key Concepts:**
  - Defining the data flow: Source System (ERP, MES, ITOM) $\rightarrow$ Staging / Data Warehouse $\rightarrow$ Power Query Transformations $\rightarrow$ Visual Dashboard.
  - Designing KPIs from ambiguous stakeholder requirements.
- **Exercise:**
  - Take your Micropoint/L&T Realty experience: Write down a 2-minute elevator pitch explaining how you translated raw operational and ticket logs into clear management KPIs.

### 📘 Day 2: Advanced SQL for Multi-System Integration
- **Focus:** Querying data across disparate tables and timestamps.
- **Key Concepts:**
  - Multi-table `JOIN` strategies (`INNER`, `LEFT`, `FULL OUTER`, `CROSS`).
  - Window Functions: `ROW_NUMBER()`, `DENSE_RANK()`, `LEAD()`, `LAG()` for timestamp comparison and duration tracking.
  - Common Table Expressions (CTEs) for multi-stage aggregation.
- **Sample Query Drill:**
  - Write a SQL query to calculate the rolling 7-day average of system incidents or quality defects grouped by product line.

### 📘 Day 3: Power BI, DAX & Automated Data Ingestion
- **Focus:** Building performant, automated dashboards.
- **Key Concepts:**
  - Star Schema dimensional modeling: Fact tables (incidents/defects) vs. Dimension tables (date, machine, department).
  - DAX Measures:
    - Time Intelligence: `TOTALYTD()`, `SAMEPERIODLASTYEAR()`, `DATEADD()`.
    - Dynamic Context: `CALCULATE(..., FILTER(...))`, `ALL()`, `USERELATIONSHIP()`.
  - Power Query M transformations: Merging queries, unpivoting columns, conditional columns, and scheduled data refreshes.
- **Interview Soundbite:**
  - Explain how you automated reporting at Micropoint to eliminate 30% of manual reporting overhead.

### 📘 Day 4: Manufacturing & Quality Analytics (Bridging the Gap)
- **Focus:** Master the industry vocabulary for Manufacturing & Quality domains.
- **Key Metrics to Memorize:**
  1. **OEE (Overall Equipment Effectiveness):** $\text{Availability} \times \text{Performance} \times \text{Quality}$.
  2. **First Pass Yield (FPY):** $\frac{\text{Acceptable Units without rework}}{\text{Total Units Started}}$.
  3. **Defect Rate & PPM (Parts Per Million):** Tracking manufacturing quality over time.
  4. **MTBF & MTTR:** Mean Time Between Failures & Mean Time To Repair (directly analogous to your IT asset/incident SLA tracking).
- **Practical Translation:**
  - If asked about manufacturing experience, explain: *"While my direct production work has been in IT systems and infrastructure asset management, the underlying telemetry is identical: tracking asset downtime, calculating MTTR, defect trend analysis, and root-cause discovery."*

### 📘 Day 5: Python (Pandas/NumPy) for Trend Discovery & Data Cleaning
- **Focus:** Rapid data synthesis using Python.
- **Key Techniques:**
  - Cleaning messy text logs: `.str.extract()`, `.fillna()`, `.dropna()`.
  - Data reshaping: `pd.pivot_table()`, `.groupby()`, `.resample('W')`.
  - Outlier detection with IQR and standard deviations.

### 📘 Day 6: Scenario-Based Case Studies & Mock Dashboarding
- **Scenario 1:** An engineering client reports that their defect reporting is delayed by 3 days because multiple plant managers send Excel spreadsheets. How do you design an automated pipeline?
  - *Answer Framework:* Standardized template / automated ingestion via Python/Power Query $\rightarrow$ Centralized database or SharePoint repository $\rightarrow$ Automated scheduled refresh in Power BI with alert thresholds.
- **Scenario 2:** You notice a sudden spike in quality defects or ticket volume. What steps do you take to identify the root cause?
  - *Answer Framework:* Slice by dimensions (time of day, supplier batch, operator team) $\rightarrow$ perform Pareto 80/20 analysis $\rightarrow$ validate underlying data integrity $\rightarrow$ report findings to lead engineer.

### 📘 Day 7: Behavioral STAR Stories & Architecture Walkthroughs
- **Story 1 (Problem-Solving & Automation):** Tell me about a time you improved a slow or manual reporting process (The 30% time-saving Power Query / Python automation project).
- **Story 2 (Stakeholder Management):** How you handled conflicting reporting requirements between cross-functional teams at L&T Realty.
- **Story 3 (Data Accuracy Under Pressure):** How you ensured 95%+ SLA compliance across user records and asset tracking.

---

## ❓ Accenture Interview Question Bank

### Technical Questions:
1. *What is the difference between `CALCULATE()` and normal row filtering in DAX?*
2. *How do you optimize a slow Power BI report connected to large operational datasets?*
   - *(Answer: Push transformations upstream to SQL/ETL, remove unused columns, avoid bidirectional relationships, use integer surrogate keys).*
3. *How do you handle missing or corrupted sensor/system records during ETL?*
4. *How would you compare Power BI with alternative tools like QlikSense or Looker Studio?*
   - *(Answer: Emphasize Power BI's seamless Microsoft 365 ecosystem, DAX tabular model, and Power Query M engine, while acknowledging Qlik's associative engine).*

### Scenario & Behavioral Questions:
5. *Why Accenture, and why the Engineering Services Analyst role?*
6. *Describe a situation where the raw data seemed inaccurate or conflicting. How did you verify the source of truth?*
7. *How do you present technical data insights to a non-technical manager or client?*

---

## 🔗 Curated Learning Resources
- 📘 [Microsoft Power BI Architecture & DAX Guide](https://learn.microsoft.com/en-us/power-bi/)
- 📘 [SQL Window Functions Interactive Tutorial (Mode Analytics)](https://mode.com/sql-tutorial/sql-window-functions/)
- 📘 [Manufacturing Analytics & OEE Explained (Lean Production)](https://www.leanproduction.com/oee/)
- 📘 [Accenture Careers & Culture: What We Believe](https://www.accenture.com/us-en/about/company/culture)
