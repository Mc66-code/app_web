from django.shortcuts import render
from app_covid19.forms import NouveauPassionForm
from app_covid19.models import Passion


def passion(request):
    sauvegarde = False
    
    if request.method == "POST":
        form = NouveauPassionForm(request.POST, request.FILES)
        if form.is_valid():
            passion = Passion()
          #  passion.nom = form.cleaned_data["nom"]
            passion.photo = form.cleaned_data["photo"]
            passion.save()
            sauvegarde = True
    else:
        form = NouveauPassionForm()
    passions = Passion.objects.all()
    return render(request, 'passion.html',locals())



from PIL import Image
import numpy as np
import cv2
from keras.models import load_model
# from keras import backend as K

def prediction(request):
    # K.clear_session()
    inf = Passion.objects.all()
    image = Image.open(inf[0].photo).convert("RGB")
    image = np.array(image)
    image = cv2.resize(image,(224, 224))
    class_names = ['Covid19','Normal','Viral Pneumonia']
    model = load_model('model_.h5')
    y_predict = model.predict(image.reshape(1,224,224,3))
    y_pred = np.argmax(y_predict)
    label = class_names[y_pred] 
    if label == 'Normal':  label = "Ce patient n'a pas de maladie ({}% {}).".format(y_predict[0][y_pred] * 100, label)
    else : label = "Ce patient a {:.2f}% de maladie de {}.".format(y_predict[0][y_pred] * 100, label) 
    # K.clear_session()
    passions = Passion.objects.all()
    passions.delete()
    return render(request, 'prediction.html', {'inf': label })


def home(request):
    context = { }
    return render(request, "home.html", context)

