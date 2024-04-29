### Medical Recommendation System using Flutter(dart), FastAPI(Python), PostgreSQL and Machine Learning and Artificial Intelligence Algorithms.

### Description:
Welcome to our Medical Recommendation System, our platform swiftly analyzes your symptoms to accurately predict potential diseases. From there, it offers tailored dietary suggestions and precautionary measures to help you manage your health proactively. Stay informed, stay healthy with our intuitive and efficient system.

### Features:
User-Friendly Interface: Experience simplicity at its best with our interface designed to effortlessly capture your symptoms, ensuring a smooth journey through your health assessment.

Advanced ML and AI Models: Powered by the latest advancements in machine learning, our system meticulously analyzes your symptoms, delivering precise disease predictions with unparalleled accuracy.

Personalized Guidance: Receive personalized recommendations for the top 5 medicines, outlining prescription details, and even workout routines based on the predicted disease.

FastAPI Integration: With our FastAPI web application seamlessly integrating all components, making it easily accessible to users. Whether you're at home or on the go, support is just a click away.

Privacy and Security: Your privacy and security are our top priorities. Rest assured, your health information is treated with the utmost confidentiality and protected with robust security measures, adhering strictly to industry standards.

Continuous Enhancement: We are committed to continuous improvement. As our system gathers more data and insights, our machine learning models evolve, ensuring that our recommendations remain at the forefront of accuracy and relevance.

## Introduction
Welcome to my project! This ReadME will guide you through the setup and usage of this application. 

## Goals:
- Develop a user-friendly interface for effortless symptom input.
- Employ advanced AI algorithms to analyze symptoms and predict potential diseases accurately.
- Provide personalized recommendations for the top 5 medicines, prescription details, and even workout routines based on the predicted disease(In future release).
- Provide tailored dietary suggestions to support proactive health management(In future release).
- Offer precautionary measures aligned with predicted diseases to empower users in maintaining their well-being.
- Recommend suitable healthcare providers based on predicted conditions.
- Integrate with healthcare provider databases to retrieve detailed information on doctors' specialties and  availability.
- Implement a rating system to gather user feedback on recommended doctors, enhancing the system's accuracy and - trustworthiness.

## Technologies Used:
Frontend: Flutter(dart)
Backend: FastAPI(Python)
Database: PostgreSQL
Machine Learning Models: Using Pandas and Scikit-learn.

## Installation
Follow these steps to set up and run the project in your local environment:

## Prerequisites
- Android Studio installed on your machine.
- Flutter SDK installed on your machine.
- VS Code installed on your machine.
- Python 3.12.2 installed on your machine.
- Git installed on your machine.
- PostgreSQL installed on your machine.

## 1. Clone the Repository
First, clone the repository to your local machine:
    ```bash
    git clone https://github.com/sangeetanandanvishal04/AI-medical-assistant.git

### 2. Create and Activate a Virtual Environment
Open Command prompt inside your VS Code editor:
Create the virtual environment: python3 -m venv venv
Activate the virtual environment: 
    ---For Windows: venv\Scripts\activate
    ---For macOS and Linux:source venv/bin/activate

### 3.Install Dependencies
Once the virtual environment is activated, install the required Python dependencies from 
the requirements.txt file:  pip install -r requirements.txt

### 4. Set Up the PostgreSQL Database
Create a PostgreSQL database for the project and then create ".env" file and update these 
required values to connect with the PostgreSQL database.

    DATABASE_HOSTNAME = localhost,
    DATABASE_PORT = 5432,
    DATABASE_PASSWORD = "YOUR_DATABASE_PASSWORD",
    DATABASE_NAME = "YOUR_DATABASE_NAME",
    DATABASE_USERNAME = "YOUR_DATABASE_USERNAME",
    SECRET_KEY = 09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
    ALGORITHM = HS256
    ACCESS_TOKEN_EXPIRE_MINUTES = 300

### 5. Set Up values of SMTP Email and Password:
    EMAIL = "YOUR_EMAIL"
    SMTP_PASSWORD = "YOUR_SMTP_PASSWORD"

    Steps to get SMTP Password:
    --- Open Google Chrome: Launch the Chrome browser on your computer or device.
    --- Go to your Google Account settings: Click on your profile picture or initials in the top right 
        corner of the Chrome window. From the dropdown menu, select "Manage your Google Account."
    --- Navigate to "Security" settings: In your Google Account settings, find and click on the 
        "Security" tab on the left-hand side menu. This is where you manage security-related settings for 
        your Google Account.
    --- Find the section for "Signing in to other sites" or "Third-party app access": Look for a section 
        related to signing in to other sites or granting access to third-party applications. This is 
        where you'll manage access to your Gmail account for your Python script.
    --- Generate an app password if necessary: If you have two-step verification enabled for your Google 
        Account, you may need to generate an app password specifically for your Python script. Look for 
        an option to generate an app password and follow the instructions to create one. Make sure to 
        copy this password as you'll need it in your Python script.
    --- Now, Update SMTP_PASSWORD in ".env" file.

### 6. Run the Application:
    First, Run the FastAPI Server using command prompt in VS Code: uvicorn Server.main:app --reload
    After successfull run of FastAPI Server, run front-end of the Application in future release."# AI-medical-assistant" 
"# AI-medical-assistant" 
