from django.shortcuts import render
from django.http import JsonResponse
from keras.models import load_model
import os
import cv2
import numpy as np
import tensorflow as tf

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