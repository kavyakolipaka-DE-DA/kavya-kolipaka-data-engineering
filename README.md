# Kavya Kolipaka — Data Engineering Portfolio

Welcome to my Data Engineering portfolio.

This repository contains hands-on projects focused on building scalable data pipelines, ETL/ELT workflows, data processing, cloud data platforms, data quality, and workflow automation.

## About Me

I am a Data Engineer with experience working with Python, SQL, PySpark, AWS, Databricks, and modern data engineering technologies.

My focus is on designing reliable data pipelines, transforming and validating data, and building automated data workflows.

## Technical Skills

### Programming & Query Languages

* Python
* SQL
* PySpark
* Scala

### Data Engineering

* ETL / ELT
* Data Pipelines
* Data Transformation
* Data Validation
* Data Quality
* Change Data Capture (CDC)
* Data Modeling

### Big Data & Processing

* Apache Spark
* PySpark
* Delta Lake

### Cloud & Data Platforms

* AWS
* Amazon S3
* AWS Glue
* Amazon Athena
* Databricks
* Unity Catalog

### Workflow & Orchestration

* Apache Airflow
* Stonebranch
* GitHub Actions

### Development & Tools

* Git
* GitHub
* YAML
* DBeaver
* SQL Workbench

## Portfolio Projects

### 1. AWS Data Lake Pipeline

A cloud-based data pipeline demonstrating ingestion, transformation, validation, and storage using AWS services.

**Technologies:** Python, AWS S3, AWS Glue, Athena

### 2. PySpark ETL Pipeline

A scalable ETL pipeline demonstrating data ingestion, transformation, cleansing, and validation using Apache Spark.

**Technologies:** Python, PySpark, Apache Spark

### 3. Data Quality Framework

An automated framework for validating data quality through record counts, schema validation, null checks, and reconciliation.

**Technologies:** Python, SQL, PySpark

### 4. Airflow Data Pipeline

An orchestrated data pipeline demonstrating scheduling, dependencies, monitoring, and automated execution.

**Technologies:** Python, Apache Airflow

### 5. Databricks Lakehouse Project

A lakehouse implementation demonstrating data ingestion, transformation, Delta Lake, and data management.

**Technologies:** Databricks, PySpark, Delta Lake, SQL

## Repository Structure

```text
kavya-kolipaka-data-engineering/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── projects/
│   ├── aws-data-pipeline/
│   ├── pyspark-etl/
│   ├── data-quality/
│   ├── airflow-pipeline/
│   └── databricks-lakehouse/
│
├── tests/
│   └── test_basic.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## CI/CD

This repository uses GitHub Actions for continuous integration.

The workflow automatically:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Checks Python syntax
5. Runs automated tests

```text
Code Change
     ↓
Git Push / Pull Request
     ↓
GitHub Actions
     ↓
Install Dependencies
     ↓
Code Validation
     ↓
Automated Tests
     ↓
Pass / Fail
```

## Development Workflow

Projects are developed using feature branches and Pull Requests.

```text
main
  │
  └── feature/project-name
          │
          ├── Develop
          ├── Test
          └── Commit
                ↓
          Pull Request
                ↓
          GitHub Actions
                ↓
             Review
                ↓
          Merge to main
```

## Future Improvements

Planned additions include:

* Advanced PySpark pipelines
* AWS cloud data lake architecture
* Data quality automation
* CDC pipelines
* Apache Airflow orchestration
* Databricks and Delta Lake projects
* Unit and integration testing
* CI/CD deployment automation
* Data pipeline monitoring

## Contact

**Kavya Kolipaka**

Data Engineer | Python | SQL | PySpark | AWS | Databricks
