import streamlit as st
import joblib
import pandas as pd

# Define paths to model and scaler files
model_path = r"F:\Hero Vired - Data Science and Business Analytics Course\Capstone Project\Problem Statements-20240601\Airbnb\AirBnB Project\ML-MODEL-DEPLOYMENT-USING-FLASK\random_forest_model.pkl"
scaler_path = r"F:\Hero Vired - Data Science and Business Analytics Course\Capstone Project\Problem Statements-20240601\Airbnb\AirBnB Project\ML-MODEL-DEPLOYMENT-USING-FLASK\scaler.pkl"

# Load model and scaler
try:
    rf_model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
except Exception as e:
    st.error(f"Error loading model or scaler: {e}")

# Define feature names used in the model
feature_names = [
    'longitude', 'latitude', 'accomodates', 'bedrooms', 'beds', 'bathroom_number', 
    'top_10_amenities_count', 'minimum_nights', 'maximum_nights', 'property_type_Casa particular', 
    'property_type_Castle', 'property_type_Entire condominium (condo)', 'property_type_Entire cottage', 
    'property_type_Entire guest suite', 'property_type_Entire guesthouse', 'property_type_Entire loft', 
    'property_type_Entire rental unit', 'property_type_Entire residential home', 
    'property_type_Entire serviced apartment', 'property_type_Entire townhouse', 
    'property_type_Entire vacation home', 'property_type_Entire villa', 'property_type_Houseboat', 
    'property_type_Private room', 'property_type_Private room in bed and breakfast', 
    'property_type_Private room in boat', 'property_type_Private room in casa particular', 
    'property_type_Private room in condominium (condo)', 'property_type_Private room in guest suite', 
    'property_type_Private room in guesthouse', 'property_type_Private room in loft', 
    'property_type_Private room in religious building', 'property_type_Private room in rental unit', 
    'property_type_Private room in residential home', 'property_type_Private room in serviced apartment', 
    'property_type_Private room in townhouse', 'property_type_Private room in villa', 'property_type_Room in aparthotel', 
    'property_type_Room in boutique hotel', 'property_type_Room in hotel', 'property_type_Shared room in bed and breakfast', 
    'property_type_Shared room in casa particular', 'property_type_Shared room in loft', 
    'property_type_Shared room in residential home', 'property_type_Tent', 'property_type_Tiny house', 
    'property_type_Yurt', 'room_type_Entire home/apt', 'room_type_Hotel room', 'room_type_Private room', 
    'room_type_Shared room'
]

def preprocess_user_input(user_data):
    # Convert user data to DataFrame
    user_df = pd.DataFrame([user_data])
    
    # Handle categorical variables
    categorical_columns = ['property_type', 'room_type']
    user_df_encoded = pd.get_dummies(user_df, columns=categorical_columns, drop_first=False)
    
    # Ensure all expected columns are present
    for col in feature_names:
        if col not in user_df_encoded.columns:
            user_df_encoded[col] = 0
    
    # Reorder columns to match model's expectations
    user_df_encoded = user_df_encoded[feature_names]
    
    # Scale the user input data
    user_df_scaled = scaler.transform(user_df_encoded)
    
    return user_df_scaled

def predict_price(user_data):
    user_df_scaled = preprocess_user_input(user_data)
    price_prediction = rf_model.predict(user_df_scaled)
    return price_prediction[0]

def main():
    st.title('House Price Prediction App')
    st.write('Enter the details of the property to get a price prediction.')

    # User input fields
    latitude = st.number_input('Latitude')
    longitude = st.number_input('Longitude')
    property_type = st.selectbox('Property Type', [
        'Casa particular', 'Castle', 'Entire condominium (condo)', 'Entire cottage', 
        'Entire guest suite', 'Entire guesthouse', 'Entire loft', 'Entire rental unit', 
        'Entire residential home', 'Entire serviced apartment', 'Entire townhouse', 
        'Entire vacation home', 'Entire villa', 'Houseboat', 'Private room', 
        'Private room in bed and breakfast', 'Private room in boat', 
        'Private room in casa particular', 'Private room in condominium (condo)', 
        'Private room in guest suite', 'Private room in guesthouse', 'Private room in loft', 
        'Private room in religious building', 'Private room in rental unit', 
        'Private room in residential home', 'Private room in serviced apartment', 
        'Private room in townhouse', 'Private room in villa', 'Room in aparthotel', 
        'Room in boutique hotel', 'Room in hotel', 'Shared room in bed and breakfast', 
        'Shared room in casa particular', 'Shared room in loft', 'Shared room in residential home', 
        'Tent', 'Tiny house', 'Yurt'
    ])
    room_type = st.selectbox('Room Type', ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'])
    accommodates = st.number_input('Number of Accommodates', min_value=1)
    bedrooms = st.number_input('Number of Bedrooms', min_value=0.0, step=0.5)
    beds = st.number_input('Number of Beds', min_value=1.0, step=0.5)
    bathroom_number = st.number_input('Number of Bathrooms', min_value=1.0, step=0.5)
    top_10_amenities_count = st.number_input('Count of Top 10 Amenities', min_value=0)
    minimum_nights = st.number_input('Minimum Nights', min_value=1)
    maximum_nights = st.number_input('Maximum Nights', min_value=1)

    user_data = {
        'latitude': latitude,
        'longitude': longitude,
        'property_type': property_type,
        'room_type': room_type,
        'accommodates': accommodates,
        'bedrooms': bedrooms,
        'beds': beds,
        'bathroom_number': bathroom_number,
        'top_10_amenities_count': top_10_amenities_count,
        'minimum_nights': minimum_nights,
        'maximum_nights': maximum_nights
    }

    if st.button('Predict Price'):
        predicted_price = predict_price(user_data)
        st.success(f'Predicted price: ${predicted_price:.2f}')

if __name__ == '__main__':
    main()
