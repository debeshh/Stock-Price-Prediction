# 📈 Stock Price Prediction Web App

A simple machine learning web application that predicts stock closing prices based on historical data. Built using **Flask** for the backend and designed to be deployed using **Render**.

---

## 🚀 Features

- Predict stock close price using:
  - K-Nearest Neighbors Regressor
  - Multiple Linear Regression
  - Ridge Regression
- Supports user input for stock name (e.g., MSFT)
- Data preprocessing & polynomial feature expansion
- Model evaluation with R² and MSE
- Visual plots comparing actual vs predicted

---

## 🧠 Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas / Numpy
- Matplotlib
- Render (for deployment)

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/stock-predictor-app.git
   cd stock-predictor-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app locally**
   ```bash
   python app.py
   ```

   App will be live at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ☁️ Deployment on Render

### Step-by-Step:

1. Push your project to GitHub.
2. Go to [Render](https://render.com/).
3. Create a **New Web Service**.
4. Connect your GitHub repo.
5. Set the following:

   - **Build Command:**  
     ```bash
     pip install -r requirements.txt
     ```

   - **Start Command (recommended):**  
     ```bash
     gunicorn app:app
     ```

   - OR (alternative dev mode):  
     ```bash
     flask run --host=0.0.0.0 --port=10000
     ```

6. Add Environment Variables if needed:
   - `FLASK_APP=app.py`
   - `FLASK_ENV=development`

7. Deploy & Get the URL (e.g., `https://stock-predictor-api.onrender.com`)

---

## 📁 Project Structure

```
📦 stock-predictor-app
├── app.py
├── MSFT.csv
├── requirements.txt
├── README.md
└── templates/
    └── index.html (optional if frontend is added)
```

---

## 🧪 Sample Prediction Route

Add this to your `app.py` to test:

```python
@app.route('/')
def home():
    return "🚀 Stock Price Predictor API is Live!"
```

Then visit the deployed URL to check if it's working.

---

## 💡 Future Improvements

- Add frontend with React/Vite and deploy to Netlify
- Add more regression models
- Pull live stock data via APIs (e.g., Alpha Vantage, Yahoo Finance)

---

## 🧑‍💻 Author

Made with ❤️ by Debesh

---

## 📜 License

MIT License
