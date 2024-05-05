# Stock Project

This project analyzes stock data using Python and various libraries.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Introduction

This project analyzes stock data for a selected list of tech companies, including Apple (AAPL), Google (GOOG), Microsoft (MSFT), and Amazon (AMZN). It uses the Yahoo Finance API to fetch stock data and various Python libraries such as Pandas, Matplotlib, and Seaborn for data analysis and visualization.
In this project I try to answer the following questions:

1.) What was the change in price of the stock over time?

2.) What was the daily return of the stock on average?

3.) What was the moving average of the various stocks?

4.) What was the correlation between different stocks' closing prices?

5.) What was the correlation between different stocks' daily returns?

6.) How much value do we put at risk by investing in a particular stock?

7.) How can we attempt to predict future stock behavior?
## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine:
git clone https://github.com/juliancam314/VSCode-Stock-Project.git
2. Install the required dependencies:
pip install -r requirements.txt
3. Run the main script:
python main.py


## Usage

After following the installation steps, you can explore the stock data analysis provided by the project. The main script (`main.py`) fetches stock data, performs data analysis, and generates visualizations such as line plots, histograms, and correlation plots.

## Dependencies

The project relies on the following Python libraries:

- pandas
- numpy
- matplotlib
- seaborn
- yfinance
- pandas_datareader

These dependencies are listed in the `requirements.txt` file.

