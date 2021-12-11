from flask import Blueprint, render_template, redirect
from flask_security import login_required
from user_page.test_variable import User_page, translate_days_week
from user_page.data_time_for_calendar import creat_dict_date
from datetime import datetime, time, timedelta, date


user_page = Blueprint('user_page', __name__, template_folder='templates')


@user_page.route('/')
@login_required
def index():
    return redirect('calendar')


@user_page.route('/calendar')
@login_required
def calendar():
    master_time = User_page()
    return render_template('user_page/calendar.html',
                           calendar = creat_dict_date(),
                           master_time_start = master_time.user_time_works_standert_start,
                           master_time_finish = master_time.user_time_works_standert_finish,
                           translate_days_week = translate_days_week,
                           str=str,
                           type=type,
                           list=list,
                           datetime = datetime)


