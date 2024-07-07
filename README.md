# AirBnb_Capstone_Project
This repository contains the code and data for the Airbnb Capstone Project. The project aims to predict the appropriate listing prices for properties in Antwerp, Belgium, using various machine learning models. The final model selected is the Random Forest Regressor, which has been deployed using Streamlit for property price prediction.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Data Description](#data-description)
3. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
    - [Bivariate relationships using Scatterplot for Price Distribution](#bivariate-relationships-using-scatterplot-for-price-distribution)
    - [Correlation Heatmap](#correlation-heatmap)
    - [Feature Distributions](#feature-distributions)
4. [Feature Engineering](#feature-engineering)
5. [Modeling](#modeling)
    - [Train/Test/Validation Split](#traintestvalidation-split)
    - [Model Comparison](#model-comparison)
    - [Final Model](#final-model)
6. [Model Deployment](#model-deployment)
7. [Conclusion](#conclusion)
8. [Files in the Repository](#files-in-the-repository)
9. [License](#license)
10. [Contact](#contact)


## Project Overview

The objective of this project is to build a machine learning model that can suggest appropriate listing prices to property owners when they list their properties for rent on Airbnb. The dataset used for this project includes various attributes of the Calender, listings, hosts, and reviews.


## Data Description

The dataset comprises four tables:

1. **Calendar**: Contains information about listing availability and pricing over time.
2. **Listings**: Includes detailed information about each property listing.
3. **Hosts**: Contains information about the hosts who have posted the listings.
4. **Reviews**: Includes reviews left by guests who have stayed at the properties.


## Exploratory Data Analysis (EDA)

### Bivariate relationships using Scatterplot for Price Distribution

**1. Analysis by Location Coordinates("Lat/Long")**:

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/8a357456-0b58-4f99-ba43-f13073a18e7a) 
![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/5fbbea85-c21c-4ae3-80a2-016be0dcde45)


- Most of the properties are located between 51.207870 and 51.220905 latitude.

- Prices of the properties are high between the latitudes 51.200 and 51.250.

- Most of the properties are located between 4.400140 and 4.424660 longitude.

- The prices of the properties are relatively high between the longitudes.

**2. Analysis by Accommodates**:

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/b6d23d6a-6156-4283-885a-a0384f331e09)

- The accommodation varies from 1 to 16 depending on the property type.

- The prices of the even number of accommodations are relatively higher.

**3. Analysis by Bedrooms**:

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/d342a825-c24e-4096-8585-7600214eff89)

- Most of the properties offer 1 to 5 bedrooms according to the room type.

- The highest price was for a single bedroom.

**4. Analysis by Amenities**:

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/d5266ab1-1fa1-44a5-bab0-f50c53d40b93)

- The price increases when the property offers more basic amenities that are provided by all the properties.

**5. Analysis by Booking Month**:

- Analysis using Line Chart on the basis of Change in Average price of Property Monthly

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/21656fe7-fd10-4abe-a94a-dbb6d7f2953e)

- The average price **increases** in the **winters**.

**6. Analysis by Day wise**:

- Analysis on the basis of Change in Average price of Property Day wise

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/e9089c95-5844-48d3-8aff-f8a40091dd28)

- The average price **increases** on Weekends i.e. **Friday & Saturday**

### Correlation Heatmap

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/1d6db7ef-2b1e-4bd4-b05a-0753e4106d1f)

**Price Correlations**:

- Bathroom Number: The number of bathrooms has a moderate positive correlation with price (0.24).
- Bedrooms: The number of bedrooms shows a positive correlation with price (0.25).
- Accommodates: The number of people the listing can accommodate has a lower positive correlation with price (0.20).

**Inter-Feature Correlations**:

- Accommodates and Beds: There is a strong positive correlation between the number of people accommodated and the number of beds (0.72).
- Bedrooms and Beds: Bedrooms and beds also have a strong positive correlation (0.81).
- Accommodates and Bedrooms: These two features show a strong positive correlation (0.58).

**Weak or Negative Correlations**:

- Host Age: Host Age generally shows weak correlations with other features.
- Minimum and Maximum Nights: These show weak correlations with most features, including price.
- Top 10 Amenities Count: This has weak correlations with most features, indicating that the number of amenities does not strongly relate to the other numerical variables in the dataset.

### Feature Distributions

**1. Analysis by Location Coordinates("Lat/Long")**:

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/ac5eb0f6-347b-43d8-b539-5006cd6c1515)

**2. Analysis by Accommodates**:

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/1333291d-c16d-4548-a412-d178fccc1407)

**3. Analysis by Bedrooms**:

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/56df8f10-f2d0-4337-b582-813a5fffdf6a)

**4. Analysis by Amenities**:

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/87d0f6aa-00a2-4029-a68e-ecf7228669df)


## Feature Engineering

Several new features were created, and existing features were transformed to improve the model's predictive power. Key engineered features include host experience in months, distance from railway station, bus station, and various aggregated metrics from the calendar data.


## Modeling

### Train/Test/Validation Split

The data was split into training, validation, and test sets using a 70-15-15 split to ensure the model generalizes well to unseen data.

### Model Comparison

Several regression models were compared, including Multilinear Regression, Regression Trees, Random Forest Regressor, Gradient Boosting Machine (GBM), XGBoost, and LightGBM.

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/244b40de-af0c-4618-9ff8-d669285b5151)

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/6bcf6403-6cd7-467b-bad9-f098363599dd)

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/75c4f093-168c-4fca-b752-d7dfb70fa26a)

### Final Model

#### The Random Forest Regressor was selected as the final model based on its superior performance. The model's evaluation metrics are as follows:

- Best Model: Random Forest Regressor
- Test MAE: 1.4016939707545986
- Test MSE: 121.63470813256798
- Test R²: 0.9956058407503108

#### The model with the **lowest** **MAE** and **MSE**, and the **highest** **R²** is the best.


## Model Deployment

The final model has been deployed using jupyter notebook final model [**Airbnb_price_predictor_RF.ipynb**](Airbnb_price_predictor_RF.ipynb) file and Streamlit using final price prediction file [**airbnbprice.py**](airbnbprice.py). You can predict the price of a property by entering the top 10 predictors that directly influence the target variable (price).

#### Result using pyton in Jupyter Notebook

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/8e603924-d469-4a4d-ba0c-a967e480fe8a)

#### Result by running model using Streamlit

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/efaef50b-8414-4f85-a3cd-a65b5d4e3b61)


## Conclusion

The Random Forest Regressor was found to be the best model for predicting Airbnb listing prices. Key predictors includes: 

#### Top 5 most important predictors, we can use the feature importance attribute of the finalized model .
  - Feature: property_type_Private room in townhouse, Importance: 0.2748234452248065
  - Feature: property_type_Entire villa, Importance: 0.13951710988468868
  - Feature: accomodates, Importance: 0.06764998181524914
  - Feature: bathroom_number, Importance: 0.06618025546898562
  - Feature: distance_to_railway_station, Importance: 0.05432578039678924

#### Top 5 Most Important Predictors:
  - property_type_Private room in townhouse: High importance value, indicates it significantly influences the target variable.
  - property_type_Entire villa: High importance value, second most influential predictor.
  - accomodates: Moderate importance value, third most influential.
  - distance_to_railway_station: Lower importance value, fourth most influential.
  - latitude: Lowest importance value among the top 5, but still significant.


## Files in the Repository

- [**Airbnb Capstone Project.ipynb**](Airbnb%20Capstone%20Project.ipynb): Jupyter notebook containing the code and analysis.
- [**final_df.xls**](final_df.xls): Final dataset after preprocessing and feature engineering.
- [**airbnbprice.py**](airbnbprice.py): Script for deploying the model using Streamlit.
- [**random_forest_model.pkl**](random_forest_model.pkl): Trained Random Forest Regressor model.
- [**scaler.pkl**](scaler.pkl): Scaler used for feature scaling.
- [**Airbnb_price_predictor_RF.ipynb**](Airbnb_price_predictor_RF.ipynb): Jupyter notebook for Random Forest model analysis.
- [**Presentation.pptx**](Presentation.pptx): Presentation summarizing the project.


## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/shishir1991/AirBnb_Capstone_Project/blob/main/LICENSE) file for more details.


## Contact
For any further questions or contributions, please contact us:

#### Project Lead: Shishir Kherod
#### Email: shishirdma@gmail.com

Feel free to clone this repository and explore the code and data. If you have any questions or suggestions, please open an issue or contact me directly.










 
































