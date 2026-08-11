from fastapi import FastAPI
import joblib

# write api

class input(Basemodel):
    site_id = field(example="site_001")


def predict(input=input):
    if site_id = "site_001":
        model = 'site_001_model_path'

        