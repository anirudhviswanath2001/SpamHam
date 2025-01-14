# Spam Classification - Streamlit Application

## Overview
This project is a **Streamlit-based web application** for classifying emails as either **Spam** or **Ham**. It uses a pre-trained machine learning model and TF-IDF vectorization to process and classify user-input messages.

---

## Features
- **Input Field**: Users can input a message they wish to classify.
- **Real-Time Prediction**: The app processes the message and provides instant feedback.
- **Spam/Ham Classification**: Displays whether the message is spam or not.

---

## Requirements
To run this application, ensure you have the following dependencies installed:

```plaintext
streamlit
scikit-learn
nltk
pickle
```

---

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/spam-classification.git
    cd spam-classification
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Download NLTK data (if not already installed):
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

4. Ensure the `vectorizer.pkl` and `model.pkl` files are present in the project directory.

---

## Usage
Run the application locally with the following command:

```bash
streamlit run app.py
```

1. Open the Streamlit application in your browser (default: http://localhost:8501).
2. Enter a message in the input field.
3. Click the **Predict** button to see the classification result.

---

## File Structure
```plaintext
spam-classification/
├── app.py              # Main Streamlit application
├── vectorizer.pkl      # TF-IDF vectorizer model
├── model.pkl           # Trained ML model
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## How It Works
1. **Text Preprocessing**:
   - Converts input text to lowercase.
   - Tokenizes text into words.
   - Removes non-alphanumeric characters, stopwords, and punctuation.
   - Applies stemming using the Porter Stemmer.

2. **Vectorization**:
   - Transforms the preprocessed text into numerical format using a pre-trained TF-IDF vectorizer.

3. **Prediction**:
   - Feeds the vectorized text into the trained machine learning model.
   - Outputs the classification result as **Spam** or **Ham**.

---

## Example
**Input**:
```
Congratulations! You've won a free ticket to Bahamas. Claim now!
```
**Output**:
```
Spam
```

---

## Contributions
Feel free to submit pull requests or open issues to enhance this project. Contributions are welcome!

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
