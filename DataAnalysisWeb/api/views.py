# Create your views here.

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import xlrd
from django.utils.safestring import mark_safe as safe
import django.utils
import json

def index(request):
    dates = pd.date_range('20130101',periods=6)
    df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
    data = df.to_json()
    return HttpResponse(data, mimetype='application/json')