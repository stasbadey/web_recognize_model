from django.shortcuts import render
from keras.models import load_model
import os
import cv2


# Create your views here.
def home_page(request):

    # img = cv2.imread()
    return render(request, 'home_page/home_page.html')


def model(request):
    model = load_model(os.path.join('models', 'anotherclassifier.h5'))
    return render(request, 'home_page/model.html')
