# Brief-Analysis-of-Nobel-Prize-Winners

Welcome to the Nobel Prize Data Analysis project! This project analyzes Nobel Prize data from 1901 to 2023, with a focus on identifying patterns related to gender, nationality, and multiple Nobel Prize winners. The task involves answering several key questions using the available dataset. Below, I’ll walk you through the analysis and explain the key findings.

## Task Overview

The primary goal of this project is to analyze the Nobel Prize dataset and answer the following questions:
1. **What is the most commonly awarded gender and birth country?**
2. **Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?**
3. **Which decade and Nobel Prize category combination had the highest proportion of female laureates?**
4. **Who was the first woman to receive a Nobel Prize, and in what category?**
5. **Which individuals or organizations have won more than one Nobel Prize throughout the years?**

## What the Code Does

The analysis uses the Nobel Prize dataset and provides answers to the above questions. Here's a breakdown of how the code works:

### 1. Most Common Gender & Birth Country
The code finds the gender and birth country with the highest number of Nobel laureates. These results are stored as variables `top_gender` and `top_country`.

### 2. US-Born Nobel Prize Winners by Decade
The dataset is analyzed to identify the decade with the highest ratio of US-born Nobel Prize winners. The result is stored as an integer variable `max_decade_usa`.

### 3. Highest Proportion of Female Laureates by Decade & Category
The code computes the proportion of female laureates by decade and Nobel Prize category, and identifies the combination with the highest proportion of women. This information is stored in a dictionary called `max_female_dict`.

### 4. First Woman to Win a Nobel Prize
The first woman to win a Nobel Prize is identified, along with the category she won. The results are stored as strings `first_woman_name` and `first_woman_category`.

### 5. Multiple Nobel Prize Winners
The code identifies individuals or organizations that have won more than one Nobel Prize. The names of these repeat winners are stored in a list called `repeat_list`.

### Visualizations
The project also includes visualizations to represent:
- The proportion of US-born winners over the decades.
- The proportion of female laureates by decade and category.
- A bar chart showing individuals or organizations with multiple Nobel Prize wins.

## How It Works

The code processes the Nobel Prize dataset using **pandas** for data manipulation and **seaborn** and **matplotlib** for visualizations. The main steps include:
1. Loading the dataset and performing data wrangling to clean and organize the data.
2. Performing group-by operations to analyze the data and compute the answers.
3. Displaying the results and visualizations for further insights.

## Requirements

To run the code, you'll need the following libraries:
- pandas
- matplotlib
- seaborn
- numpy

## Conclusion
This project provides insights into the Nobel Prize data, helping to identify key trends related to gender, nationality, and repeated winners. It was a great opportunity to practice data analysis, visualization, and answer interesting questions about one of the most prestigious awards in the world.

Thanks for checking out my Nobel Prize Data Analysis project!
