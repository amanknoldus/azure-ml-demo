import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        # Initialize paths to model and preprocessor
        self.model_path = os.path.join("artifacts", "model.pkl")
        self.preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

    def predict(self, features):
        try:
            # Load model and preprocessor
            model = load_object(file_path=self.model_path)
            preprocessor = load_object(file_path=self.preprocessor_path)

            # Preprocess input features
            data_scaled = preprocessor.transform(features)

            # Make predictions
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, gender: str, race_ethnicity: str, parental_level_of_education: str,
                 lunch: str, test_preparation_course: str, reading_score: float, writing_score: float):
        # Initialize input data
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            # Convert input data to a DataFrame
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
