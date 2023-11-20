from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from keras.models import load_model
import os
import cv2
import numpy as np
import tensorflow as tf
from .models import Response


# Create your views here.
def home_page(request):
    return render(request, 'home_page/home_page.html')


def model(request):
    return render(request, 'home_page/model.html')


def classify_image(request):
    if request.method == 'POST' and request.FILES['photo']:
        image = request.FILES['photo']
        model = load_model(os.path.join('models', 'anotherclassifier.h5'))
        img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
        resize = cv2.resize(img, (256, 256))
        yhat = model.predict(np.expand_dims(resize / 255, 0))
        predicted_class = 'Normal' if yhat[0][0] > 0.7 else 'Defected'
        print(yhat[0][0])
        return JsonResponse({'predicted_class': predicted_class})
    else:
        return JsonResponse({'error': 'Image file is missing or invalid.'})

def save_response(request):
    if request.method == 'POST':
        response_value = int(request.POST.get('response'))
        response = Response(boolean_value=response_value)
        response.save()
        return HttpResponse(status=200)
    return HttpResponse(status=400)

def get_percentage(request):
    total_responses = Response.objects.count()
    if total_responses > 0:
        positive_responses = Response.objects.filter(boolean_value=1).count()
        percentage = (positive_responses / total_responses) * 100
        rounded_percentage = round(percentage, 2)  # Округляем до 2 знаков после запятой
        return JsonResponse({'percentage': rounded_percentage})
    return JsonResponse({'percentage': 0})


def model_view(request):
    if request.method == 'POST':
        boolean_value = int(request.POST.get('boolean_value', 0))
        DataEntry.objects.create(boolean_value=boolean_value)

    data_entries = DataEntry.objects.all()
    total_entries = len(data_entries)
    true_entries = data_entries.filter(boolean_value=1).count()
    accuracy = (true_entries / total_entries) * 100 if total_entries > 0 else 0

    return render(request, 'your_template.html', {'accuracy': accuracy})