from pydantic import BaseModel
import pandas as pd
import mlflow.pyfunc

# Création du modèle de données pour le modéle
Dataset = pd.read_csv('dataset/Sleep_health_and_lifestyle_dataset.csv')


# Création du modèle de données pour le modéle 1 ('Gender', 'Age', 'Physical Activity Level', 'Heart Rate', 'Daily Steps', 'BloodPressure_high', 'BloodPressure_low', 'Sleep Disorder'])
class Credit(BaseModel):

    Gender: int
    Age: int
    PhysicalActivityLevel: int
    HeartRate: int
    DailySteps: int
    BloodPressure_high: int
    BloodPressure_low: int
    SleepDisorder: int


# Création du modèle de données pour le modéle 2 ('Physical Activity Level', 'Heart Rate', 'Daily Steps', 'Sleep Disorder')

class Credit2(BaseModel):
    PhysicalActivityLevel: int
    HeartRate: int
    DailySteps: int
    SleepDisorder: int


# class Model1(mlflow.pyfunc.PythonModel):
#     def __init__(self):
#         self.model = None
#
#     def load_context(self, context):
#         self.model = context.artifacts['model_1']
#
#     def predict(self, context, model_input):
#         data = pd.DataFrame(model_input, index=[0])
#         return self.model.predict(data)
#
#
# model1 = Model1()
#
# mlflow.pyfunc('model_1', 'v1', 'predict')
#
#
#
# class Model2(mlflow.pyfunc.PythonModel):
#     def __init__(self):
#         self.model = None
#
#     def load_context(self, context):
#         self.model = context.artifacts['model_2']
#
#     def predict(self, context, model_input):
#         data = pd.DataFrame(model_input, index=[0])
#         return self.model.predict(data)
#
#
# model2 = Model2()
#
# mlflow.pyfunc('model_2', 'v1', 'predict')