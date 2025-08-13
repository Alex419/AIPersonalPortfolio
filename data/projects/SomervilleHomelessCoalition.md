# Project: Somerville Homeless Coalition Application Processing Tool (Tufts JumboCode) (Fall 2023 - Spring 2024)

## Project Overview
This portfolio entry details the development of a web application for the **Somerville Homeless Coalition (SHC)**, a local non-profit with the mission to provide homeless and nearly homeless individuals and families with individualized supportive services and tailored housing solutions with a goal of obtaining and maintaining affordable housing. Completed as a project through **Tufts JumboCode** during **Fall 2023 - Spring 2024**, this initiative directly addressed a critical operational bottleneck in the SHC's process for handling financial relief applications. We developed a user-friendly website designed to **streamline application processing**, empowering SHC workers to efficiently match clients with eligible funding sources and manage their data.

## Problem Statement
Following the COVID-19 pandemic, the Somerville Homeless Coalition experienced a significant surge in applications for financial relief. A major operational bottleneck emerged because only a limited number of staff members possessed the specialized knowledge required to accurately process these applications and determine client eligibility for various benefits. This reliance on a few experts caused delays, meaning individuals urgently needing financial assistance faced extended waiting times, as the SHC lacked the capacity to review and process the high volume of applications quickly and consistently.

## Solution Overview
Through Tufts JumboCode, we developed a **secure, intuitive web application** tailored to the SHC's specific needs, designed to alleviate their application processing bottleneck and improve service delivery. The website's core functionalities were engineered to make it much easier for SHC workers to understand what benefits clients were eligible for, by using real-life eligibility questions to instantly match them with available help.

### Core Requirements Fulfilled:
* **Matching Tool**: The central and most critical feature, enabling the system to automatically display eligible funding sources to clients based on their input.
* **Secure Login**: Only authorized SHC workers have the ability to authenticate themselves and access the administrative dashboard and matching tool.
* **Dashboard**: Provides SHC workers with comprehensive capabilities to view, edit, add, and delete funding sources.
* **Register Users**: Authenticated SHC workers are empowered to register additional users, facilitating team collaboration and expanded access.


## Technical Workflow & Implementation
The application operates on a robust **full-stack architecture**, built for efficiency and ease of use:

1.  **Admin & Client Interaction**: An SHC worker collaboratively gathers and consolidates a client’s financial information.
2.  **Frontend Data Input**: This information is securely inputted by the SHC worker into a **React.js frontend**.
3.  **Backend Server Processing**: The data is transmitted to a server built with **Node.js** and **Express.js**, where compatibility with various funding sources is checked.
4.  **Database Query**: Funding source data is retrieved from a **MongoDB** database, and eligible matches are sent back to the frontend.

### The Matching Algorithm
The application's core logic is a **matching algorithm**, designed based on a predefined set of eligibility questions provided by the SHC to obtain comprehensive client information.
To determine a client's eligible funding sources, our algorithm:
* Queries the database with information derived from each question in isolation.
* Utilizes **set operations** to combine and filter the results from these individual queries, producing the final consolidated list of eligible funding sources.

### Key Functionalities
* **Automated Matching Tool**: For instant client-to-resource pairing.
* **Add/Edit/Delete Funding Source Functionality**: Enabling dynamic management of available resources.
* **Secure Login/Logout Functionality**: For authorized worker access and data protection.

## Learnings & Skill Development
This project, undertaken as part of Tufts JumboCode, offered invaluable practical lessons in both technical development and the essential non-technical aspects of delivering real-world software solutions to a client:

### Technical Learnings
* **Full-Stack Web Development**: Gained hands-on experience across the entire web stack, using **React.js** for frontend, **Node.js/Express.js** for backend, and **MongoDB** for database integration.
* **Deployment**: Practical understanding of deploying web applications, specifically utilizing **Vercel** for frontend deployment.
* **Security Fundamentals**: Implemented critical security practices such as **salting and hashing** for robust user authentication.
* **API Design**: Gained experience in designing and implementing **RESTful API endpoints** for CRUD (Create, Read, Update, Delete) operations.
* **Algorithmic Design**: Developed a practical matching algorithm leveraging set operations for efficient data filtering.

### Non-Technical Learnings
* **Client Management & Needs Assessment**: Engaged directly with a non-profit client, translating their real-world operational challenges into clear software requirements and user stories.
* **Team Collaboration**: Gained insights into effectively working within a software development team.
* **Project Management & Ticketing**: Learned the importance and methods of writing clear, actionable development tickets for organized workflow.
* **User Onboarding & Training**: Acquired experience in teaching client-side users how to effectively use the newly developed web application, ensuring adoption and maximizing impact.
* **Communication**: Developed skills in clear and consistent communication with stakeholders.


## Project Deliverables & Future
* **Live Application**: The completed website is accessible at: **https://somerville-homeless-coalition.vercel.app/**
* **Maintenance & Documentation**: Provided comprehensive documentation for the general file structure (`shc-app/src/components`, `shc-app/src/pages`, `shc-app/src/util`, `backend/index.js`), user credentials for initial setup, and general maintenance guidance, empowering the SHC to manage the website independently.
This project demonstrates my ability conceptualize, develop, and deliver a full-stack web application that directly solves a critical operational problem for a real-world client, combining technical expertise with strong project management, client communication, and a focus on social impact.