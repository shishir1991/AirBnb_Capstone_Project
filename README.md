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






















 
































