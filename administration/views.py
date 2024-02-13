from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from main.models import User
from django.http import HttpResponse, JsonResponse
from django.db.models import Q, F, Sum
from datetime import datetime, timedelta
from django.db.models.functions import TruncMonth
from django.db.models import Avg
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.utils.dateformat import DateFormat

def dashboard(request):

    registered_users = User.objects.all().count()
    application_allowed_users = User.objects.filter(is_deleted = 0, application_access = User.APPLICATION_ACCESS_STATUS_ALLOWED).count()
    application_declined_users = User.objects.filter(is_deleted = 0, application_access = User.APPLICATION_ACCESS_STATUS_DECLINED).count()
    users_deleted = User.objects.filter(is_deleted=1).count()

    active_users = User.objects.all().count()

    admin_count = User.objects.filter(is_deleted = 0, is_admin = True).count()
    customer_count = User.objects.filter(is_deleted = 0, is_admin = False).count()

    current_date = datetime.now()

    userGrowthData = getUsersGrowthData()


    return render(request, 'dashboard.html', context={'registered_users':registered_users, 'users_deleted':users_deleted, 
        'current_date':current_date, 'userGrowthData':userGrowthData, 'application_allowed_users':application_allowed_users, 
        'application_declined_users':application_declined_users, 'admin_count':admin_count, 'customer_count':customer_count, 'active_users':active_users})


def getUsersGrowthData():
    today = datetime.now().date()
    start_date = today - timedelta(days=365)

    data = (
        User.objects
        .annotate(month=TruncMonth('date_joined'))
        .filter(date_joined__gte=start_date)
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    labels = []
    values = []
    cumulative_count = 0

    for d in data:
        month_name = DateFormat(d['month']).format('F')
        labels.append(month_name)
        cumulative_count += d['count']
        values.append(cumulative_count)

    return {'labels': labels, 'values': values}

