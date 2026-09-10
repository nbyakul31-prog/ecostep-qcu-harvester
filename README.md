# EcoStep QCU: Kinetic Energy-Harvesting Footstep Floor Platform
### Academic Hardware Prototype, 4x4 Grid Simulator & Public Utility System
**Course:** AR101 - Computer Architecture and Organization  
**Institution:** Quezon City University (QCU – Novaliches Campus)  
**Target Deployment:** High-Traffic Campus Entrance & Sidewalk Footpaths  
**Live Interactive Simulator:** [https://nbyakul31-prog.github.io/ecostep-qcu-harvester/](https://nbyakul31-prog.github.io/ecostep-qcu-harvester/)  

---

## 🌟 Executive Overview

In Quezon City University (Novaliches Campus), thousands of students, faculty members, and staff traverse the narrow main entrance walkways and cafeteria corridors daily. Every single day, tens of thousands of mechanical foot strikes exert hundreds of thousands of Newtons of kinetic force into the concrete ground—energy that is currently 100% wasted as dissipated heat and sound.

**"EcoStep QCU"** converts this ambient pedestrian kinetic energy into usable electrical power while upcycling campus plastic waste (shredded HDPE bottle caps) into durable structural composite pavement bricks.

The system is monitored in real-time by an embedded **ATmega328P microcontroller architecture**, bridging AR101 computer architecture principles (`INT0` hardware interrupts, `ADMUX`/`ADCSRA` 10-bit ADC data buses, and register arithmetic) into an interactive public utility system.

---

## ⚡ Core Features & Interactive Modules

### 1. 🚶‍♂️ Infinite Walking Student Animation Canvas
- Real-time HTML5 Canvas simulation of a QCU student walking across kinetic pavement tiles.
- Biomechanical heel-strike impacts generate dynamic shockwave ripples and upward kinetic energy sparks.
- Live sliders to adjust **Student Body Weight (45kg – 95kg)** and **Walking Cadence (40 – 160 spm)**.

### 2. 🕒 QCU Campus Rush Shift Traffic Flow Modifier
- **🌅 Shift 1: AM Class Entry (6:30 AM – 8:30 AM):** 1,400 students inbound $\implies$ ~2,100 foot strikes.
- **🔄 Shift 2: Midday Rush (11:30 AM – 1:30 PM):** 2,200 students crossing each other in bi-directional traffic $\implies$ ~3,300 foot strikes (peak energy surge).
- **🌙 Shift 3: PM Departure & Night Lights (5:00 PM – 8:00 PM):** 1,600 students outbound at dusk with active overhead streetlight illumination.
- **🔁 24h Full Day Cycle:** Automatically cycles through all three shifts to demonstrate a full 7,800-step campus day.

### 3. 👥 Population & Stepper Dynamo Sizing Engine
- Mathematically computes exact **hours and minutes** of usable power based on student population:
  - 📱 **Phone 5V Fast Charging:** Total hours/minutes and count of 4,000mAh smartphones recharged.
  - 💡 **Night Streetlights & Pathway Lamps:** Hours/minutes of powering 3W corridor pathway lamps & 10W streetlamps.
  - 🔌 **Free Student Power Outlet (E-Bench):** Hours/minutes running a 2.5W pocket Wi-Fi router or 4W portable fan.
  - 🚨 **Campus SOS Emergency Call Box:** Days/hours of 0.5W standby monitoring & 5W active voice intercom.

### 4. 💰 3-Level Progressive Budgeting Roadmap (Philippine Pesos ₱)
- **🟢 Level 1: Lab Proof-of-Concept (Spend Right Now):** **₱ 140.00 MAX** (*₱ 35.00 / student* for a 4-person team).
- **🟡 Level 2: Semi-Autonomous Buffer (Semester-End):** **₱ 480.00 TOTAL** (*₱ 120.00 / student*).
- **🟣 Level 3: Full 4th-Year Capstone Production Grid:** **₱ 1,850.00 TOTAL** (*₱ 462.50 / student*).

### 5. 📸 Hardware Build Requirements & Stock Photo Gallery
Features high-resolution photo specifications and scrap sourcing origins for all 4 primary physical components:
1. **Recycled HDPE Pavement Eco-Brick** (Melted bottle caps, ₱0.00)
2. **PZT-5A 35mm Piezoelectric Ceramic Discs** (₱140.00 / 16 pcs)
3. **Scrap Stepper Motor Micro-Dynamo** (Salvaged from e-waste printers, ₱0.00)
4. **AR101 Embedded Controller & Bus Unit** (Arduino Nano + 16x2 I2C LCD, ₱0.00)

### 6. 📐 3D CAD Exploded Stackup & Orthographic Blueprints
- Interactive 3D CSS orbital viewport showing layer-by-layer explosion (Eco-brick, plunger studs, piezo bed, return springs, sub-chassis).
- Vector SVG blueprint ([piezo_floor_blueprint_schematic.svg](piezo_floor_blueprint_schematic.svg)) and AutoCAD DXF file ([piezo_floor_generator_blueprint.dxf](piezo_floor_generator_blueprint.dxf)).

---

## 🧠 AR101 Computer Architecture Mapping

1. **Hardware Interrupt Line (`INT0` / Digital Pin 2):**  
   The mechanical foot strike generates a voltage impulse tripping the external interrupt. This wakes the ATmega328P CPU from `SLEEP_MODE_PWR_DOWN`, mimicking energy-aware low-power processor architectures.
2. **10-Bit ADC Data Bus (`ADMUX` & `ADCSRA` Registers):**  
   The rectified capacitor rail is sampled across a 10:1 resistor divider into ADC Channel 0. The quantized 10-bit digital word is moved across the internal data bus into CPU general-purpose registers.
3. **Energy Register Arithmetic ($E = \frac{1}{2} C V^2$):**  
   Internal register arithmetic computes instantaneous and cumulative Joules harvested across student traffic.
4. **I2C System Bus Interface:**  
   Pushes real-time step counts and power telemetry over the two-wire serial bus (SDA/SCL) to memory-mapped address `0x27` on the 16x2 LCD display.

---

## 🚀 Running Locally

```bash
# Clone the repository
git clone https://github.com/nbyakul31-prog/ecostep-qcu-harvester.git

# Navigate to project directory
cd ecostep-qcu-harvester

# Start a simple local server
python -m http.server 8080
```
Open **`http://localhost:8080`** in your browser.

---

## 📄 Documentation
- Full Academic Specification & Literature Review: [`QCU_Piezoelectric_Floor_Generator_Research_and_SRS.md`](QCU_Piezoelectric_Floor_Generator_Research_and_SRS.md)
- Vector Blueprint CAD Schematic: [`piezo_floor_blueprint_schematic.svg`](piezo_floor_blueprint_schematic.svg)
- AutoCAD DXF Drawing: [`piezo_floor_generator_blueprint.dxf`](piezo_floor_generator_blueprint.dxf)

---
*Quezon City University · Department of Information Technology · 3rd Year BSIT · Academic Year 2025–2026*
