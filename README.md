# ai-real-estate-valuator
tAI-Powered Real Estate Investment Tool: A multi-modal machine learning application that predicts property values using a combination of structured data (Random Forest) and visual analysis (Computer Vision) via FastAPI and Streamlit.
🏠 AI Smart Property Valuator
This project demonstrates a Multi-modal Machine Learning approach to real estate valuation. Unlike traditional calculators that only look at numbers, this tool uses Computer Vision to "see" the condition of a property and adjust the market estimate accordingly.

🚀 Key Features
Multi-modal Fusion: Combines structured tabular data (Sqft, Bedrooms) with unstructured image data.  

Computer Vision Pipeline: Leverages MobileNetV2 (Deep Learning) to analyze interior photos for "Modern" vs "Standard" renovations.  

ML Regression: Uses a Random Forest Regressor to provide a baseline market valuation.  

Production-Ready API: Built with FastAPI for high-performance, asynchronous request handling.  

Interactive Dashboard: A clean, user-friendly interface built with Streamlit.
🛠️ Tech StackLanguage: PythonAI/ML: TensorFlow, Scikit-Learn, Joblib  Backend: FastAPI, Uvicorn  Frontend: Streamlit  Data Handling: NumPy, Pandas, IO  

#installation and usage

Install dependencies: pip install -r requirements.txt

Train the model: python model_train.py (Generates the property_model.pkl file).  

Start the Backend: uvicorn main:app --reload.  

Launch the Frontend: streamlit run app.py.
