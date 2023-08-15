# Outline

## Meet Your Instructor


## Lesson Introduction


## What is Airflow?


## Key terms and concepts


## Hello World and Airflow UI


## Directory Structure and Dag Structure


## Initialize a Dag Object
- Steps 1-6 `dag.py`

## Add task_1

### Part 1
- Initialize the operator

### Part 2
- Context Variables

### Part 3
- Hooks

### Part 4
- Pushing to xcom
    - Maybe s3 push example

## Add task_2
- Pull from xcom
    - Maybe s3 pull example
- Push to xcom

## Add task_3

### Part 1
- PostgresOperator

### Part 2
- Templating
    - Inserting a variable via params

## Add task_4
- Templating
    - Pulling from xcom

## Setting Dependencies
- Introduction to Syntax
- Setting dependencies (pokemon)
- Extra practice

## Final Assignment
- Intro do files
- Solution Video





## Airflow Scheduling

In airflow 2, the dag schedule is based on something called a **data interval**.

A **data interval** consists of two timestamps. 
1. The `data_interval_start` timestamp
2. The `data_interval_end` timestamp

Crucially, **a dag is activated at the _end_ of the data interval _not_ the start.**

### So how is the data interval calculated?

- When you initialize a DAG, the dag's `start_date` argument becomes the `data_interval_start` for the very first scheduled run of the dag. 
- The `data_interval_end` timestamp is calculated from the dag's `schedule` argument. 

**So...**

> If you set the `start_date` to `"12/01/23 8:00AM"` and the `schedule` to `"@hourly"`, airflow adds 1 hour to the start_date and `"12/01/23 9:00AM"` becomes the `data_interval_end`

Then for the second scheduled run of the dag, `"12/01/23 9:00AM"` becomes the `data_interval_start` and `"12/01/23 10:00AM"` becomes the `data_interval_end`. 


# Video Notes
2. In the terminal I should have types sys.path.append, and I should also demonstrate fixing the issue and observing the error message disappear. 
