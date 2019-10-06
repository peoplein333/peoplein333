from .models import Juicy, Gongcha, Subway, Starbucks, Momstouch, Ediya, Sinjeon, Caffebene, Mrsd
from django.shortcuts import get_object_or_404, render, redirect
from chartit import DataPool, Chart, PivotDataPool, PivotChart

# Create your views here.

def franchise_list(request):
    return render(request, 'franchise/franchise_list.html')

def juicy(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Juicy},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'column',
                'stacking': False},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/JUICY.html', {'chart_list': [cht]})

def gongcha(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Gongcha},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'column',
                'stacking': False},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/GONGCHA.html', {'chart_list': [cht]})

def subway(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Subway},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'column',
                'stacking': False},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/SUBWAY.html', {'chart_list': [cht]})

def starbucks(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Starbucks},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'column',
                'stacking': False},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/STARBUCKS.html', {'chart_list': [cht]})

def momstouch(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Momstouch},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'column',
                'stacking': False},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/MOMSTOUCH.html', {'chart_list': [cht]})


def ediya(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Ediya},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'column',
                'stacking': False},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/EDIYA.html', {'chart_list': [cht]})


def sinjeon(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Sinjeon},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'column',
                'stacking': False},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/SINJEON.html', {'chart_list': [cht]})

def caffebene(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Caffebene},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'column',
                'stacking': False},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/CAFFEBENE.html', {'chart_list': [cht]})

def mrsd(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Mrsd},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'column',
                'stacking': False},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/MRSD.html', {'chart_list': [cht]})
