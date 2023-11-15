from django.shortcuts import render
from keras.models import load_model
import cv2


# Create your views here.
def home_page(request):
    # model = load_model()
    # img = cv2.imread()
    return render(request, 'home_page/home_page.html')


def model(request):
    return render(request, 'home_page/model.html')
