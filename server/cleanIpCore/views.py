from django.shortcuts import render
from cleanIpCore.models import *


def post_session(request):
    data = json.loads(request.body.decode('utf-8'))
    session  = Session(name=data['name'])
    
