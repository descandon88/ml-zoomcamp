import pickle

# 1. Cargar el modelo
with open("pipeline_v1.bin", "rb") as f_in:
    model = pickle.load(f_in)

record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

X = [record]

# 4. Obtener la predicción
prediction = model.predict_proba(X)[0, 1]

print("Prediction:", prediction)
