# HR Analytics

An exploratory Human Resources data analysis project developed with Python, Pandas, and Matplotlib. Its goal is to transform employee data into useful insights about salaries, departments, job roles, performance ratings, and company tenure.

## Features

The project calculates and displays the following information in the terminal:

- total number of employees;
- average, highest, and lowest salaries;
- average employee age;
- average company tenure;
- department with the highest salary;
- average salary by department;
- number of employees by department;
- job role with the highest average salary;
- most common job role;
- number of developers;
- highest performance rating and average rating;
- employees with a performance rating above 9;
- employees with the longest and shortest company tenure;
- highest-paid employee.

The project also creates four charts:

1. average salary by department;
2. salary distribution histogram;
3. employee distribution by department;
4. number of employees by job role.

## Technologies

- Python 3
- Pandas
- Matplotlib

## Project structure

```text
HR_Analytics/
├── data/
│   └── employees.csv
├── HR_analysis.py
└── README.md
```

## Dataset

The `data/employees.csv` file contains the following columns:

| Column | Description |
|---|---|
| `ID` | Employee identifier |
| `Nome` | Employee name |
| `Idade` | Age |
| `Sexo` | Gender |
| `Cargo` | Job role |
| `Departamento` | Department |
| `Salario` | Salary |
| `Tempo_Empresa` | Company tenure in years |
| `Avaliacao` | Performance rating |

## Getting started

Clone the repository and navigate to the project directory. Then create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install pandas matplotlib
```

Run the analysis from the repository root:

```bash
python HR_Analytics/HR_analysis.py
```

The analysis results will be displayed in the terminal, and a window containing the four charts will open. Close the chart window to finish the program.

## Key learnings

This project applies the following concepts:

- reading and exploring CSV files;
- creating reusable Python functions;
- filtering and selecting data;
- aggregating data with `groupby()`;
- descriptive statistics;
- handling ties between minimum and maximum values;
- creating bar charts, pie charts, and histograms.

## Author

Developed by Joaquim Koster as part of his studies in Python for data analysis.
