# QUEZON CITY UNIVERSITY
### College of Computer Studies - Department of Information Technology
**San Bartolome Campus, Novaliches, Quezon City**

---

# PROJECT PROPOSAL
### IPT102 - Integrative Programming and Technologies 2

| Parameter | Details |
| :--- | :--- |
| **PROJECT TITLE:** | **`[ INSERT YOUR PROJECT TITLE HERE ]`** |
| **COURSE & SECTION:** | **IPT102 (Integrative Programming and Technologies 2) - SBIT-3G** |
| **COURSE INSTRUCTOR:** | **Prof. Marilou Mangrobang** |
| **TARGET DELIVERABLE:** | Python Telemetry Ingestion & Web Analytics Dashboard with Tile Prototype |

---

### PROJECT PROPONENTS (GROUP MEMBERS)

| PROPONENTS (1 TO 5) | PROPONENTS (6 TO 10) |
| :--- | :--- |
| **1. Luigi Emanuel Britania** *(Lead Proponent)* | 6. `[ Insert Member Name 6 ]` |
| 2. `[ Insert Member Name 2 ]` | 7. `[ Insert Member Name 7 ]` |
| 3. `[ Insert Member Name 3 ]` | 8. `[ Insert Member Name 8 ]` |
| 4. `[ Insert Member Name 4 ]` | 9. `[ Insert Member Name 9 ]` |
| 5. `[ Insert Member Name 5 ]` | 10. `[ Insert Member Name 10 ]` |

---

## 1. Project Description

**Overview:**  
This project is a software-focused data logging and analytics system developed in Python for a kinetic energy footstep floor platform. In this setup, our group will produce a working prototype footstep tile equipped with piezoelectric sensors that generate small electrical pulses when stepped on. However, the primary focus and academic contribution of our project lies in the software: creating a reliable Python program that continuously captures the electrical data, stores it in a database, and displays it on an interactive web dashboard.

**Software Architecture:**  
The software connects directly to the prototype tile's microcontroller over a USB serial connection. Every time someone steps on the tile, the Python listener records the instantaneous power generated, updates the total energy stored inside an intermediate battery bank, monitors connected electronics (such as active smartphone chargers or 12V campus LED pathway lights), and counts the number of footsteps.

**Practical Visualizations:**  
To evaluate whether the kinetic generator is truly effective, the dashboard automatically groups the power data into distinct time horizons: **by 1 hour**, **by 10 hours** (representing a full campus school shift), **by 1 day** (24 hours), and **by 2 days** (48 hours). Furthermore, the dashboard includes a practical **"Device Equivalence Calculator"** that translates technical values like Joules or Watt-hours into real-world terms that anyone can understand—such as *"Equivalent to 15% of a phone battery charged"* or *"Enough power to illuminate a pathway lamp for 30 minutes."*

> [!NOTE]
> **Hardware vs. Software Delimitation for Evaluators:**  
> While our group is assembling the physical prototype floor tile to generate test signals, our project is explicitly software-focused for IPT102. Our deliverables are the Python data ingestion script, database storage, time-series analytical engine, and interactive web dashboard that make the kinetic generator measurable and practical.

---

## 2. Project Context

Drawing direct inspiration from pioneering kinetic pavement trials in Japan—such as the East Japan Railway (JR East) Tokyo Station footstep experiments where commuter turnstiles harvested pedestrian energy to power station pathway displays—this project explores the practical adaptation of kinetic energy harvesting within the local Philippine university environment. At Quezon City University (QCU San Bartolome Campus), thousands of pedestrians, including students, faculty, campus staff, and everyday commuters queuing at the main entrance walkway and the adjacent public bus and jeepney stops, exert heavy, continuous mechanical pressure onto the pavement daily. As an initial proof-of-concept to demonstrate that kinetic harvesting is attainable locally, our team is producing a functional prototype footstep tile—tested by illuminating a basic lightbulb load to visually confirm instantaneous energy capture—with a future vision of fabricating scalable sidewalk tiles built from upcycled plastic wastes and recycled electronic parts. However, because physical hardware alone cannot evaluate long-term feasibility or energy retention, the primary focus of this project for IPT102 under Prof. Marilou Mangrobang is centered on the software side: engineering an interactive Python telemetry and analytics dashboard that continuously logs power generation, monitors battery reserves and connected electronics, and provides transparent, actionable insights into campus clean-energy generation.

---

## 3. Statement of the Problem

Kinetic energy footstep platforms are often demonstrated as standalone hardware units without software logging, leaving campus stakeholders with no reliable way to measure energy generation, storage retention, and practical usability over time. To establish a verifiable and transparent system, this study addresses the following specific research and technical problems:

1. **Problem 1:** How can a functional prototype footstep tile be constructed and wired to an embedded microcontroller to supply real electrical telemetry during foot strikes?
2. **Problem 2:** How can a Python serial communication script be developed to continuously read live voltage, current, and footstep trigger data from the prototype tile without data loss or lag?
3. **Problem 3:** How can the collected power data be structured and visualized into 1-hour, 10-hour (school shift), 1-day (24 hours), and 2-day (48 hours) time intervals to evaluate generation efficiency during different campus hours?
4. **Problem 4:** How can the system track and display real-time energy status, specifically instantaneous power created at every moment and cumulative battery storage capacity (Watt-hours and percentage)?
5. **Problem 5:** How can the system monitor active electronic loads connected to the battery output, including the number of mobile phones plugged into 5V USB charging ports and the status of a 12V campus LED pathway light?
6. **Problem 6:** How can the software log footstep counts, compute average walking cadence per minute, and calculate everyday consumer device equivalents to show non-technical users what the stored power can realistically run?

---

## 4. General and Specific Objectives

### 4.1 General Objective
The general objective of this project is to develop a Python-based telemetry and web analytics dashboard integrated with a functional prototype footstep tile generator, providing an accessible, end-to-end software platform that captures real-time electrical output, records longitudinal power generation trends across multiple time horizons (1 hour, 10 hours, 1 day, and 2 days), monitors battery storage levels and active electronic loads, and presents practical device equivalencies to evaluate the efficiency and real-world feasibility of kinetic footstep energy harvesting at Quezon City University.

### 4.2 Specific Objectives
To achieve the general objective and systematically resolve each statement of the problem, the project shall pursue the following specific step-by-step objectives:

1. **Objective 1:** **To construct** a functional prototype footstep floor tile equipped with piezoelectric transducers and an embedded microcontroller to generate and output physical electrical signals during pedestrian foot strikes.
2. **Objective 2:** **To develop** a Python serial communication program that continuously ingests live voltage, current, and footstep trigger events from the prototype tile's microcontroller over a USB serial connection without packet loss.
3. **Objective 3:** **To design** an interactive time-series charting module that graphs power generated across 1-hour, 10-hour (campus shift), 1-day (24 hours), and 2-day (48 hours) intervals to evaluate generation efficiency across varying class schedules.
4. **Objective 4:** **To program** a real-time battery monitoring interface that displays instantaneous power created at every moment, cumulative stored energy (in Joules and Watt-hours), and the battery charge percentage (SoC %).
5. **Objective 5:** **To implement** a connected load monitoring module that tracks electronic devices drawing power from the battery bank, identifying the number of active 5V USB phone chargers and the operational status of a 12V campus LED pathway light.
6. **Objective 6:** **To build** an automated calculation engine that logs total footsteps, computes the average walking cadence per minute, and converts accumulated energy into relatable everyday benchmarks (such as smartphone recharge percentage and LED lighting runtime).

---

## 5. Scope and Delimitation

### 5.1 Project Scope (What the System Does)
The project encompasses the following concrete technical scope:

- **Prototype Tile Hardware Rig:** Construction of a single modular prototype footstep tile utilizing piezoelectric discs and an embedded microcontroller (Arduino/ESP32) to serve as the physical signal generator for the software system.
- **Python Telemetry Listener:** A lightweight Python script that opens a serial connection over USB, reads incoming telemetry packets (voltage, current, power, step trigger), and updates the database in real time without lag.
- **Multi-Interval Power Generation Charts:** Visual analytics graphs displaying power generated across four specific timeframes:
  - *1-Hour Window:* Captures immediate power surges during class changeover rushes.
  - *10-Hour Window:* Evaluates daytime generation across a full QCU school shift (7:00 AM to 5:00 PM).
  - *1-Day Window (24 Hours):* Measures total daily power and balances daytime generation against night standby.
  - *2-Day Window (48 Hours):* Compares power consistency across different days (e.g., busy face-to-face days vs. lighter schedules).
- **Real-Time Generation & Storage Status:** Live display of instantaneous power created at every moment (milliWatts/Watts), total stored energy in the battery bank (Joules and Watt-hours), and dynamic battery percentage (%).
- **Connected Load Monitoring:** Programmatic tracking of active output loads: counting how many smartphones are plugged into the 5V USB charging ports and monitoring the on/off relay state of a 12V DC LED campus pathway light.
- **Footstep Cadence & Everyday Equivalents:** Logging total footstep strikes, calculating average steps per minute (cadence), and running automated conversion formulas that show practical device equivalents (e.g., percentage of a 4,000mAh phone battery recharged, minutes of emergency talk-time, and LED lamp runtime).

### 5.2 Project Delimitations (What the System Does NOT Do)
To maintain a feasible scope for 3rd-year BSIT students, the project is delimited by the following boundaries:

- **No Commercial Transducer Manufacturing:** The team is assembling a working prototype using standard, readily available piezoceramic discs. We are not synthesizing new piezoelectric materials or engaging in industrial transducer manufacturing.
- **No Permanent Campus Pavement Excavation:** The prototype tile is a self-contained, portable floor unit tested in campus hallways or laboratory walkways. It does not involve permanent underground electrical wiring or civil sidewalk demolition.
- **No Claim of Instant Full Phone Charging from a Single Step:** A single footstep produces only millijoules of energy, which cannot instantaneously charge a phone to 100%. The system functions by accumulating energy across hundreds of footsteps into a battery buffer, which our software tracks until sufficient power is available.

---

### SUBMISSION & ENDORSEMENT

| SUBMITTED BY (ON BEHALF OF 10 PROPONENTS): | RECEIVED AND REVIEWED BY: |
| :--- | :--- |
| <br><br>**LUIGI EMANUEL BRITANIA**<br>Lead Proponent, SBIT-3G<br>Quezon City University - San Bartolome Campus | <br><br>**PROF. MARILOU MANGROBANG**<br>Course Instructor, IPT102<br>College of Computer Studies, Quezon City University |
