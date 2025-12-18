# 🎓 College Help Desk Chatbot (Rasa Framework)

## Project Overview

The **College Help Desk Chatbot** is a conversational AI application built using the **Rasa framework**. The chatbot assists users by answering common college-related queries such as admissions, courses offered, fee structure, facilities, college timings, location, and contact information.

This project was developed **as part of an academic requirement** to gain practical experience in chatbot development, Natural Language Understanding (NLU), and dialogue management.

---

## Objectives

* To design and implement a chatbot for a real-world college help desk scenario
* To understand the working of **intents, entities, stories, rules, and actions** in Rasa
* To provide quick and accurate responses to common student queries
* To gain hands-on experience with **NLU training data** and conversational flow

---

## Features

* Admission process information
* Course and fee details
* College facilities and infrastructure
* College timings and location
* Contact information support
* Web-based chat interface
* Dockerized deployment support

---

## Technologies Used

* **Python**
* **Rasa Framework**
* **Docker**
* **YAML** (for training data and configuration files)
* **HTML / JavaScript** (for frontend interface)

---

## Project Structure

```
college-help-desk-chatbot/
├── data/
│   ├── nlu.yml          # Intents and example user queries
│   ├── stories.yml      # Conversation flows
│   └── rules.yml        # Rule-based interactions
├── actions/
│   ├── __init__.py
│   └── actions.py       # Custom actions for responses
├── config.yml           # NLU pipeline and policies
├── domain.yml           # Intents, entities, responses, actions
├── endpoints.yml        # Action server configuration
├── Dockerfile           # Docker configuration
├── index.html           # Web-based chat interface
└── README.md            # Project documentation
```

---

## How the Chatbot Works

1. The user enters a query related to the college
2. Rasa NLU identifies the **intent** of the query
3. The dialogue manager selects the appropriate **story or rule**
4. The chatbot responds with relevant college information

---

## Intents Covered

* `greet` – Greeting messages
* `admission_info` – Admission-related queries
* `course_info` – Courses offered
* `fee_info` – Fee structure queries
* `facilities_info` – College facilities
* `contact_info` – Contact details
* `goodbye` – End of conversation

---

## How to Run the Project Locally

### 1️.Install Rasa

```bash
pip install rasa
```

### 2️.Train the Model

```bash
rasa train
```

### 3️.Run the Action Server

```bash
rasa run actions
```

### 4️.Start the Chatbot

```bash
rasa shell
```

---

## Run Using Docker

```bash
docker build -t college-helpdesk-chatbot .
docker run -p 5005:5005 college-helpdesk-chatbot
```

---

## Academic Relevance

This project fulfills academic requirements by demonstrating:

* Practical application of conversational AI concepts
* Use of the Rasa framework for real-world problem solving
* Implementation of intent-based and rule-based dialogue systems


