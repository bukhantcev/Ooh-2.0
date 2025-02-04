import datetime
from calendar import monthrange
from django.db import models
import os



from forms.models import Event, Event_type
#----------------------------------------CALENDAR
month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
current_year = datetime.datetime.now().year
current_month = month_text[datetime.datetime.now().month]


class Calendar:
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    year_title = current_year

    month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

    def cal_text(current_month):
        return month_text(current_month)

my_calendar = Calendar


def calendar (result='', user_valid=False, card_header_bg_color='', author=''):       #--------------------------------------------DAYS
    current_year = my_calendar.current_year
    current_month = my_calendar.current_month
    days_quantity = monthrange(current_year, current_month)[1]
    weekdays = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}



    button_tg1 = '<a href="?text_message=' if user_valid == True else ''
    button_tg2 = '" type="submit">Отравить в телегу</a>' if user_valid == True else ''


    for i in range(days_quantity):
        today_color = card_header_bg_color if i+1 == datetime.datetime.now().day else ''
        event_li = ''
        date = datetime.datetime(current_year, current_month, i+1)
        event_object = Event.objects.order_by('date')
        event_type_for_color = Event_type.objects

        for event in event_object:



            id = f'event_id{event.id}'
            ev_name = event.name
            ev_date = event.date
            ev_time =   f'{str(ev_date).split(" ")[1].split(":")[0]}:{str(ev_date).split(" ")[1].split(":")[1]}'

            ev_type = event.type
            event_type_for_color = Event_type.objects.get(type=str(ev_type))#------COLOR EVENT
            btn_color = f'background-color: {event_type_for_color.button_color}; border-color: {event_type_for_color.button_color}'#------COLOR EVENT
            ev_location = event.location
            ev_utochneniya = f'<h5 style="color: red">Описание:<br></h5><p>{event.utochneniya}</p>' if event.utochneniya!='' else ''
            ev_staff = f'Свет - {event.svet}<br>Звук - {event.zvuk}<br>Видео - {event.video}<br>Декорации - {event.decor}<br>Реквизит - {event.rekvizit}<br>Грим - {event.grim}<br>Костюм - {event.kostum}'
            if str(date).split(' ')[0] in str(ev_date).split(' ')[0]:
                event_li = event_li + f'''<button type="button" class="btn btn-primary" style="font-size: 0.8rem; margin-bottom: 0.1rem; width: 100%; {btn_color}" data-bs-toggle="modal" data-bs-target="#{id}">
  {ev_time} &quot;{ev_name}&quot; ({ev_type})
</button>

<!-- Modal -->
<div class="modal fade" style="width: 100%" id="{id}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title" id="exampleModalLabel">{ev_type} &quot;{ev_name}&quot;&nbsp;&nbsp;Время: {ev_time}</h3>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
      <div class="modal-body">
        <h5 style="color: red">Место проведения: <p style="color: #000"><br>{ev_location}</p><br></h5>

        {ev_utochneniya}
        <h5 style="color: red">Вызываются службы:<br></h5>
        <p>{ev_staff}</p><br>
        <p style="color: #ccc;">{author}</p>
        
        
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
        {button_tg1}{event.id if user_valid == True else ''}{button_tg2}
      </div>
    </div>
  </div>
</div>\n'''
        result = result + f'<div class="col h-100" style="padding-top: 5rem" id="id_card_{i+1}"><div class="card" style="height: 20rem" ><div class="card-header" style="font-size: 1rem; {today_color}">{i+1} {weekdays[date.weekday()]}</div><div class="card-body"><ul style="margin-right: 2rem">{event_li}</ul></p></div></div></div>\n'
    return result

def calendar_switch_month(): #---------------------MONTS
    month_text = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    result = []
    final = ''
    ind2 = 0
    for i in range(11):
        ind = my_calendar.current_month
        if i < (12-ind):

            ind = ind+i +1
            result.append(ind)
        else:
            ind2 = ind2 + 1
            result.append(ind2)
    for i in result:
        final = final + f'<li><a class="dropdown-item" href="?month={i}" type="submit">{month_text[i]}</a></li>' + '\n'




    return final


def calendar_switch_year(): #__________________________________YEARS
    current_year = my_calendar.current_year
    next_year = my_calendar.current_year + 1
    real_year = datetime.datetime.now().year
    return {'current_year': current_year, 'next_year': next_year, 'real_year': real_year}
#----------------------------------------------------------------------------------------CALENDAR


#--------------Autoscroll today______------------

def autoscroll():
    today =f'#id_card_{datetime.datetime.now().day}'

    return today



#--SPEKTAKLI

class Spect(models.Model):

    label = 'q'
    name = models.CharField(max_length=500, verbose_name="Название спектакля", unique=True)
    link = models.CharField(max_length=500, default='', verbose_name="Ссылка на спектакль", blank=True)
    length = models.CharField(max_length=50, default='', verbose_name="Длительность спектакля", blank=True)
    video = models.CharField(max_length=5000, default='', verbose_name="Видео спектакля", blank=True)
    svet_doc = models.FileField(upload_to=f'materials/{label}/svet_doc/', verbose_name='Свет', blank=True, default='')
    zvuk_doc = models.FileField(upload_to=f'materials/{label}/zvuk_doc/', verbose_name='Звук', blank=True, default='')
    video_doc = models.FileField(upload_to=f'materials/{label}/video_doc/', verbose_name='Видео', blank=True, default='')
    decor_doc = models.FileField(upload_to=f'materials/{label}/decor_doc/', verbose_name='Декорация', blank=True, default='')
    rekv_doc = models.FileField(upload_to=f'materials/{label}/rekv_doc/', verbose_name='Реквизит', blank=True, default='')
    grim_doc = models.FileField(upload_to=f'materials/{label}/grim_doc/', verbose_name='Грим', blank=True, default='')
    kostum_doc = models.FileField(upload_to=f'materials/{label}/kostum_doc/', verbose_name='Костюм', blank=True, default='')
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Спектакль'
        verbose_name_plural = 'Спектакли'

