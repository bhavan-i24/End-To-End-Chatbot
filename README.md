# 💬 Streamlit Chatbot (TensorFlow-Free)

A lightweight, deployable chatbot built using Python, Streamlit, and Scikit-learn — no TensorFlow required! Designed to run on **Streamlit Cloud** and other modern Python 3.13-compatible environments.

---

## 🚀 Features

- Natural language response matching using TF-IDF + cosine similarity
- Fully deployable on [Streamlit Cloud](https://streamlit.io/cloud)
- Easy-to-edit intents via `intents.json`
- Fast, lightweight, and beginner-friendly

---

## 🗂️ Project Structure

end-to-end-chatbot/
├── app.py # Streamlit UI app
├── chatbot.py # Core chatbot logic (NLU)
├── intents.json # Predefined intents (tags, patterns, responses)
└── requirements.txt # Dependencies

## 🧠 How It Works

1. `chatbot.py` loads the `intents.json` file
2. It uses `TfidfVectorizer` to embed user queries and intent patterns
3. `cosine_similarity` finds the closest matching intent
4. A random response from the best-matching intent is returned

---

## 🛠️ Requirements

- Python 3.8–3.13
- `streamlit`
- `scikit-learn`

Install them with:

```bash
pip install -r requirements.txt


