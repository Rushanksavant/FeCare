import streamlit as st
import joblib
import torch
import torch.nn as nn
from model_architecture import Network

model = joblib.load('FeCare.pkl')

html_temp = """
    <div style="background-color:skyblue;padding:10px">
    <h1 style="color:white;text-align:center;">FeCare Diabetes Prediction model </h1>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
st.write('''
    # Procedure to use this App:

    ### Input the following.

    * Diastolic blood pressure (in millimeters of mercury). Use your blood pressure monitor to get accurate values.
    * Tricep Skinfold Thickness (in millimeters), using your Skinfold Caliper. If you do not know how to use Caliper, click on "Know" button below.
    * Input rest of the general details as asked and DON'T forget to press ENTER after every input
    * Then proceed to input/calculating your Diabetes Pedigree Function (read the instructions in that section)
''')
if st.button('Know'):
    st.image("SFT.jpg")
    st.write('''
        #### Ideal Tricep Skinfold Thickness is around 20.0 mm
    ''')


bp= st.number_input(label='Enter your Blood Pressure Reading(mm Hg)') #Input to model

sft= st.number_input(label='Enter your Triceps Skinfold Thickness (mm)') #Input to model

preg= st.number_input(label='How many number of times you have been pregnent?') #Input to model

age= st.number_input(label='What is your Age(in years)?') #Input to model

height= st.number_input(label='What is your Height(in centimeter)?')

weight= st.number_input(label='What is your Weight(in Kg)?')

BMI= 0 #Input to model
if height>0:
    BMI= weight/((height/100)**2)


# To calculate diabetes pedigree function
html_temp = """
    <div style="background-color:skyblue;padding:3px">
    <h2 style="color:white;text-align:ledt;">Your Diabetes Pedigree Function </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)


st.write('''
    * Diabetes Pedigree Function is a function which scores likelihood of diabetes based on family history.
    * If you already know your Diabetes Pedigree Function input it in the following field
    * If not, leave it blank and jump to "Calculating Your Diabetes Pedigree Function" and DON'T forget to click on 'Submit Info'
    * Diabetes Pedigree Function is given as:
''')

st.write('''
    $$
    (sum Ki(88 - ADMi) + 20) / (sum Kj(ALCj - 14) + 50)
    $$
    ''')
st.write('''
    #### In the abve equation:
    *   K values are kept fix for the type of relative(Parent, Full Sibling etc..)
    *   ADMi is the age in years of relatve, when diabetes was diagnosed
    *   ACL, is the age in years of relativej at the last non-diabetic examination (prior to the subject's examination date);
''')


dpf= st.number_input(label='Enter your Diabetes Pedigree Function') #Input to model
DPF= 0 #Input to model
if dpf != 0:
    DPF= dpf

else:
    html_temp = """
        <div style="background-color:skyblue;padding:3px">
        <h3 style="color:white;text-align:ledt;">Calculating Your Diabetes Pedigree Function: </h3>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True)

# For relatives having diabetes
    st.write('''
        ## Info of relatives having Diabetes
    ''')


    i= st.number_input(label='Number of genetically close relatives who have developed diabetes till the date')

    K_collect_yes=[] # Will contain type of relative 
    K_collect_age_yes=[] # Wil contain ages of all relatives

    for k in range(0, int(i)):
        l= st.selectbox(label=f'Enter Relative{k+1} Type', options=[f'{k+1}Parent', f'{k+1}Full Sibling', f'{k+1}Half Sibling', f'{k+1}Grandparent', f'{k+1}Aunt', f'{k+1}Uncle', f'{k+1}Half Aunt', f'{k+1}Half Uncle', f'{k+1}First Cousin'])
        a= st.number_input(label= f'Enter Age(in years) for Relative{k+1}')

        K_collect_yes.append(l)
        K_collect_age_yes.append(a)


    YES_diabetes=[] # Will contain list of Kx constants for all Diabetic Relatives

    Done_yes= K_collect_yes
    Kx= [0.5, 0.25, 0.125] # Kx=[Parent/Full Sibling, half sibling, grandparent, aunt or uncle, half aunt, half uncle or first cousin]
    
    for j in range(len(Done_yes)):

        if (Done_yes[j]== f'{j+1}Parent'):
            K= Kx[0]

        elif (Done_yes[j]== f'{j+1}Full Sibling'):
            K= Kx[0]

        elif (Done_yes[j]== f'{j+1}Aunt'):
            K= Kx[1]

        elif (Done_yes[j]== f'{j+1}Uncle'):
            K= Kx[1]

        elif (Done_yes[j]== f'{j+1}Half Sibling'):
            K= Kx[1]

        elif (Done_yes[j]== f'{j+1}Grandparent'):
            K= Kx[1]

        elif (Done_yes[j]== f'{j+1}Half Aunt'):
            K= Kx[2]

        elif (Done_yes[j]== f'{j+1}Half Uncle'):
            K= Kx[2]

        elif (Done_yes[j]== f'{j+1}First Cousin'):
            K= Kx[2]


        YES_diabetes.append(K)





    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

    #For relatives NOT having diabetes
    st.write('''
        ## Info of relatives NOT having Diabetes
    ''')
    j= st.number_input(label='Number of genetically close relatives who have NOT developed diabetes till the date')

    K_collect_no=[] # Will contain type of relative
    K_collect_age_no=[] # Wil contain ages of all relatives
    for k in range(0, int(j)):
        l= st.selectbox(label=f'Enter Relative {k+1} Type', options=[f'{k+1} Parent', f'{k+1} Full Sibling', f'{k+1} Half Sibling', f'{k+1} Grandparent', f'{k+1} Aunt', f'{k+1} Uncle', f'{k+1} Half Aunt', f'{k+1} Half Uncle', f'{k+1} First Cousin'])
        a= st.number_input(label= f'Enter Age(in years) for Relative {k+1}')
        K_collect_no.append(l)
        K_collect_age_no.append(a)


    NO_diabetes=[] # Will contain list of Kx constants for all Diabetic Relatives

    Done_no= K_collect_no
    Kx= [0.5, 0.25, 0.125] # Kx=[Parent/Full Sibling, half sibling, grandparent, aunt or uncle, half aunt, half uncle or first cousin]
    
    for j in range(len(Done_no)):

        if (Done_no[j]== f'{j+1} Parent'):
            K= Kx[0]

        elif (Done_no[j]== f'{j+1} Full Sibling'):
            K= Kx[0]

        elif (Done_no[j]== f'{j+1} Aunt'):
            K= Kx[1]

        elif (Done_no[j]== f'{j+1} Uncle'):
            K= Kx[1]

        elif (Done_no[j]== f'{j+1} Half Sibling'):
            K= Kx[1]

        elif (Done_no[j]== f'{j+1} Grandparent'):
            K= Kx[1]

        elif (Done_no[j]== f'{j+1} Half Aunt'):
            K= Kx[2]

        elif (Done_no[j]== f'{j+1} Half Uncle'):
            K= Kx[2]

        elif (Done_no[j]== f'{j+1} First Cousin'):
            K= Kx[2]


        NO_diabetes.append(K)



    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #  



# Calculating Diabetes Pedigree Function(DPF):
    DPF_list_yes=[]
    DPF_list_no= []

    # if st.button('Submit Info'):
    for i in range(len(YES_diabetes)):
        DPF_list_yes.append(YES_diabetes[i] * (88 - K_collect_age_yes[i]) +20)

    for i in range(len(NO_diabetes)):
        DPF_list_no.append(NO_diabetes[i] * (K_collect_age_no[i] - 14) + 50)

    if sum(DPF_list_no) == 0:
        st.text('Please enter valid Inputs for Calculating Diabetes Pedigree Function')
    else:

        DPF= (sum(DPF_list_yes))/(sum(DPF_list_no))

    if st.button('Submit Info'):
        st.write('''
            Your calculated Diabetes Pedigree Function
        ''')
        st.text(DPF)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #


# Getting Final Output

model.eval() # prepare model for evaluation

inp= torch.Tensor([preg, bp, sft, BMI, DPF*100, age]) # Input Tensor
# Note:- Diabetes Pedigree Function was scaled by scaler(100) multiplication, and hence in Input Tensor it is given as DPF*100

out= model(inp.float())

_, pred= torch.max(out, 0)

out= pred.tolist()

if st.button("Results"):

# Check if all Inputs are done properly 

    if bp <= 0:
        st.write('''
            #### Please input your Diastolic Blood Pressure before checking the Results
        ''')

    elif sft <= 0:
        st.write('''
            #### Please input your Tricep Skinfold Thickness before checking the Results
        ''')

    elif age <= 0:
        st.write('''
            #### Please input your Age before checking the Results
        ''')

    elif height <= 0:
        st.write('''
            #### Please input your Height before checking the Results
        ''')

    elif weight <= 0:
        st.write('''
            #### Please input your Weight before checking the Results
        ''')

    elif DPF <= float(0):
        st.write('''
            #### Please input your Diabetes Pedigree Function before checking the Results
        ''')

# Display Result based on prediction
    else:

        if out==0:
            st.write('''
            ## Congratulations....!!!! 
            ### FeCare model has predicted you are not Diabetic
            ''')
        elif out==1:
            st.write('''
            ## Calm Down.. 
            ### FeCare model has predicted you are a Diabetic
            ### Please visit your nearest lab for Glucose Tolerance Test
            ''')

# st.write(bp)
# st.write(sft)
# st.write(BMI)
# st.write(DPF*100)
# st.write(age)

