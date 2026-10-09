INSTITUTE OF ENGINEERING & TECHNOLOGY, DAVV
B.Tech IV Year E&TC  – Session 2026-27
Project Report Proforma-I

Class: BE IV Year E&TC 	      	 Section: B   		          Group No.: 11
1. Title of the Project:
Medical Insurance Cost Prediction Using Machine Learning
2. Domain (Hardware / Software):
☐ Hardware       [*] Software
3. Objectives (at least 4):
1. To develop a machine-learning-based system for predicting the approximate medical insurance cost of an individual.
2. To identify important features that have a significant relationship with the predicted insurance cost.
3. To transform categorical information into a machine-learning-compatible format using suitable encoding techniques.
4. To train multiple regression models and compare their performance for the insurance-cost prediction task.
5. To evaluate the trained models using appropriate regression evaluation metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² score.
6. To create a prediction system where relevant user information can be provided as input and the estimated medical insurance cost can be obtained as output.
4. Abstract :
Medical insurance plays an important role in managing the financial burden associated with healthcare and medical treatment. The cost of medical insurance can vary significantly among individuals depending on several demographic, lifestyle, and health-related factors. Estimating insurance costs accurately can therefore be useful for financial planning, risk analysis, and insurance-related decision-support applications. This project, titled “Medical Insurance Cost Prediction Using Machine Learning,” aims to develop a machine-learning-based system capable of predicting the approximate medical insurance cost of an individual using historical data.
The project uses a medical insurance cost dataset obtained from Kaggle containing information related to individuals and their corresponding insurance costs. The data is first analyzed using exploratory data analysis techniques to understand the distribution of variables, identify relationships between features, and observe patterns associated with insurance expenses. Data preprocessing techniques are then applied to prepare the dataset for machine-learning algorithms. This may include handling missing or duplicate records, encoding categorical variables, and appropriately preparing numerical features.
Since insurance cost is a continuous numerical variable, the problem is formulated as a supervised regression problem. Multiple regression algorithms can be trained and evaluated to determine their ability to estimate insurance costs. Appropriate evaluation metrics such as MAE, MSE, RMSE, and R² score can be used for objective model comparison.
The final system is intended to accept relevant individual information as input and generate an estimated insurance cost. The project demonstrates how machine learning and predictive analytics can be applied to structured healthcare-related data to support cost estimation and decision-making.
5. Problem Statement :
Medical expenses and insurance costs can differ considerably from one individual to another. Two individuals with similar demographic characteristics may have significantly different medical expenses because of differences in lifestyle, health conditions, medical history, and other relevant factors. For individuals, estimating potential insurance expenses in advance can be difficult because the relationship between these factors and the final medical cost is not always straightforward.
Traditional approaches to estimating insurance costs may depend heavily on predefined rules, historical averages, actuarial calculations, or manual analysis. Although such approaches can be useful, they may not easily capture complex relationships between multiple variables present in a large dataset. With the availability of historical insurance and healthcare-related data, machine learning provides an alternative approach in which computational models can learn relationships between input characteristics and previously observed insurance costs.
The main problem addressed by this project is the development of a machine-learning-based predictive system that can estimate medical insurance costs using relevant individual-level attributes. The project uses the Medical Insurance Cost Prediction dataset available through Kaggle. The dataset provides structured information that can be analyzed to identify relationships between individual characteristics and insurance expenses.
The first challenge is to understand the characteristics and quality of the available data. Real-world datasets may contain categorical variables, numerical variables, duplicate records, missing values, unusual observations, and variables with different scales. Therefore, simply applying a machine-learning algorithm directly to the raw dataset may not produce reliable results. Appropriate exploratory data analysis and preprocessing are required before model development.
The project then formulates insurance-cost prediction as a supervised regression problem, because the expected output is a continuous numerical value rather than a category. Different regression algorithms can be trained using the processed dataset. Their predictions need to be evaluated using suitable statistical performance measures rather than simply examining whether the model can fit the training data.
Model evaluation is particularly important because a model that performs well on training data may not necessarily generalize well to previously unseen individuals. Therefore, the dataset should be appropriately divided into training and testing data, and suitable evaluation metrics such as MAE, MSE, RMSE, and R² can be used to measure prediction performance. Model comparison can then help identify an appropriate approach for the final prediction system.
Thus, the overall problem is to design and evaluate a machine-learning pipeline that can transform historical medical insurance data into a reliable cost-prediction model through data analysis, preprocessing, feature preparation, regression modeling, evaluation, and prediction. Existing Kaggle implementations of this dataset similarly demonstrate workflows involving exploratory analysis, preprocessing, regression models, model comparison, and final evaluation.

6. Expected Outcomes (at least 4):
1. Clean and Processed Dataset
A properly analyzed and preprocessed version of the medical insurance dataset will be prepared for machine-learning development.
2. Exploratory Data Analysis
The project will provide visual and statistical analysis showing patterns and relationships between available input variables and medical insurance costs.
Examples may include:
    • Distribution of insurance costs
    • Relationship between age and insurance cost
    • Comparison of insurance costs across categorical groups
    • Correlation analysis between numerical variables


3. Feature Analysis
The project is expected to identify the variables that have stronger relationships with the insurance-cost target variable.
4. Regression Models
One or more suitable machine-learning regression algorithms will be trained to predict insurance costs.

