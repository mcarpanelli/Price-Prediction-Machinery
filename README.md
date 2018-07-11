# Case Study: Prediction of Heavy Machinery Auction Prices
June 25, 2018

## Objective
This Case Study aims at applying Linear Regression algorithms to predict the auction price of heavy machinery equipment.


## Findings
* The best predictors for the auction price of a machine are (i) the type of machine, (ii) some measure of weight or size (depending on the machine type), and (iii) the machine's enclosure.
* Even though the age of a machine is strongly correlated with the price, after adding controls the size of the association is low (i.e. small estimated coefficient).
* Statistically-significant predictors related to the market conditions of the transaction, such as the state and the auctioneer, have a small association with price (i.e. small estimated coefficients).


## Data
The data is sourced from auction result postings and includes information on usage and equipment configurations. The dataset is sparse and consists of 53 features and >400,000 rows. Many of the features contained mixed datatypes and/or presented a high share of missing values.

Intuitively, important features to determine machinery price (target) should capture:
* function or type of machinery
* depreciation (proxy: age)
* size and/or power
* energy consumption
* comfort of use (proxy: enclosure)

Moreover, a machine's price could be affected by market conditions captured by the dataset, such as:
* state in which the auction takes place
* who the auctioneer is

## Data Cleaning & Feature Engineering
* Log(price)
* Fill in NaNs
* Age
* Creation of dummies from categorical variables

## Modeling
3 algortihms were tried for the same model specification:
* Linear Regression
* Ridge
* Lasso

The model evaluation was based on Root Mean Squared Log Error.

## Results

| Model  |  Error     |
| ------------------------ | ------------- |
| OLS                 | 0.4083        |
| Ridge (L2)          | 0.4082        |
| Lasso (L1)          | 0.4083        |

[Coefficients]: https://github.com/mcarpanelli/Case-Study-Tractors/blob/master/coefficients.png?raw=true

![Coefficients]


Pros
* Low errors
* Intuitive interpretation of estimates (betas)

Cons
* High complexity, i.e. too many features

## Team
* [Ini](https://github.com/inistar)
* [Cosma](https://github.com/cosmakufa)
* [Olga](https://github.com/olgaiushchenko/)
