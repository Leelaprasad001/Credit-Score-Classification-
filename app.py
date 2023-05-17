import streamlit as st
import numpy as np
import pickle

# Load the saved model from file
def load_model():
    with open('final_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

def predict_credit_score(features):
    return model.predict(features)

def main():
    st.title("Credit Score Prediction")
    st.subheader("Enter the required information below:")
    a = st.text_input("Annual Income:")
    b = st.text_input("Monthly Inhand Salary:")
    c = st.text_input("Number of Bank Accounts:")
    d = st.text_input("Number of Credit Cards:")
    e = st.text_input("Interest Rate:")
    f = st.text_input("Number of Loans:")
    g = st.text_input("Average number of days delayed by the person:")
    h = st.text_input("Number of delayed payments:")
    i = st.selectbox("Credit Mix (Bad: 0, Standard: 1, Good: 3):", ['0', '1', '3'])
    j = st.text_input("Outstanding Debt:")
    k = st.text_input("Credit History Age:")
    l = st.text_input("Monthly Balance:")


    if st.button("Predict", key='predict_button'):
        if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "" or i == "" or j == "" or k == "" or l == "":
            st.warning("Please provide values for all the fields.")
        else:
            features = np.array([[float(a), float(b), float(c), float(d), float(e), float(f), float(g), float(h), float(i), float(j), float(k), float(l)]])
            predicted_score = predict_credit_score(features)
            st.success("Predicted Credit Score: {}".format(predicted_score[0]))

if __name__ == "__main__":
    main()