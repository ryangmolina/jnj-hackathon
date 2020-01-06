import os

import pandas as pd
import joblib


"""
questions = {
    "0": [
        "How to file leaves?",
        "What are the existing company clubs?",
        "How to reset password?",
        "How to file complaint against another employer?",
        "How to get COE?",
        "How many leaves do I have?",
        "How to file salary loan?",
        "How to do reimbursement?",
        "How to apply for training?",
    ],
    "1": ["How to get promoted?", "How to promote someone?",],
    "2": [
        "What are the benefits that I can avail upon regularization?",
        "What are the company policies?",
        "What is the company hotline?",
        "What is the company organization?",
        "How to connect to wifi?",
        "When is the schedule of salary disbursement per month?",
        "How install work applications in PC?",
    ],
    "3": ["How to get promoted?", "How to promote someone?",],
    "4": ["How to get clearance?", "How to get transferred to another unit?",],
}
"""

questions = {
    "3": [
        "What are the benefits that I can avail upon regularization?",
        "What are the company policies?",
        "What is the company hotline?",
        "What is the company organization?",
        "How to connect to wifi?",
        "When is the schedule of salary disbursement per month?",
        "How install work applications in PC?",
        "How to file leaves?",
        "What are the existing company clubs?",
        "How to update employee data?"
    ],
    "2": [
        "Job Change Request",
        "How to get COE?",
        "How to file salary loan?",
        "How to apply for training?",
        "How to reset password?",
        "How to get promoted?",
        "How to promote someone?"
    ],
    "4": [
        "How to file complaint against another employer?",
        "How many leaves do I have?",
        "How to do reimbursement?",
    ],
    "0": [
        "How to get clearance?",
        "How to get transferred to another unit?",
    ],
    "1": [
        "How to transfer to other units?",
        "How to file paternity leaves?",
    ]
}

def predict(form_data):
    data = pd.DataFrame(form_data, index=[0])
    # First need to arrange feature accordingly, so that it can be automated
    data = data.loc[
        :,
        [
            "age",
            "generation",
            "gender",
            "civil_status",
            "city_municipality",
            "province",
            "highest_educational_attainment",
            "education_status",
            "tenure",
            "employment_status",
            "pay_class",
            "last_employee_movement",
            "latest_performance_rating",
            "compa-ratio",
            "job_loc",
            "rank",
            "unit",
        ],
    ]

    Listpay1 = ["BC I", "BC II", "WC III", "WC II", "WC IV", "WC I"]
    Listpay2 = [
        "BC VIII",
        "BC VII",
        "S I",
        "S II-B",
        "S II-A",
        "BC VI",
        "BC V",
        "WC VI",
        "BC IV",
        "BC III",
        "WC V",
    ]
    Listpay3 = ["BC IX", "S III-A", "S III-B", "S V-A", "S V-B", "S IV-B", "S IV-A"]
    Listpay4 = ["S VIII", "S VII", "S VI"]
    Listpay5 = ["S X", "S IX", "S XI", "S XII", "S XIII"]

    # function for the transformation to categorical variables
    def pay_to_cat(x):
        if x in Listpay1:
            return 0
        if x in Listpay2:
            return 1
        if x in Listpay3:
            return 2
        if x in Listpay4:
            return 3
        if x in Listpay5:
            return 4
        else:
            return x


    Mindanao = [
        "LANAO DEL NORTE",
        "ZAMBOANGA",
        "SOUTH COTABATO",
        "BASILAN",
        "BUKIDNON",
        "MALAY",
        "MISAMIS ORIENTAL",
        "SURIGAO DEL SUR",
        "SURIGAO DEL NORTE",
    ]
    Luzon = [
        "LAGUNA",
        "BATAAN",
        "RIZAL",
        "NUEVA ECIJA",
        "BULACAN",
        "BATANGAS",
        "CAVITE",
        "OCCIDENTAL MINDORO",
        "QUEZON",
        "ZAMBALES",
        "PANGASINAN",
        "BENGUET",
        "PAMPANGA",
        "NUEVA VIZCAYA",
        "CAMARINES SUR",
        "LA UNION PROVINCE",
        "TARLAC",
        "PASIG CITY",
        "MANILA",
        "BACOOR",
        "QUEZON CITY",
        "ILOCOS SUR",
        "QUEZON PROVINCE",
        "MALABON CITY",
        "MARIKINA CITY",
        "MUNTINLUPA",
        "ISABELA",
        "PALAWAN",
        "ALBAY",
        "CAMARINES NORTE",
        "MARINDUQUE",
        "LUCENA CITY",
    ]
    Visayas = [
        "CAPIZ",
        "AKLAN",
        "BOHOL",
        "ILOILO",
        "LEYTE",
        "CEBU",
        "EASTERN SAMAR",
        "SOUTHERN LEYTE",
        "WESTERN SAMAR",
        "NORTHERN SAMAR",
        "NEGROS ORIENTA",
        "NEGROS ORIENTAL",
    ]
    # fontion for the transformation to categorical variables
    def Regio_to_cat(x):
        if x in Mindanao:
            return "Mindanao"
        if x in Luzon:
            return "Luzon"
        if x in Visayas:
            return "Visayas"
        else:
            return "Metro Manila"

    data["province"] = data["province"].apply(Regio_to_cat)
    data["pay_class"] = data["pay_class"].apply(pay_to_cat)
    data.drop("city_municipality", axis=1, inplace=True)
    data = pd.get_dummies(data)
    
    with open(os.path.join(os.getcwd(), "app/personalizations/question_clustering", "model.pkl"), "rb") as file:
        model = joblib.load(file)

    with open(os.path.join(os.getcwd(), "app/personalizations/question_clustering", "scaler.pkl"), "rb") as file:
        scaled = joblib.load(file)

    with open(os.path.join(os.getcwd(), "app/personalizations/question_clustering", "blanket.pkl"), "rb") as file:
        blanket = joblib.load(file)

    # import blanket.pkl name it blanket
    final_data = pd.concat([blanket, data], sort=False)
    final_data = final_data.iloc[:, range(35)]
    final_data = final_data.fillna(0)
    # import scaler.pkl, name it scaled
    transformed = scaled.transform(final_data)
    # import model.pkl name it model
    return questions.get(str(model.predict(transformed)[0]))
