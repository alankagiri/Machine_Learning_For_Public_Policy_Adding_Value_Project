# Machine Learning For Public Policy: Adding Value Project
Authors: Mburu Kagiri, Alice Lyu, Chris Strehl, Ashna Patel

# Objective
This project seeks to answer 2 main questions:
1. Are geographical features such as neighborhood, ward, or city predictive for certain types of 311 Requests?
2. How accurately can snow removal requests be anticipated to facilitate early and proactive administrative responses?

The goal is to identify a real world policy task of allocating public service provisions within the City of Pittsburgh, conducts EDA with a purpose for ML clustering on the City of Pittsburgh's 311 Data, and reports experiences, observations, and recommendations. The project contains both a time series forecast and clustering analysis. The aim of the time series forecast is to support planning for spikes in complaints like snow/ice removal. The aim of the clustering analysis is to identify and monitor areas with chronic or high-volume service needs.

# 311_Data_EDA File
This file cleans the 311 data, conducts feature discovery, variance thresholding, and principal component analysis for clustering, and performs k-means clustering on the data.

# Constants File
The constants.py file is linked to the 311_Data_EDA.ipynb file, and hosts either the redundant features contained in the original 311 Data file for reference, or categorical values numerically encoded for classification purposes. For instance, each request made is associated with a 311-specific code; having both features results in multicollinearity and yields no additional information for modeling purposes. Therefore this file contains the mapped values for such redundant features for references and data integrity. 

The values contained within this file are not manually imputed, but are instead dynamically populated based on functions in the 311_Data_EDA file. This dynamic approach allows for a more effective method of data deduplication in case changes to such decisions are made in the future.

# Forecast.ipynb
This file uses daily snowfall data to perform time series forecasting for snow removal service requests. It prepares the snow rate data, applies seasonal decomposition, fits time series models, and generates forecasts to support proactive administrative planning. The forecasting analysis helps anticipate spikes in snow/ice-related 311 complaints based on historical snowfall patterns.

# Requirements to Run Project Files
Please refer to the requirements.txt for installing the necessary Python libraries.
