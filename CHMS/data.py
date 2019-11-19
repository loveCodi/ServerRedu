import joblib
import numpy as np

from CHMS.models import TblDiseaseSysmptom, TblHeard, TblCattle


class Symptoms:
    def __init__(self):
        self.symptoms = []
        self.load_data()

    def load_data(self):
        symptoms = TblDiseaseSysmptom.objects.all()
        for symptom in symptoms:
            self.symptoms.append([symptom.idtbl_disease_sysmptom, symptom.description.lower()])


class Heards:
    def __init__(self):
        self.heards = []
        self.load_data()

    def load_data(self):
        herds = TblHeard.objects.select_related().filter(tbl_farm_idtbl_farm_id=1)
        for herd in herds:
            self.heards.append([herd.idtbl_heard, herd.description.lower()])


class Cattle:
    def __init__(self):
        self.cattle = []
        self.load_data()

    def load_data(self):
        cattle = TblCattle.objects.all()
        for mombe in cattle:
            self.cattle.append([mombe.idtbl_cattle, mombe.date_of_birth, mombe.name.lower()])


class Diagnose:
    def __init__(self, symptoms):
        self.model = joblib.load('C:/Users/AngrybirD/PycharmProjects/ServerRedu/static/models/model.pkl')
        self.symptoms = symptoms
        self.reformatted_symptoms = self.reformat_symptoms()
        self.list_of_symptoms = self.get_descriptions()
        self.encoded_symptoms = self.input_to_one_hot(self.reformatted_symptoms)

    def get_descriptions(self):
        symptoms = Symptoms().symptoms
        descriptions = []
        for symptom in symptoms:
            descriptions.append(symptom[1])
        return descriptions

    def reformat_symptoms(self):
        reformatted_symptoms = {}
        for symptom in self.symptoms:
            if symptom not in reformatted_symptoms:
                reformatted_symptoms[symptom] = 1

        return reformatted_symptoms

    def input_to_one_hot(self, reformatted_symptoms):
        # initialize the target vector with zero values
        enc_input = np.zeros(29)

        for symptom in reformatted_symptoms:
            enc_input[self.list_of_symptoms.index(symptom)] = reformatted_symptoms[symptom]

        return enc_input

    def predict(self):
        # encoded_symptoms = self.input_to_one_hot()
        pred = self.model.predict([self.encoded_symptoms])
        return pred[0]
