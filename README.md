# Job Skill Analyzer

**A Python-powered tool to extract actionable skills from ~200 MB of job postings and deliver tailored learning resources.**

![Demo](2EF5AD87-8A51-4F83-A6F2-7F67840EEE4B.jpeg)

## Overview
This project turns raw job data into career gold:
- **Skill Extraction**: Mines nearly 200 MB of job postings with NLP to pinpoint must-have skills (e.g., "Experience with cloud technologies such as AWS, GCP").
- **Learning Resources**: Scrapes Coursera for courses to master job related skills fast.
- **Modern Interface**: Streamlit-driven web UI—intuitive, polished, and built for impact.

## Motivation
I built this to decode real-world job requirements and map them to actionable learning paths, it is built off of legally sourced Kaggle datasets instead of scraping platforms like LinkedIn. It’s about cutting through the noise of job boards with tech that delivers.



## Technology Stack
- **Python**: Core engine for robust, scalable logic.
- **Streamlit**: Web frontend that’s sleek and user-friendly.
- **spaCy**: NLP framework for precise skill extraction and filtering.
- **Selenium**: Automated scraping of Coursera resources.
- **pandas**: Handles ~200 MB of preprocessed job data with ease.

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd job-skill-analyzer

## Setup

1. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```
2. Run the application:  
   ```sh
   python main.py
   ```

## Features

- Loads job postings from datasets
- Extracts skills using NLP (Natural Language Processing)
- Displays skill-related sentences
- Provides a list of most common skills


----------------------------------------------------------------------------------------------
Built on publicly available job posting datasets from Kaggle
