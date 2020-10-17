# FeCare
With an intention of **Fekar** (care in Hindi) towards the health of Indian women. 
[Web App link](https://fecare.herokuapp.com/)

Researchers have identified a bunch of districts in India that have a maximum prevalence of diabetes among women. At least 50 of the 640 districts studied have a high prevalence of diabetes — greater than one in every 10 among women.
And hence, FeCare classifier model aims to detect diabetes in Indian women. The clasifier was trained using [Pima Indians Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database)

# Dataset info:
The dataset consists of several medical predictor variables and one target variable, Outcome. Predictor variables include:
- Number of times pregnant
- Plasma glucose concentration, 2 hours in an oral glucose tolerance test (not included in training)
- Diastolic blood pressure (mm Hg)
- Triceps skinfold thickness (mm)
- 2-Hour serum insulin (mu U/ml) (not included in training)
- Body mass index
- Diabetes pedigree function
- Age (years)

As you can notice that two variables were not included in the training process, this was due to the reason that the Glucose Tolerance Test (GTG) can not give very inaccurate results when conducted at home using a blood sugar measuring device. And same is the case for finding the reading of 2-Hour serum Insulin.

As this project aims to provide regular Diabetes check-up for all women(above the age of 20 years) irrespective of their work engagement(house-wives and working women), it is not possible in all cases that user will have the required tools, skills, and experience to execute the required test at home. And hence the above features were eliminated from the training process.

# Requirements:
- The user should know her general information(Age, Height, Weight, and Pregnancies)
- To know the reading of Diastolic Blood Pressure, the user should have a Blood Pressure monitor [like this](https://www.webmd.com/hypertension-high-blood-pressure/guide/hypertension-home-monitoring#1) which costs less than 100$
<img src= "Graphics/BP-monitor.JPG" width="250" height="150">

- To know the Tricep Skinfold Thickness value, the user should have a Skinfold Caliper and take the reading in the following manner:
<img src= "Graphics/SFT.jpg" width="500" height="300">

The cost of Skinfold Caliper is less than 4$

<img src= "Graphics/Skinfold-Caliper.JPG" width="150" height="150">

- If the user do not know her Diabetes Pedigree Function, then it can be calculated on the web application using the following:

<img src= "Graphics/DiabetesPedigreeFunction-1.JPG" width="500" height="650">
<img src= "Graphics/DiabetesPedigreeFunction-Constant-Info.JPG" width="400" height="350">

[Reference](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2245318/pdf/procascamc00018-0276.pdf) 

The user can input relative’s details(as much she knows) in the web-application, and Diabetes Pedigree Function will be calculated.

Note that the value of the DPF increases as the number of relatives who developed DM increases, as the age at which those relaves developed DM decreases, and as the percentage of genes that they share with the subject increases. Also notice that the value of the DPF decreases as the number of relatves who never developed DM increases, as their ages at their last examinain increase, and as the percent of genes that they share with the subject increases.

# Steps for pre-processing data and training classifier:
- The data has a very less number of 1s in Output(cases with positive diabetes), and hence this can affect the classifier’s accuracy to differentiate with 1s and 0s.

Due to this reason, an equal amount of data for 1s and0s were taken in the training set(for which the data was divided into two parts on the same basis and then segregated for training data)

- Now the two data frames(with 1s and 0s) were concatenated so that they can be accessed easily



# Unknown
![Demo-DPF-Unknown](https://user-images.githubusercontent.com/50732558/96336365-d9cd8700-109c-11eb-8fec-d639258abddc.gif)

# Known
![Demo-DPF-Known](https://user-images.githubusercontent.com/50732558/96336398-1ac59b80-109d-11eb-88c3-3bccfadbd808.gif)

