# Mini Hospital Management System & AI Study Scheduler

A dual-purpose Python application containing a CLI-based **Mini Hospital Management System** and an **AI-powered Study Schedule Optimizer** utilizing Machine Learning to calculate optimal study hours.

## 📋 Table of Contents

* [Features](#-features)
  * [1. Mini Hospital Management System](#1-mini-hospital-management-system)
  * [2. AI Study Schedule Optimizer](#2-ai-study-schedule-optimizer)
* [Prerequisites](#-prerequisites)
* [Installation](#-installation)
* [Usage](#-usage)
  * [Running the Hospital Management System](#running-the-hospital-management-system)
  * [Running the Study Schedule Optimizer](#running-the-study-schedule-optimizer)
* [Data & ML Pipeline Details](#-data--ml-pipeline-details)

## 🚀 Features

### 1. Mini Hospital Management System

A interactive Command-Line Interface (CLI) tool designed for managing patient records:

* **Add Patient**: Register new patients with auto-duplication checks on Patient ID.
* **Search Patient**: Quickly look up patient details by ID.
* **Display All Patients**: View full list of patients and their status.
* **Doctor & Department Assignment**: Assign doctors and relevant departments to patients.
* **Status Updates**: Track consultation progress (`Not Consulted`, `Waiting`, `In Consultation`, `Consultation Completed`).
* **Update & Delete**: Modify patient info or remove records from memory.
* **Statistics**: Instantly get the total count of registered patients.

### 2. AI Study Schedule Optimizer

An intelligent system powered by `scikit-learn` that predicts recommended daily study hours for courses based on student workload and performance metrics:

* **Synthetic Data Generation**: Generates course attributes (difficulty, credits, days until exam, current/target grades, and stress levels).
* **Random Forest Regression Pipeline**: Uses standardized features and a Random Forest Regressor to predict required study hours.
* **Priority Classification**: Categorizes subjects into `High Priority (Urgent)`, `Medium-High Priority`, or `Normal Priority`.
* **Capacity Adjustment**: Dynamically scales study schedule hours to fit within a maximum daily study budget (e.g., 7.5 hours/day).

## 🛠️ Prerequisites

Ensure you have Python 3.8+ installed on your system.

To run the Machine Learning script, install the required dependencies:

```
pip install numpy pandas scikit-learn
```

## 💻 Installation

1. **Clone the repository** or copy `minihospital.py` to your local environment.
2. **Navigate to the directory**:
   ```
   cd path/to/your/folder
   ```

## 📖 Usage

### Running the Script

Run the Python file directly from your terminal:

```
python minihospital.py
```

1. **Hospital Management Application**: Use the interactive terminal menu (Choices 1–9) to navigate patient registration, doctor assignments, and status updates.
2. **AI Study Scheduler**: The study optimizer logic runs after initializing the relevant setup, training the pipeline model on generated dataset features, and printing recommended daily study schedules scaled to a student's daily hour capacity.

## 🔬 Data & ML Pipeline Details

The AI Study Scheduler utilizes a Machine Learning pipeline configured as follows:

1. **Feature Engineering**:
   * `difficulty`: Subject difficulty rating (1 to 5)
   * `credits`: Subject credit hours (2 to 5)
   * `days_until_exam`: Days remaining before assessment (1 to 30)
   * `current_grade`: Current performance score (40–100%)
   * `target_grade`: Desired performance score (70–100%)
   * `stress_level`: Perceived stress level (1 to 5)

2. **Pipeline Steps**:
   * `StandardScaler`: Normalizes feature distributions.
   * `RandomForestRegressor`: Ensemble regressor trained with 100 decision trees to estimate required preparation hours.