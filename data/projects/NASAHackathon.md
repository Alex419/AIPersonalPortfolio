# Project: NASA ExoSky - Interactive Solar System Explorer (NASA Hackathon)

## Project Overview
NASA ExoSky was a highly ambitious project developed during a **NASA Hackathon (October 2024)**. Our team aimed to create an engaging educational tool for the younger generation to learn about our solar system and exoplanets, leveraging authentic NASA data. We developed an interactive web application that transformed planetary exploration into a game-like experience, fostering curiosity about the vastness of the universe.

## Problem Statement
Traditional methods of teaching astronomy to younger students can often lack interactivity and could fail to fully convey the scale and wonder of the cosmos. Existing resources, while factual, may not be engaging enough to capture and sustain the attention of a digital-native generation. The challenge was to create a dynamic, fun, and educational tool that made complex astronomical concepts accessible and exciting, directly utilizing NASA's vast datasets.

## Solution Overview
Our solution was an interactive web application that allows students to virtually "visit" different planets in our solar system and beyond, experiencing unique perspectives and engaging with generative AI. The application leverages real NASA data to dynamically alter the user's viewpoint, simulating what the solar system might look like from various celestial bodies. A key innovative feature allows users to draw their own constellations, which are then recognized by AI and used to generate personalized, fantastical stories, making learning a creative and memorable adventure.

## Technical Workflow & Implementation
The web application features a full-stack architecture integrating various cutting-edge technologies and APIs:
1.  **Starting Point: Earth View:** The application begins by placing the user on Earth, displaying the solar system from an Earth-centric perspective.
2.  **Interactive Constellation Drawing:** Users can draw their own constellations in the sky by connecting stars.
3.  **AI-Powered Constellation Recognition:**
    * The drawn constellation image is sent to the backend.
    * **YOLO (You Only Look Once)** image recognition is employed to identify what the student's drawing most closely resembles (e.g., an animal, an object).
4.  **Generative Storytelling:**
    * The identified object/concept is used as a prompt for **Groq's LLM API**.
    * Groq generates a fantastical, mythical story about why this newly "discovered" constellation exists, providing a fun name for it.
    * The story and name are sent back to the frontend for the student.
5.  **Planetary Exploration & Viewpoint Shift:**
    * Students can then either enter the name of another planet or choose to travel to a random exoplanet pulled from the **NASA Exoplanet Archive database**.
    * Using NASA data on planetary positions and distances from the Earth and Sun, the application dynamically calculates and renders a theoretical viewpoint of the solar system as it would appear from the newly "visited" planet.
6.  **Continuous Exploration:** From the new planet's perspective, users can again draw constellations and receive new stories, reinforcing the vastness and ever-changing perspective of the universe.

## Features Implemented
* **Interactive Solar System Viewer:** Dynamic visualization of the solar system from various planetary viewpoints (Earth, other planets/exoplanets).
* **Custom Constellation Drawing Tool:** Allows users to create their own constellations by connecting stars.
* **AI-Powered Image Recognition (YOLO):** Identifies user-drawn constellations.
* **Generative Storytelling (Groq):** Creates unique, mythical stories and names for user-defined constellations.
* **NASA Data Integration:** Utilizes data from the NASA Exoplanet Archive for planetary distances, positions, and discovery information.
* **Random Planet Exploration:** Enables discovery of new and unknown exoplanets from NASA's database.

## My Role & Contributions
As a hackathon participant, my role involved a blend of creative design and technical implementation:
* **Brainstorming & Design:** Contributed significantly to brainstorming exciting and engaging interactive designs for the web application, focusing on gamification elements for a younger audience.
* **Backend Development:** Assisted in building out the backend infrastructure, handling data processing, AI model integration, and API endpoints.
* **Frontend Development (React):** Created interactive frontend components using **React**, ensuring a highly engaging and intuitive user interface for students.
* **Data Integration:** Worked with NASA Exoplanet Archive data to calculate and estimate planetary distances and positions.

## Technology Stack
* **Frontend:** **React** (for the web application UI), **JavaScript** (core language).
* **Backend:** **Flask** (for the server logic and API endpoints).
* **Deployment:** **Azure Web Apps** (for deploying the backend server).
* **AI/ML Models & APIs:**
    * **YOLO:** For real-time image recognition of user drawings.
    * **Groq:** For rapid, generative storytelling based on identified constellations.
* **Data Sources:** NASA Exoplanet Archive.
* **Version Control:** Git/GitHub.

## Learnings & Skill Development
This hackathon project provided intensive, hands-on experience across multiple domains in a very short timeframe:

### Technical Learnings
* **Full-Stack Development:** Practical experience integrating React frontend with a Flask backend, deployed on Azure.
* **Generative AI Integration:** Hands-on experience with advanced LLM APIs like **Groq** for creative content generation.
* **Computer Vision (YOLO):** Applied real-time image recognition for user-generated content.
* **API Integration:** Sourced and utilized data from complex external APIs (NASA Exoplanet Archive).
* **Astronomical Data Handling:** Developed logic for distance calculations and positional mapping of celestial bodies using scientific data.
* **Rapid Prototyping:** Executed a complex project from concept to demoable product under tight hackathon constraints.

### Non-Technical Learnings
* **Ideation & Brainstorming:** Developed innovative educational concepts.
* **User-Centric Design:** Focused on creating an engaging and understandable experience for a specific target audience (younger students).
* **Communication & Presentation:** Developed skills in quickly conveying complex ideas and demonstrating a functional prototype.

## Project Deliverables & Future
* **Interactive Web Application Prototype:** A functional demo showcasing the full site flow, including constellation drawing, AI recognition, storytelling, and planetary exploration.
* **GitHub Repositories:**
    * Frontend: [https://github.com/departing-earth/departing-earth.github.io.git](https://github.com/departing-earth/departing-earth.github.io.git)
    * Backend: [https://github.com/slimjimcammy/departing-earth-server.git](https://github.com/slimjimcammy/departing-earth-server.git)

This project powerfully demonstrates my ability to rapidly conceptualize, design, and implement sophisticated, AI-driven web applications that deliver real educational value. It highlights my creativity, technical versatility across the stack, and strong problem-solving skills in high-pressure environments.