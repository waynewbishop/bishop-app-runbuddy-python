# Run Buddy: AI-Powered Running Outfit Recommender

Run Buddy is an innovative iOS application that leverages machine learning to provide personalized running outfit recommendations based on current weather conditions. This repository contains the backend implementation of the Run Buddy system.

## Project Overview

The core of Run Buddy is a machine learning model (RandomForestClassifier) that predicts appropriate running attire categories (very light, light, medium, heavy) based on temperature, humidity, and wind speed. The system is designed to enhance runners' experiences by suggesting suitable clothing while integrating brand partnerships for monetization.

Key Features:
- Weather-based outfit prediction using machine learning
- JSON-based data management for model, brands, user preferences, and clothing interpretations
- Flask API for seamless integration with the iOS frontend
- Continuous model improvement through user feedback
- Brand rotation system for fair representation of partner brands

The backend is built with Python, utilizing libraries such as scikit-learn for machine learning, Flask for API development, and joblib for model serialization. The system architecture includes a modular design with separate components for model management, data collection, API handling, and testing.

This project aims to demonstrate the practical application of machine learning in everyday scenarios, providing value to runners while exploring opportunities for brand integration and personalized recommendations.

Future enhancements may include more sophisticated data collection methods, advanced feature engineering, and integration with popular fitness tracking platforms for improved personalization.

Contributors are welcome to help improve the model accuracy, expand the feature set, or enhance the API functionality.