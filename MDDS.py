import pickle
import streamlit as st
from streamlit_option_menu import option_menu


cold_disease_model= pickle.load(open('COLD_COVID_ALLERGY_FLU_prediction_model.sav','rb'))
diabetes_model= pickle.load(open('Diabetes_prediction_model.sav', 'rb'))
heart_diesease_model= pickle.load(open('heart_disease_prediction_model.sav','rb'))


# st.title('Multi-Disease Detection System')

# with st.sidebar:
selected = option_menu('Multi-Disease Detection System', 
                         ['Covid, Flu, Cold or Allergy Detection','Diabetes', 'Heart Disease'], 
                         icons=['virus','activity','suit-heart-fill'], 
                         default_index=0,orientation='horizontal')


st.markdown(
    """
    <style>
        
        /* Option menu at the top */
        .css-1lcbmhc {
            background-color: #ffffff !important; /* White background for the sidebar */
            color: #ffffff !important; /* Dark grey text */
            padding: 10px 0;
            border-radius: 0;
        }

        /* Title and headers text color */
        h1, h2, h3, h4, h5, h6, p, label {
            color: #333333; /* Dark grey text */
        }

        .main-title {
            text-align: center;
            font-size: 36px;
            color: #00468B;
            font-weight: bold;
        }

        .section-header {
            text-align: center;
            font-size: 24px;
            color: #0072B2;
            margin-top: 20px;
        }

    </style>
    """,
    unsafe_allow_html=True
)


if (selected == 'Covid, Flu, Cold or Allergy Detection'):
  st.markdown("<div class='main-title'>Covid, Flu, Cold or Allergy Detection</div>", unsafe_allow_html=True)
  st.markdown("<div class='section-header'>Please fill out the symptoms below</div>", unsafe_allow_html=True)

  
  # st.write('Input 1 if Yes/Positive')
  # st.write('Input 0 if No/Negative')
  # st.write('Input 1 if Yes/Positive, 0 if No/Negative')
    
  col1, col2 = st.columns(2)
  fields = [
        ('Presence of cough', 'COUGH'), ('Presence of muscle aches', 'MUSCLE_ACHES'),
        ('Presence of tiredness', 'TIREDNESS'), ('Presence of sore throat', 'SORE_THROAT'),
        ('Presence of runny nose', 'RUNNY_NOSE'), ('Presence of stuffy nose', 'STUFFY_NOSE'),
        ('Presence of fever', 'FEVER'), ('Presence of nausea', 'NAUSEA'),
        ('Vomiting', 'VOMITING'), ('Diarrhea', 'DIARRHEA'),
        ('Presence of shortness of breath', 'SHORTNESS_OF_BREATH'),
        ('Presence of difficulty breathing', 'DIFFICULTY_BREATHING'),
        ('Loss of taste', 'LOSS_OF_TASTE'), ('Loss of smell', 'LOSS_OF_SMELL'),
        ('Presence of itchy nose', 'ITCHY_NOSE'), ('Presence of itchy eyes', 'ITCHY_EYES'),
        ('Presence of itchy mouth', 'ITCHY_MOUTH'), ('Presence of itchy inner ear', 'ITCHY_INNER_EAR'),
        ('Presence of sneezing', 'SNEEZING'), ('Presence of pink eye', 'PINK_EYE')
    ]
  inputs = {}
  for i, (label, key) in enumerate(fields):
        col = col1 if i % 2 == 0 else col2
        inputs[key] = col.text_input(label, placeholder="Enter 1 for Yes, 0 for No", key=key, help="Input binary values only.")
    
  cold_diagnosis = ''
  if st.button('COVID, Flu, Cold or Allergy Test Result', key='cold_test', help="Click to view results"):
      cold_pred = cold_disease_model.predict([[inputs[key] for key in inputs]])
      diagnosis_map = {
            'ALLERGY': 'This person has allergy!!',
            'COLD': 'This person has cold!!',
            'COVID': 'This person has COVID!!',
            'FLU': 'This person has flu!!'
        }
      cold_diagnosis = diagnosis_map.get(cold_pred[0], 'Diagnosis is unclear.')
      st.markdown(f"<div class='result'>{cold_diagnosis}</div>", unsafe_allow_html=True)





if (selected == 'Diabetes'):
  st.markdown("<div class='main-title'>Diabetes Detection</div>", unsafe_allow_html=True)
  st.markdown("<div class='section-header'>Please fill out the symptoms below</div>", unsafe_allow_html=True)

  col1, col2, col3 = st.columns(3)

  with col1:
    Pregnancies	= st.text_input ('Number of Pregnancies')
  with col2:
    Glucose	=st.text_input ('Glucose Level')
  with col1:
    BloodPressure =st.text_input ('Blood Pressure Level')
  with col2:
    SkinThickness	=st.text_input ('Skin Thickness Value')
  with col1:
    Insulin	=st.text_input ('Insulin Level')
  with col2:
    BMI	=st.text_input ('BMI Value')
  with col1:
    DiabetesPedigreeFunction =	st.text_input ('Diabetes Pedigree Function value')
  with col2:
    Age	 =st.text_input ('Age of the Person')

  dia_diagnosis= ''

  if st.button('Diabetes Test Result'):
    dia_pred=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    if (dia_pred[0]==1):
      dia_diagnosis = 'The person has diabetes!!'
    else:
      dia_diagnosis = 'The person is not diabetic !!'

  st.success(dia_diagnosis)


if (selected == 'Heart Disease'):
  st.markdown("<div class='main-title'>Heart Disease Detection</div>", unsafe_allow_html=True)
  st.markdown("<div class='section-header'>Please fill out the symptoms below</div>", unsafe_allow_html=True)

  # age			         age
  # sex              sex
  # cp               chest pain type (4 values)
  # trestbps         resting blood pressure
  # chol             serum cholestoral in mg/dl
  # fbs              fasting blood sugar > 120 mg/dl
  # restecg          resting electrocardiographic results (values 0,1,2)
  # thalach          maximum heart rate achieved
  # exang            exercise induced angina
  # oldpeak          oldpeak = ST depression induced by exercise relative to rest
  # slope            the slope of the peak exercise ST segment
  # ca               number of major vessels (0-3) colored by flourosopy
  # thal             thal: 0 = normal; 1 = fixed defect; 2 = reversable defect

  age = st.text_input('Age of the Person')
  sex = st.text_input('Sex of the person (male/female)')
  cp = st.text_input('Chest pain type (4 values)')
  trestbps = st.text_input('Resting blood pressure')
  chol = st.text_input('Serum cholesterol in mg/dl')
  fbs = st.text_input('Fasting blood sugar > 120 mg/dl')
  restecg = st.text_input('Resting electrocardiographic results (values 0,1,2)')
  thalach = st.text_input('Maximum heart rate achieved')
  exang = st.text_input('Exercise induced angina (yes/no)')
  oldpeak = st.text_input('Oldpeak = ST depression induced by exercise relative to rest')
  slope = st.text_input('Slope of the peak exercise ST segment')
  ca = st.text_input('Number of major vessels (0-3) colored by fluoroscopy')
  thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')


  try:
      age = float(age) if age else 0
      trestbps = float(trestbps) if trestbps else 0
      chol = float(chol) if chol else 0
      fbs = float(fbs) if fbs else 0
      restecg = int(restecg) if restecg else 0
      thalach = float(thalach) if thalach else 0
      oldpeak = float(oldpeak) if oldpeak else 0
      slope = int(slope) if slope else 0
      ca = int(ca) if ca else 0
      thal = int(thal) if thal else 0
        
      sex = 1 if sex == 'male' else 0

       
      exang = 1 if exang == 'yes' else 0
        
       
      cp = int(cp) if cp else 0  
  
  except SomeException as e:
    print(f"An error occurred: {e}")

  heart_diagnosis= ''

  if st.button('Heart Disease Test Result'):
    heart_pred=heart_diesease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if (heart_pred[0]==1):
      heart_diagnosis = 'The person has heart disease!!'
    else:
      heart_diagnosis = 'The person do not have heart disease !!'

  st.success(heart_diagnosis)
