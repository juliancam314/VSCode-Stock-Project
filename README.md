# Stock Project

This project analyzes stock data using Python and various libraries.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Plots](#plots)

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

## Plots

The plots included in this project are designed to offer a comprehensive view of stock performance. For my purposes I chose to look at the AAPL stock, however any of the four stocks I included can be used!

The Adj. Close over a year

![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure_1.png?raw=true)

The volume of the stock traded over a year
![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure_2.png?raw=true)

The Moving Average
![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure_4.png?raw=true)

The Daily Returns of the stock
![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure_5.png?raw=true)
![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure_6.png?raw=true)

The next four plots are used show the correlation between the stocks in the list:

Joint Plot to show correlation between AMZN and AAPL stock
![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure_7.png?raw=true)

Pairplot to compare every combination of stocks in the list
![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure_8.png?raw=true)

Pairgrid to repeat analysis of all combinations
![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure_9.png?raw=true)

Heatmap to show correlation
![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure_10.png?raw=true)

The final plot below shows the risk of each stock. Furthermore, the quantile function was used to caluclate the risk of each stock.
![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure_11.png?raw=true)
![App Screenshot](https://github.com/juliancam314/VSCode-Stock-Project/blob/master/Figure%2013.JPG?raw=true)
