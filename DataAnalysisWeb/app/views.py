"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
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



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    #make data
    dates = pd.date_range('20130101',periods=6)
    df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
    data = df.to_json()

    #save it out to file also
    f = open('app/static/data.json', 'wt', encoding='utf-8')
    f.write(data)



    #plotting

    #generate Figure
    #series 1 plot
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    #series 2 plot
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()

    plt.ylabel('some numbers')
    plt.xlabel('the dates')

    plt.savefig('app/static/app/content/images/Figure_1.png', bbox_inches='tight')

    plt.close()




    #send it into view
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'data':data
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
