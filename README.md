# DTSC-691-Capstone
In this project I built a baseball stat predictor.

Project Steps:
1. Build a webscraper and collect player data from www.baseball-reference.com into 2 datasets (1 for pitchers & 1 for batters)
2. Clean data 
   - Remove irrelevant columns and sub-headers
   - Resolve data type errors (Converted object values to their correct respective values)
   - Handle differing null values
   - Set minimal requirements for players (2+ seasons, 5+ games/season for pitchers, 15+ games & 2+ at bats/season for batters)
   - Grouped data
   - Reset Index
3. Setup Feature Selectors (Ridge Regression w/ Time Series Split)
4. Scale & Fit Data
5. Ran multiple Decision Tree models and determined best model based on MSE for each player stat
6. Compared best Decision Tree model for each stat to Linear regression models
7. Unscale Data
8. Create new Dataset comparing actual stats to the predicted stats
9. Build a simple Flask app to display the data.

**NOTE: Changes were made due to limited time and issues with trying to run a successful LSTM model. Switched to Decision Tree and Linear Regression Models and compared them.**

