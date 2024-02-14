from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from keras.models import load_model
import os
import cv2
import numpy as np
from .models import DataEntry


# Create your views here.
def home_page(request):
    return render(request, 'home_page/home_page.html')


def model(request):
    return render(request, 'home_page/model.html')


def classify_image(request):
    if request.method == 'POST' and request.FILES['photo']:
        image = request.FILES['photo']
        model = load_model(os.path.join('models', 'classifier.h5'))
        img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
        resize = cv2.resize(img, (256, 256))
        yhat = model.predict(np.expand_dims(resize / 255, 0))
        predicted_class = '''Model can't recognize that image''' if yhat[0][0] >= 0.99 or yhat[0][0] < 0.1 else 'Normal' if yhat[0][0] > 0.7 else 'Defected'
        print(yhat[0][0])
        return JsonResponse({'predicted_class': predicted_class})
    else:
        return JsonResponse({'error': 'Image file is missing or invalid.'})


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def model_view(request):
    if request.method == 'POST':
        boolean_value = int(request.POST.get('boolean_value', 0))
        DataEntry.objects.create(boolean_value=boolean_value)

    data_entries = DataEntry.objects.all()
    total_entries = len(data_entries)
    true_entries = data_entries.filter(boolean_value=1).count()
    accuracy = (true_entries / total_entries) * 100 if total_entries > 0 else 0
    rounded_accuracy = round(accuracy, 2)

    return HttpResponse(str(rounded_accuracy))
