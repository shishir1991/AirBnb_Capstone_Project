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

![image](https://github.com/shishir1991/AirBnb_Capstone_Project/assets/157515610/8a357456-0b58-4f99-ba43-f13073a18e7a)

**Analysis by Latitude**:

- Most of the properties are located between 51.207870 and 51.220905 latitude.

- Prices of the properties are high between the latitudes 51.200 and 51.250.





























