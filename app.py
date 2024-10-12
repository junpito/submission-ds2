import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler


# Load the trained model
model = load_model('model.h5')


# Function to get user input
def get_user_input():
    st.title("Data Input Mahasiswa")
    marital_status_options = {
    1: "Single",
    2: "Married",
    3: "Widowed",
    4: "Divorced",
    5: "Facto Union",
    6: "Legally Separated"
    }
    Marital_status = st.selectbox("Marital Status", list(marital_status_options.values()))
    # Menyimpan nilai numerik berdasarkan pilihan yang dibuat
    s_marital_status = [key for key, value in marital_status_options.items() if value == Marital_status][0]


    application_mode_options = {
    1: "1st phase - general contingent",
    2: "Ordinance No. 612/93",
    5: "1st phase - special contingent (Azores Island)",
    7: "Holders of other higher courses",
    10: "Ordinance No. 854-B/99",
    15: "International student (bachelor)",
    16: "1st phase - special contingent (Madeira Island)",
    17: "2nd phase - general contingent",
    18: "3rd phase - general contingent",
    26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
    27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
    39: "Over 23 years old",
    42: "Transfer",
    43: "Change of course",
    44: "Technological specialization diploma holders",
    51: "Change of institution/course",
    53: "Short cycle diploma holders",
    57: "Change of institution/course (International)"
    }
    Application_mode = st.selectbox("Application Mode", list(application_mode_options.values()))
    s_Application_mode = [key for key, value in application_mode_options.items() if value == Application_mode][0]

    Application_order = st.number_input("Application Order", min_value=0, max_value=9, value=1)
    course_options = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)"
    }
    Course = st.selectbox("Course", list(course_options.values()))
    s_Course = [key for key, value in course_options.items() if value == Course][0]

    Daytime_evening_attendance_option = {
        0: "Evening",
        1: "Daytime"
    }
    Daytime_evening_attendance = st.selectbox("Attendance Time", list(Daytime_evening_attendance_option.values()))  
    s_Daytime_evening_attendance = [key for key, value in Daytime_evening_attendance_option.items() if value == Daytime_evening_attendance][0]

    previous_qualification_options = {
    1: "Secondary education",
    2: "Higher education - bachelor's degree",
    3: "Higher education - degree",
    4: "Higher education - master's",
    5: "Higher education - doctorate",
    6: "Frequency of higher education",
    9: "12th year of schooling - not completed",
    10: "11th year of schooling - not completed",
    12: "Other - 11th year of schooling",
    14: "10th year of schooling",
    15: "10th year of schooling - not completed",
    19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
    38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    42: "Professional higher technical course",
    43: "Higher education - master (2nd cycle)"
    }
    Previous_qualification = st.selectbox("Previous Qualification", list(previous_qualification_options.values()))
    s_Previous_qualification = [key for key, value in previous_qualification_options.items() if value == Previous_qualification][0]


    Previous_qualification_grade = st.slider("Previous Qualification Grade", 0.0, 200.0, 10.0)
    
    
    nationality_options = {
    1: "Portuguese",
    2: "German",
    6: "Spanish",
    11: "Italian",
    13: "Dutch",
    14: "English",
    17: "Lithuanian",
    21: "Angolan",
    22: "Cape Verdean",
    24: "Guinean",
    25: "Mozambican",
    26: "Santomean",
    32: "Turkish",
    41: "Brazilian",
    62: "Romanian",
    100: "Moldova (Republic of)",
    101: "Mexican",
    103: "Ukrainian",
    105: "Russian",
    108: "Cuban",
    109: "Colombian"
    }
    Nationality = st.selectbox("Nationality", list(nationality_options.values()))
    s_Nationality = [key for key, value in nationality_options.items() if value == Nationality][0]

    mother_qualification_options = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    22: "Technical-professional course",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
    }
    Mother_Qualification = st.selectbox("Mother Qualification", list(mother_qualification_options.values()))
    s_Mother_Qualification = [key for key, value in mother_qualification_options.items() if value == Mother_Qualification][0]

    father_qualification_options = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    13: "2nd year complementary high school course",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    20: "Complementary High School Course",
    22: "Technical-professional course",
    25: "Complementary High School Course - not concluded",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    31: "General Course of Administration and Commerce",
    33: "Supplementary Accounting and Administration",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
    }
    Father_Qualification = st.selectbox("Father Qualification", list(father_qualification_options.values()))
    s_Father_Qualification = [key for key, value in father_qualification_options.items() if value == Father_Qualification][0]

    mother_occupation_options = {
    0: "Student",
    1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    2: "Specialists in Intellectual and Scientific Activities",
    3: "Intermediate Level Technicians and Professions",
    4: "Administrative staff",
    5: "Personal Services, Security and Safety Workers and Sellers",
    6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
    7: "Skilled Workers in Industry, Construction and Craftsmen",
    8: "Installation and Machine Operators and Assembly Workers",
    9: "Unskilled Workers",
    10: "Armed Forces Professions",
    90: "Other Situation",
    99: "(blank)",
    122: "Health professionals",
    123: "Teachers",
    125: "Specialists in information and communication technologies (ICT)",
    131: "Intermediate level science and engineering technicians and professions",
    132: "Technicians and professionals, of intermediate level of health",
    134: "Intermediate level technicians from legal, social, sports, cultural and similar services",
    141: "Office workers, secretaries in general and data processing operators",
    143: "Data, accounting, statistical, financial services and registry-related operators",
    144: "Other administrative support staff",
    151: "Personal service workers",
    152: "Sellers",
    153: "Personal care workers and the like",
    171: "Skilled construction workers and the like, except electricians",
    173: "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like",
    175: "Workers in food processing, woodworking, clothing and other industries and crafts",
    191: "Cleaning workers",
    192: "Unskilled workers in agriculture, animal production, fisheries and forestry",
    193: "Unskilled workers in extractive industry, construction, manufacturing and transport",
    194: "Meal preparation assistants"
    }
    Mother_Occupation = st.selectbox("Mother Occupation", list(mother_occupation_options.values()))
    s_Mother_Occupation = [key for key, value in mother_occupation_options.items() if value == Mother_Occupation][0]

    father_occupation_options = {
    0: "Student",
    1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    2: "Specialists in Intellectual and Scientific Activities",
    3: "Intermediate Level Technicians and Professions",
    4: "Administrative staff",
    5: "Personal Services, Security and Safety Workers and Sellers",
    6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
    7: "Skilled Workers in Industry, Construction and Craftsmen",
    8: "Installation and Machine Operators and Assembly Workers",
    9: "Unskilled Workers",
    10: "Armed Forces Professions",
    90: "Other Situation",
    99: "(blank)",
    101: "Armed Forces Officers",
    102: "Armed Forces Sergeants",
    103: "Other Armed Forces personnel",
    112: "Directors of administrative and commercial services",
    114: "Hotel, catering, trade and other services directors",
    121: "Specialists in the physical sciences, mathematics, engineering and related techniques",
    122: "Health professionals",
    123: "Teachers",
    124: "Specialists in finance, accounting, administrative organization, public and commercial relations",
    131: "Intermediate level science and engineering technicians and professions",
    132: "Technicians and professionals, of intermediate level of health",
    134: "Intermediate level technicians from legal, social, sports, cultural and similar services",
    135: "Information and communication technology technicians",
    141: "Office workers, secretaries in general and data processing operators",
    143: "Data, accounting, statistical, financial services and registry-related operators",
    144: "Other administrative support staff",
    151: "Personal service workers",
    152: "Sellers",
    153: "Personal care workers and the like",
    154: "Protection and security services personnel",
    161: "Market-oriented farmers and skilled agricultural and animal production workers",
    163: "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence",
    171: "Skilled construction workers and the like, except electricians",
    172: "Skilled workers in metallurgy, metalworking and similar",
    174: "Skilled workers in electricity and electronics",
    175: "Workers in food processing, woodworking, clothing and other industries and crafts",
    181: "Fixed plant and machine operators",
    182: "Assembly workers",
    183: "Vehicle drivers and mobile equipment operators",
    192: "Unskilled workers in agriculture, animal production, fisheries and forestry",
    193: "Unskilled workers in extractive industry, construction, manufacturing and transport",
    194: "Meal preparation assistants",
    195: "Street vendors (except food) and street service providers"
    }
    Father_Occupation = st.selectbox("Father Occupation", list(father_occupation_options.values()))
    s_Father_Occupation = [key for key, value in father_occupation_options.items() if value == Father_Occupation][0]

    Admission_grade = st.slider("Admission Grade", 0.0, 200.0, 10.0)

    Displaced_option = {
        0: "No",
        1: "Yes"
    }
    Displaced = st.selectbox("Displaced", list(Displaced_option.values()))  # 0: Tidak, 1: Ya
    s_Displaced = [key for key, value in Displaced_option.items() if value == Displaced][0]

    educational_special_needs_options = {
    0: "No",
    1: "Yes"
    }
    Educational_special_needs = st.selectbox("Educational Special Needs", list(educational_special_needs_options.values()))
    s_Educational_special_needs = [key for key, value in educational_special_needs_options.items() if value == Educational_special_needs][0]

    debtor_options = {
    0: "No",
    1: "Yes"
    }
    Debtor = st.selectbox("Debtor", list(debtor_options.values()))
    s_Debtor = [key for key, value in debtor_options.items() if value == Debtor][0]

    tuition_fees_options = {
    0: "No",
    1: "Yes"
    }
    Tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", list(tuition_fees_options.values()))
    s_Tuition_fees_up_to_date = [key for key, value in tuition_fees_options.items() if value == Tuition_fees_up_to_date][0]

    gender_options = {
    0: "Female",
    1: "Male"
    }
    Gender = st.selectbox("Gender", list(gender_options.values()))
    s_Gender = [key for key, value in gender_options.items() if value == Gender][0]

    scholarship_holder_options = {
    0: "No",
    1: "Yes"
    }
    Scholarship_holder = st.selectbox("Scholarship Holder", list(scholarship_holder_options.values()))
    s_Scholarship_holder = [key for key, value in scholarship_holder_options.items() if value == Scholarship_holder][0]

    Age_at_enrollment = st.number_input("Age at Enrollment", min_value=18, max_value=100, value=18)
    
    International_options = {
        0: "No",
        1: "Yes"
    }
    International = st.selectbox("International", list(International_options.values()))
    s_International = [key for key, value in International_options.items() if value == International][0]

    Curricular_units_1st_sem_credited = st.number_input("Curricular Units 1st Sem Credited", min_value=0, max_value=100)
    Curricular_units_1st_sem_enrolled = st.number_input("Curricular Units 1st Sem Enrolled", min_value=0, max_value=100)
    Curricular_units_1st_sem_evaluations = st.number_input("Curricular Units 1st Sem Evaluations", min_value=0, max_value=100)
    Curricular_units_1st_sem_approved = st.number_input("Curricular Units 1st Sem Approved", min_value=0, max_value=100)
    Curricular_units_1st_sem_grade = st.slider("Curricular Units 1st Sem Grade", 0.0, 20.0, 10.0)
    Curricular_units_1st_sem_without_evaluations = st.number_input("Curricular Units 1st Sem Without Evaluations", min_value=0, max_value=100)

    Curricular_units_2nd_sem_credited = st.number_input("Curricular Units 2nd Sem Credited", min_value=0, max_value=100)
    Curricular_units_2nd_sem_enrolled = st.number_input("Curricular Units 2nd Sem Enrolled", min_value=0, max_value=100)
    Curricular_units_2nd_sem_evaluations = st.number_input("Curricular Units 2nd Sem Evaluations", min_value=0, max_value=100)
    Curricular_units_2nd_sem_approved = st.number_input("Curricular Units 2nd Sem Approved", min_value=0, max_value=100)
    Curricular_units_2nd_sem_grade = st.slider("Curricular Units 2nd Sem Grade", 0.0, 20.0, 10.0)
    Curricular_units_2nd_sem_without_evaluations = st.number_input("Curricular Units 2nd Sem Without Evaluations", min_value=0, max_value=100)

    Unemployment_rate = st.slider("Unemployment Rate", 0.0, 100.0, 5.0)
    Inflation_rate = st.slider("Inflation Rate", 0.0, 100.0, 2.0)
    GDP = st.slider("GDP", 0.0, 1000000.0, 50000.0)

    # Store the inputs in a dictionary
    user_data = {
        'Marital_status': s_marital_status,
        'Application_mode': s_Application_mode,
        'Application_order': Application_order,
        'Course': s_Course,
        'Daytime_evening_attendance': s_Daytime_evening_attendance,
        'Previous_qualification': s_Previous_qualification,
        'Previous_qualification_grade': Previous_qualification_grade,
        'Nationality': s_Nationality,
        'Mothers_qualification': s_Mother_Qualification ,
        'Fathers_qualification': s_Father_Qualification,
        'Mothers_occupation': s_Mother_Occupation,
        'Fathers_occupation': s_Father_Occupation,
        'Admission_grade': Admission_grade,
        'Displaced': s_Displaced,
        'Educational_special_needs': s_Educational_special_needs,
        'Debtor': s_Debtor,
        'Tuition_fees_up_to_date': s_Tuition_fees_up_to_date,
        'Gender': s_Gender,
        'Scholarship_holder': s_Scholarship_holder,
        'Age_at_enrollment': Age_at_enrollment,
        'International': s_International,
        'Curricular_units_1st_sem_credited': Curricular_units_1st_sem_credited,
        'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_evaluations': Curricular_units_1st_sem_evaluations,
        'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
        'Curricular_units_1st_sem_without_evaluations': Curricular_units_1st_sem_without_evaluations,
        'Curricular_units_2nd_sem_credited': Curricular_units_2nd_sem_credited,
        'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_evaluations': Curricular_units_2nd_sem_evaluations,
        'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
        'Curricular_units_2nd_sem_without_evaluations': Curricular_units_2nd_sem_without_evaluations,
        'Unemployment_rate': Unemployment_rate,
        'Inflation_rate': Inflation_rate,
        'GDP': GDP
    }
    
    return pd.DataFrame(user_data, index=[0])


# Streamlit app layout
st.title("Student Success Prediction")

# Get user input
input_df = get_user_input()

# Preprocessing data 
scaler = StandardScaler()
input_scaled = scaler.fit_transform(input_df)

# Mengonversi DataFrame ke array NumPy
input_array = np.array(input_scaled)
st.write(input_array.shape)
# Show user inputs as a dataframe
st.subheader("User Input Data")
st.write(input_df.head())




# Predict the result using the loaded model
if st.button("Predict"):
    prediction = model.predict(input_array)
    st.subheader("Prediction Result")
    st.write(f"Prediction: {prediction[0][0]}")