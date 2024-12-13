# Research-Project-Code
All the code generated for big data analytics research project.

# Abbreviations
1. BN: Bayesian network
2. NN: neural network
3. RQ1: research question 1
4. RQ2: research question 2

# Variables used in the data generation project

1. **IR (Interest Rate)**: Represents the base interest rate set by a central bank, influencing economic conditions.
2. **EI (Economic Indicator)**: General measure indicating the economic health of a region, such as GDP growth or unemployment rates.
3. **IRT (Interest Rate Trend)**: Describes the trend or movement of interest rates over a given period (e.g., increasing, stable, decreasing).
4. **MS (Market Sentiment)**: Reflects the overall attitude of investors toward a particular market or economy.
5. **GEO (Geopolitical Status)**: Refers to the current state of geopolitical affairs, such as stability, conflict, or trade relationships. In some other codes, it is also the Geographic Classification/Area Type, which represents the type of region or area in consideration, such as urban, suburban, or rural. However, they both contribute the same.
6. **UE (Unemployment Rate)**: Indicates the percentage of the labor force that is unemployed and actively seeking work.
7. **GDP (Gross Domestic Product)**: Total economic output of a country, measuring economic performance and growth.
8. **INF (Inflation Rate)**: Represents the rate at which the general price level of goods and services is rising, eroding purchasing power.
9. **IRP (Interest Rate Policy)**: Policies implemented by central banks regarding interest rates to control economic activity.
10. **INV (Investment Levels)**: Measures the amount of investment occurring in a region or market, indicating economic confidence.
11. **CI (Consumer Index)**: Gauge of consumer confidence or spending, indicating economic sentiment among consumers.
12. **OIL (Oil Prices)**: Represents the current price of oil, a critical factor influencing global economies and industries.
13. **FX (Foreign Exchange Rate)**: Indicates the value of one currency in relation to another, affecting international trade and investments.
14. **IRB (Interest Rate Balance)**: Refers to the equilibrium between short-term and long-term interest rates, impacting economic stability.
15. **SP (Stock Performance)**: Outcome variable representing the overall performance or trend of the stock market (e.g., increase, stable, decrease).

These nodes collectively create a complex network reflecting the interactions and dependencies among different economic and market factors.

# Code Use
- `NN 1_3 3`: Neural network with 1 hidden layer and 3 nodes (25 epochs and batch size 16), trained on data that contains only 3 variables. This same code was also used to train a NN with 6 hidden layers and 30 nodes per layer (500 epochs and batch size 320). This data was used for both RQ1 and RQ2.
