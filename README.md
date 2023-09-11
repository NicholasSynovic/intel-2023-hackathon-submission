# Intel 2023 Student Ambassador Hackathon Submission: DiagnoEase

> A prototype developed by Nicholas M. Synovic

## Table of Contents

- [Intel 2023 Student Ambassador Hackathon Submission: DiagnoEase](#intel-2023-student-ambassador-hackathon-submission-diagnoease)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
    - [Problem to Solve](#problem-to-solve)
    - [Our solution](#our-solution)
  - [AI Reference Kits Used Used](#ai-reference-kits-used-used)
  - [Design Doc](#design-doc)
  - [Slide Deck/ Presentation](#slide-deck-presentation)
    - [How to Install](#how-to-install)
    - [How to Run](#how-to-run)
    - [How to Uninstall](#how-to-uninstall)
  - [Video Submission](#video-submission)

## About

DiagnoEase is a web application developed for Empire General Hospital to assist
patients with self-diagnosis of many diseases through the usage of AI. While
this application does not meet the accuracy, care, and consideration that a
trained medical professional would (nor is it meant to), this application is
meant to improve patient-doctor communications by having patients report what
symptoms they are currently experiencing, and what top-5 diseases they could be
ailing from. Furthermore, as telehealth and remote healthcare options become
more available, it is expected that AI will play a crucial role in identifying
patient prognoses. Thus, it is critical that the AI infrastructure and
applications (such as this prototype) exist in order to test the efficacy of
such solutions.

### Problem to Solve

DiagnoEase is an automatic prognosis identification tool for Empire General
Hospital (a fake hospital) that is aimed at providing patients with a fast
result for self-reported symptoms.

It is not meant to replace the need for in-person, professional medical
checkups, but rather to provide a starting point for patients to engage in a
conversation about what disease(s) they may have with their healthcare
professional.

While not as accurate as a human professional, this proof-of-concept application
should provide the telehealth sector with a unique tool to screen patient
symptoms rapidly without engaging with a human operator.

### Our solution

I am building DiagnoEase, a web app, with a frontend and backend component.

The frontend is built using Streamlit, and the backend is built using FastAPI.

The data storage component is built using SQLite.

## AI Reference Kits Used Used

I used the following Intel AI Reference Kits:

- [Disease Prediction Using NLP](https://www.intel.com/content/www/us/en/developer/articles/reference-kit/disease-prediction.html)
- [Medical Imaging Diagnostics Using Computer Vision](https://www.intel.com/content/www/us/en/developer/articles/reference-kit/medical-imaging-diagnostics.html)

## Design Doc

The following image is the **rough** design that I followed for this project

[![artifacts/design.png](artifacts/design.png)](artifacts/design.png)

## Slide Deck/ Presentation

The following document contains a presentation of the project:

- [Presentation](artifacts/presentation.pdf)

### How to Install

1. Run: `make install`

### How to Run

1. Run: `make run`

### How to Uninstall

1. Run: `make uninstall`

## Video Submission

You can watch the video submission at:
[https://youtu.be/xyvEMmIxiEU](https://youtu.be/xyvEMmIxiEU)
