# FastAPI Iris ML Model API 🚀🌸

A simple FastAPI app that serves a trained Machine Learning model (Random Forest) to predict the species of an Iris flower based on its features.

---

## 📂 Project Structure

simple-ML/
├── main.py # FastAPI app
├── train_model.py # Script to train & save the model
├── iris_model.joblib # Saved ML model
├── venv/ # Virtual environment (not tracked by Git)
├── .gitignore
├── requirements.txt
└── README.md


---

## ✅ Features

- 🧠 **Scikit-learn** Random Forest model trained on the classic Iris dataset
- ⚡ **FastAPI** backend serving predictions through a `/predict` POST endpoint
- ✅ Input validation with **Pydantic**
- 🔒 Ready for containerization & deployment

---

## 🚀 How to run it

### 1️⃣ Clone the repo

```bash
git clone https://github.com/EshanDhanjal/FastAPI-ML
cd FastAPI-ML

2️⃣ Create & activate a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Train the model (optional)

python train_model.py

5️⃣ Run the FastAPI app

uvicorn main:app --reload

Visit http://127.0.0.1:8000/docs to use the interactive Swagger UI.
🔎 Example API request

POST /predict

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

Response:

{
  "predicted_species": "setosa"
}

📦 Dependencies

    FastAPI

    Uvicorn

    Pandas

    Scikit-learn

📄 License

This project is open-source and free to use.
✨ Author

Eshan — feel free to connect on GitHub.