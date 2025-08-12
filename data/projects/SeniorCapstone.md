# Senior Capstone Project: DIY Gamma-Ray Spectrometer

## Project Overview

Our senior capstone project was an interdisciplinary effort to design, build, and thoroughly test a low-cost, student-engineered **Gamma Ray Spectrometer (GRS) payload**. The core objective was to demonstrate the feasibility of detecting gamma radiation and accumulating energy spectrum data using highly accessible components, contrasting sharply with conventional GRS systems that can cost upwards of hundred of millions of dollars. Our budget for this project was approximately **$2,000**. The project was an exploration into whether a DIY system could collect meaningful scientific data, focusing on creating a robust, reproducible prototype for future research.

## Core Problem & Motivation

Modern Gamma Ray Spectrometer (GRS) systems are prohibitively expensive, costing hundreds of thousands to millions of dollars. This cost severely limits access for underfunded schools, researchers in developing countries, and individuals needing spectroscopic data. Our primary motivation was to develop an affordable alternative that could still produce quality data, reflecting a broader ethical commitment to **equity and accessibility in science and engineering**.

## Key Design & Subsystems

The project aimed to develop a complete GRS circuit design and prototype, reproducible by others. To support potential high-altitude data collection (a reach goal for real-world data), we also designed two crucial, independent subsystems:

1.  **Gamma Ray Spectrometer (GRS) System:**
    * **Purpose:** Detect gamma radiation, convert it into an electrical signal, and extrapolate the energy level from that signal. Over time, accumulate signals to produce an energy spectrum graph (histogram of energy ranges vs. frequency).
    * **Inspiration:** Modeled after Professor Lavelle's research on gamma ray detection circuits.
    * **Components:** Utilized a Bismuth Germanate (BGO) crystal for detection. We designed our circuit for a **Teensy 4.1 microcontroller** (chosen for its smaller size and lighter weight compared to Arduino Uno, as per the inspiring paper's use case).

2.  **Temperature Control System:**
    * **Purpose:** To maintain the BGO crystal (essential for gamma ray detection) within its required stable operating temperature range, crucial for reliable data acquisition at varying altitudes.
    * **Methodology:** Relied heavily on **PID (Proportional-Integral-Derivative) control logic** to smoothly regulate the payload's internal temperature, taking into account current temperature and projecting future rates of change.

3.  **Altitude Control System:**
    * **Purpose:** Designed to monitor and control helium release from a weather balloon to regulate altitude changes. This was conceptualized to allow the GRS to stay at a desired altitude for sufficient data accumulation and ensure a controlled descent for payload recovery.
    * **Methodology:** Also based on **PID control logic**, similarly adjusting helium release smoothly over time.

## Our Process & Collaborative Approach

Our team, composed primarily of **Computer Science** students with additional expertise in **Physics** and **Electrical Engineering**, engaged in a highly iterative design and validation process. The initial phase heavily focused on **identifying potential issues**, including component suitability, ethical considerations, and logical challenges, to ensure a complete and robust design.

### Key Phases:

1.  **Research & Feasibility:**
    * Explored the viability of a low-cost gamma ray detection system given our resources and budget.
    * Researched commercially available sensors, legal/FAA requirements (for future launch), and power considerations.
    * Defined a realistic MVP: a self-contained payload that logs radiation and altitude data, built to survive extreme conditions (though never launched), and designed for recoverability.

2.  **Component Testing & Integration:**
    * Thoroughly tested individual components, including the gamma ray spectrometer, GPS module, barometric pressure/temperature sensors.
    * Developed Arduino code to integrate these components, continuously log data with timestamps, display system status, and handle errors (e.g., GPS loss, SD card issues) gracefully.
    * **We debugged countless hardware issues**, gaining significant real-world experience in breadboard grounding and modular code design.

3.  **Physical Payload Design & Construction:**
    * Focused on designing the layout of the payload and its components within a lightweight, insulated enclosure.
    * Designed for **internal thermal shielding**

4.  **Ground Tests & Validation:**
    * While the payload was never launched into the atmosphere, we conducted**on-the-ground simulations and tests** to validate its functionality and robustness.
    * This included continuous power tests to check for overheating/crashes, GPS testing, and simulating high-altitude inputs (low pressure, cold) for the temperature control unit.
    * We spent significant time **testing and tuning the PID control logic** for both the temperature and altitude control systems to ensure the code behaved as intended for smooth, accurate regulation.

## Technical Highlights & Artifacts

### Hardware Components
* **Gamma Ray Spectrometer (DIY):** Designed for detecting gamma radiation and outputting energy signals.
* **Bismuth Germanate (BGO) Crystal:** Core detection component.
* **Teensy 4.1 Microcontroller:** Main controller for interfacing all sensors and executing code.
* **GPS Module:** For simulated location and altitude data.
* **BMP280 Sensor:** For pressure and temperature sensing.
* **Heating/Cooling Elements:** Controlled by PID for temperature regulation.
* **Helium Valve (Conceptual):** For altitude control.

### Software
* **PID Control Logic:**
    * `AutoPID` library implementation for temperature regulation (`HEATER_PIN`, `FAN_PIN`) and conceptual altitude control (`HELIUM_VALVE_PIN`).
    * Adjusts analog outputs (`analogWrite`) based on PID calculations to maintain set points.

### Key Features
* **Autonomous Operation (Designed for):** Power on → log data → recovery.
* **Low-Cost Scientific Instrument:** Achieved a GRS system design within a $2,000 budget, significantly lower than commercial counterparts.
* **Robust & Reproducible Prototype:** Focused on reliability and ease of reproduction.
* **Temperature Control Unit:** Engineered to maintain internal payload temperature for optimal crystal performance.
* **Usable Data Generation:** Demonstrated the ability to produce a histogram of detected energy ranges summarizing GRS performance.

## Reflections & Lessons Learned

This capstone project was a profound learning experience, offering insights into multidisciplinary engineering and practical problem-solving:

### Technical Deep Dives
* **Hardware-Software Integration:** Gained real-world experience with the nuances of interfacing sensors, debugging electrical constraints, and ensuring robust data acquisition in challenging environments.
* **PID Control Mastery:** Applied and tuned PID control logic extensively for both temperature and conceptual altitude regulation, understanding its critical role in maintaining stable system states.
* **Circuit Design & Assembly:** Practical skills in breadboarding, circuit assembly, and foundational understanding of Printed Circuit Board (PCB) design principles for robust layouts.
* **Data Reliability:** Recognized that reliable data logging in real-world conditions (like high altitude) requires careful consideration of noise, power stability, and timing.
* **Value of Iterative Testing:** Rigorous dry runs proved indispensable for identifying subtle, critical issues that would otherwise go undetected until potential deployment.
* **Spectrometry Fundamentals:** Learned the structure and function of gamma ray spectrometers, including their detection principles and practical considerations.

### Teamwork & Process Insights
* **Interdisciplinary Collaboration:** Working across Computer Science, Physics, and Electrical Engineering backgrounds fostered crucial skills in translating complex technical concepts and aligning diverse perspectives.
* **Communication & Planning:** Highlighted the absolute necessity of clear, frequent communication and structured planning to manage project scope, avoid redundant efforts, and ensure efficient pivots when challenges arose.
* **Asking the Right Questions:** Learned that asking clarifying questions early and often significantly streamlines problem-solving and leads to more robust design choices, rather than over-engineering or attempting inefficient solutions.

### Ethics & Social Impact
* **Scientific Accessibility:** The project embodied an ethical commitment to equity in science and engineering by developing a low-cost GRS, thus expanding access to valuable spectroscopic data for underfunded institutions and individuals.
* **Regulatory Awareness:** Gained awareness of the legal and logistical considerations for high-altitude balloon deployment (e.g., restricted airspaces, permitting, safe payload recovery).

## Future Opportunities

* **Final Assembly & Lab Testing:** Assembling the final GRS with the custom PCB and conducting tests with radioactive isotopes in a physics lab setting.
* **High-Altitude Balloon Launch:** Planning and executing a high-altitude balloon launch to collect real-world data in the stratosphere.
* **Advanced Data Analysis:** Developing sophisticated post-flight analysis scripts for energy spectra interpretation.
* **Real-time Visualization:** Creating a web dashboard for live data visualization during flight.

This capstone project stands as a testament to my ability to contribute to complex interdisciplinary engineering endeavors. It showcases my practical skills in hardware-software integration, robust system design, data acquisition, and critical problem-solving in challenging, real-world contexts, while also demonstrating an appreciation for the broader impact and accessibility of scientific tools.