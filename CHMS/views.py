from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from CHMS.data import Symptoms, Heards, Cattle, Diagnose
from CHMS.diseases import *


def home(request):
    return render(request, 'home.html')


def diagnosis(request):
    symptoms = Symptoms().symptoms
    herds = Heards().heards
    cattle = Cattle().cattle
    return render(request, 'pred.html', {'symptoms': symptoms,
                                         'herds': herds,
                                         'cattle': cattle})


def results(request, disease):
    info_ye_dzz = ''

    if disease == 'anaplasmosis':
        info_ye_dzz = Diseases().all_info[0]
    if disease == 'anthrax':
        info_ye_dzz = Diseases().all_info[1]
    if disease == 'babesiosis':
        info_ye_dzz = Diseases().all_info[2]
    if disease == 'blue tongue':
        info_ye_dzz = Diseases().all_info[3]
    if disease == 'foot and mouth':
        info_ye_dzz = Diseases().all_info[4]
    if disease == 'lumpy skin':
        info_ye_dzz = Diseases().all_info[5]
    if disease == 'theileriases':
        info_ye_dzz = Diseases().all_info[6]

    return render(request, 'pred_res.html', {'dzz_info': info_ye_dzz})


@csrf_exempt
def symptoms_reciever(request):
    prediction = ''
    if request.method == 'POST':
        symptoms_from_user = set()
        symptoms = 0
        for values in request.POST.lists():
            symptoms = values[1]

        for symptom in symptoms:
            symptoms_from_user.add(symptom)

        diagnose = Diagnose(symptoms_from_user)
        prediction = diagnose.predict()

    return HttpResponse(prediction)
