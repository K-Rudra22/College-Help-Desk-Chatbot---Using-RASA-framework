# College Help Desk Chatbot 

A conversational chatbot built using **Rasa** to assist users with common college-related queries such as admissions, courses, fees, facilities, timings, location, and contact information.

## Academic Context

This project was developed as part of an **academic requirement**, with the objective of designing and implementing an intelligent conversational system for a real-world use case.

## Features
- Admission process information
- Available courses and fee details
- College facilities and infrastructure
- College timings and location
- Contact information support
- Web-based chat interface
- Dockerized deployment

## Tech Stack
- Python
- Rasa
- Docker
- HTML / JavaScript

## Project Structure
```bash
college-help-desk-chatbot/
├── data/
│   ├── nlu.yml
│   ├── stories.yml
│   └── rules.yml
├── actions/
│   ├── __init__.py
│   └── actions.py
├── config.yml
├── domain.yml
├── endpoints.yml
├── Dockerfile
├── index.html
└── README.md
```

## Run Locally

```bash
rasa train
rasa shell
```

## Run using Docker

```bash
docker build -t college-helpdesk-chatbot .
docker run -p 5005:5005 college-helpdesk-chatbot






