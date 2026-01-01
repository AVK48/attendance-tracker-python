# attendance-tracker-python
CLI-based attendance tracker built in public

# Project Overview

This project is a CLI-based Attendance Management System built using Python, designed to go beyond basic record-keeping and focus on data correctness, feature engineering, and ML-ready dataset construction.

The system allows managing student records, logging daily attendance with system-generated dates, and computing meaningful attendance analytics such as attendance percentage, longest consecutive presence streak, and consistency score. All attendance data is stored in an append-only format to preserve historical integrity.

A key focus of the project is data pipeline design:
Attendance logs are filtered by a user-defined date range
Records are explicitly sorted to ensure algorithmic correctness
Features are derived in a reproducible and time-bounded manner
Dataset validation rules are enforced to prevent logically invalid data

The project also includes functionality to generate a structured, per-student feature dataset (student_features.csv), where each row represents a student and each column represents a computed feature. This dataset is suitable as a foundation for future Machine Learning experiments.

Rather than using external libraries like pandas or ML frameworks, the project intentionally emphasizes core Python, algorithmic thinking, and defensive data engineering practices, making it a strong foundational system and a portfolio-ready artifact.

# Features

Student management
Attendance logging (append-only, dated)
Attendance summary (%, streak)
Time-bounded dataset generation
Dataset validation to prevent bad rows


# How to Run
python main.py

# Dataset Explanation

The project generates a structured dataset named student_features.csv, which represents a processed and validated view of raw attendance logs.

# Dataset Structure

Each row represents one student
Each column represents a derived feature
All rows share the same date range, ensuring temporal consistency
This dataset is designed to be ML-ready, meaning it can be directly used for analysis or model training without additional preprocessing.

# Columns Description
Column Name	Description
roll_no	Unique identifier for the student
from_date	Start date of the attendance window used to generate features
to_date	End date of the attendance window used to generate features
total_days	Total number of attendance records within the date range
present_days	Number of days the student was marked present
attendance_pct	Attendance percentage calculated as (present_days / total_days) * 100
longest_streak	Longest consecutive sequence of present days within the date range
consistency	Ratio of longest streak to total days, indicating behavioral consistency

# Time-Bounded Dataset Generation

The dataset is generated using a user-defined date range, ensuring that:
All features reflect the same time window
No future data is accidentally included
Datasets generated for different periods are comparable and reproducible

# Data Validation

# Before writing any row to the dataset, validation rules are applied to guarantee logical correctness:

total_days > 0
present_days ≤ total_days
0 ≤ attendance_pct ≤ 100
0 ≤ consistency_score ≤ 1
longest_streak ≤ total_days
Rows that violate these rules are skipped to prevent silent data corruption.

# Design Rationale

The dataset avoids reliance on external libraries and focuses on:
Explicit ordering of time-based data
Defensive programming practices
Clean separation between raw logs and derived features
This approach mirrors real-world data engineering workflows and ensures that downstream analysis or ML models can trust the data.





