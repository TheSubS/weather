import eel # импортируем EEL библиотеку для мини-браузера в Python
from pyowm.owm import OWM # OWM - то же самое, что и PYOWM
import pyowm # PYOWM используется для отображения данных о погоде
from pyowm.utils.config import get_default_config # файлы конфигурации PYOWM по умолчанию

config_dict = get_default_config() # получение файла конфигурации PYOWM
config_dict['language'] = 'ru' # язык PYOWM

owm = OWM('6d00d1d4e704068d70191bad2673e0cc', config_dict) # API-токен OpenWeatherMap

@eel.expose # скрипт на странице
def get_weather(place): # получение погоды в °C
    try: # попробую и выполню, если будет работать

        city = place # локация
        mgr = owm.weather_manager() # сокращаем
    
        observation = mgr.weather_at_place(city) # сокращение еще раз
        w = observation.weather # коротко и понятно

        temp = w.temperature('celsius')['temp'] # температура в °C
        tempr = round(temp) # округленная температура в °C
        tempmin = w.temperature('celsius')['temp_min'] # минимальная температура в °C
        tempminr = round(tempmin) # округленная минимальная температура в °C
        tempmax = w.temperature('celsius')['temp_max'] # максимальная температура в °C
        tempmaxr = round(tempmax) # округленная максимальная температура в °C

        if w.detailed_status == "ясно": # если - отображать
            return '<img src="clear.png" weight="70" height="70"><b><font size="20px"> Ясно</font></b><h1>' + str(tempr) + ' °C</h1> Мин. температура <font color="#757575">' + str(tempminr) + ' °C</font><br>Макс. температура <font color="#757575">' + str(tempmaxr) + ' °C</font>' # верну
        if w.detailed_status == "переменная облачность": # если - отображать
            return '<img src="partly_clouds.png" weight="70" height="70"><b><font size="20px"> Переменная облачность</font></b><h1>' + str(tempr) + ' °C</h1> Мин. температура <font color="#757575">' + str(tempminr) + ' °C</font><br>Макс. температура <font color="#757575">' + str(tempmaxr) + ' °C</font>' # верну
        if w.detailed_status == "небольшая облачность": # если - отображать
            return '<img src="small_clouds.png" weight="70" height="70"><b><font size="20px"> Легкая облачность</font></b><h1>' + str(tempr) + ' °C</h1> Мин. температура <font color="#757575">' + str(tempminr) + ' °C</font><br>Макс. температура <font color="#757575">' + str(tempmaxr) + ' °C</font>' # верну
        if w.detailed_status == "небольшой дождь": # если - отображать
            return '<img src="light_rain.png" weight="70" height="70"><b><font size="20px"> Легкий дождь</font></b><h1>' + str(tempr) + ' °C</h1> Мин. температура <font color="#757575">' + str(tempminr) + ' °C</font><br>Макс. температура <font color="#757575">' + str(tempmaxr) + ' °C</font>' # верну
        if w.detailed_status == "гроза с небольшим дождём": # если - отображать
            return '<img src="thunder.png" weight="70" height="70"><b><font size="20px"> Гроза</font></b><h1>' + str(tempr) + ' °C</h1> Мин. температура <font color="#757575">' + str(tempminr) + ' °C</font><br>Макс. температура <font color="#757575">' + str(tempmaxr) + ' °C</font>' # верну
        if w.detailed_status == "облачно с прояснениями": # если - отображать
            return '<img src="partly_clouds.png" weight="70" height="70"><b><font size="20px"> Переменная облачность</font></b><h1>' + str(tempr) + ' °C</h1> Мин. температура <font color="#757575">' + str(tempminr) + ' °C</font><br>Макс. температура <font color="#757575">' + str(tempmaxr) + ' °C</font>' # верну   
        if w.detailed_status == "пасмурно": # если - отображать
            return '<img src="clouds.png" weight="70" height="70"><b><font size="20px"> Пасмурно</font></b><h1>' + str(tempr) + ' °C</h1> Мин. температура <font color="#757575">' + str(tempminr) + ' °C</font><br>Макс. температура <font color="#757575">' + str(tempmaxr) + ' °C</font>' # верну  
        if w.detailed_status == "небольшой проливной дождь": # если - отображать
            return '<img src="pour.png" weight="70" height="70"><b><font size="20px"> Ливень</font></b><h1>' + str(tempr) + ' °C</h1> Мин. температура <font color="#757575">' + str(tempminr) + ' °C</font><br>Макс. температура <font color="#757575">' + str(tempmaxr) + ' °C</font>' # верну   
        if w.detailed_status == "дождь": # если - отображать
            return '<img src="rain.png" weight="70" height="70"><b><font size="20px"> Дождь</font></b><h1>' + str(tempr) + ' °C</h1> Мин. температура <font color="#757575">' + str(tempminr) + ' °C</font><br>Макс. температура <font color="#757575">' + str(tempmaxr) + ' °C</font>' # верну   
        if w.detailed_status == "туман": # если - отображать
            return '<img src="haze.png" weight="70" height="70"><b><font size="20px"> Туман</font></b><h1>' + str(tempr) + ' °C</h1> Мин. температура <font color="#757575">' + str(tempminr) + ' °C</font><br>Макс. температура <font color="#757575">' + str(tempmaxr) + ' °C</font>' # верну  

    
        return '<img src="unknown.png"><h1><font size=20px> Состояние <b>не определено <font color="#757575">(' + w.detailed_status + ')</font></b></h1></font><br><b>Обратитесь за помощью в репозиторий GitHub, таким образом Вы поможете сделать программу лучше, спасибо.</b>' # верну
    except: # если не получилось
       return '<img src="unknown.png"><h1><font size=20px> Город <b> <font color="#757575">не найден</font></b></h1></font><b>Возможно, Вы указали несуществующий город или ввели неправильным синтаксисом. Если Вы уверены в том, что всё введено верно - попробуйте изменить название на латиницу или кириллицу (в зависимости от того, как Вы изначально вводили).</b>' # верну

@eel.expose # скрипт на странице
def get_weather_f(place): # получение погоды в °F
    try: # попробую и выполню, если будет работать
        city = place # локация
        mgr = owm.weather_manager() # сокращаем
    
        observation = mgr.weather_at_place(city) # сокращение еще раз
        w = observation.weather # коротко и понятно

        tempf = w.temperature('fahrenheit')['temp'] # температура в °F
        tempfr = round(tempf) # округленная температура в °F
        tempfmin = w.temperature('fahrenheit')['temp_min'] # минимальная температура в °F
        tempfminr = round(tempfmin) # округленная минимальная температура в °F
        tempfmax = w.temperature('fahrenheit')['temp_max'] # максимальная температура в °F
        tempfmaxr = round(tempfmax) # округленная максимальная температура в °F

        if w.detailed_status == "ясно": # если - отображать
            return '<img src="clear.png" weight="70" height="70"><b><font size="20px"> Ясно</font></b><h1>' + str(tempfr) + ' °F</h1> Мин. температура <font color="#757575">' + str(tempfminr) + ' °F</font><br>Макс. температура <font color="#757575">' + str(tempfmaxr) + ' °F</font>' # верну
        if w.detailed_status == "переменная облачность": # если - отображать
            return '<img src="partly_clouds.png" weight="70" height="70"><b><font size="20px"> Переменная облачность</font></b><h1>' + str(tempfr) + ' °F</h1> Мин. температура <font color="#757575">' + str(tempfminr) + ' °F</font><br>Макс. температура <font color="#757575">' + str(tempfmaxr) + ' °F</font>' # верну
        if w.detailed_status == "небольшая облачность": # если - отображать
            return '<img src="small_clouds.png" weight="70" height="70"><b><font size="20px"> Легкая облачность</font></b><h1>' + str(tempfr) + ' °F</h1> Мин. температура <font color="#757575">' + str(tempfminr) + ' °F</font><br>Макс. температура <font color="#757575">' + str(tempfmaxr) + ' °F</font>' # верну
        if w.detailed_status == "небольшой дождь": # если - отображать
            return '<img src="light_rain.png" weight="70" height="70"><b><font size="20px"> Легкий дождь</font></b><h1>' + str(tempfr) + ' °F</h1> Мин. температура <font color="#757575">' + str(tempfminr) + ' °F</font><br>Макс. температура <font color="#757575">' + str(tempfmaxr) + ' °F</font>' # верну
        if w.detailed_status == "гроза с небольшим дождём": # если - отображать
            return '<img src="thunder.png" weight="70" height="70"><b><font size="20px"> Гроза</font></b><h1>' + str(tempfr) + ' °F</h1> Мин. температура <font color="#757575">' + str(tempfminr) + ' °F</font><br>Макс. температура <font color="#757575">' + str(tempfmaxr) + ' °F</font>' # верну
        if w.detailed_status == "облачно с прояснениями": # если - отображать
            return '<img src="partly_clouds.png" weight="70" height="70"><b><font size="20px"> Переменная облачность</font></b><h1>' + str(tempfr) + ' °F</h1> Мин. температура <font color="#757575">' + str(tempfminr) + ' °F</font><br>Макс. температура <font color="#757575">' + str(tempfmaxr) + ' °F</font>' # верну 
        if w.detailed_status == "пасмурно": # если - отображать
            return '<img src="clouds.png" weight="70" height="70"><b><font size="20px"> Пасмурно</font></b><h1>' + str(tempfr) + ' °F</h1> Мин. температура <font color="#757575">' + str(tempfminr) + ' °F</font><br>Макс. температура <font color="#757575">' + str(tempfmaxr) + ' °F</font>' # верну   
        if w.detailed_status == "небольшой проливной дождь": # если - отображать
            return '<img src="pour.png" weight="70" height="70"><b><font size="20px"> Ливень</font></b><h1>' + str(tempfr) + ' °F</h1> Мин. температура <font color="#757575">' + str(tempfminr) + ' °F</font><br>Макс. температура <font color="#757575">' + str(tempfmaxr) + ' °F</font>' # верну   
        if w.detailed_status == "дождь": # если - отображать
            return '<img src="rain.png" weight="70" height="70"><b><font size="20px"> Дождь</font></b><h1>' + str(tempfr) + ' °F</h1> Мин. температура <font color="#757575">' + str(tempfminr) + ' °F</font><br>Макс. температура <font color="#757575">' + str(tempfmaxr) + ' °F</font>' # верну   
        if w.detailed_status == "туман": # если - отображать
            return '<img src="haze.png" weight="70" height="70"><b><font size="20px"> Туман</font></b><h1>' + str(tempfr) + ' °F</h1> Мин. температура <font color="#757575">' + str(tempfminr) + ' °F</font><br>Макс. температура <font color="#757575">' + str(tempfmaxr) + ' °F</font>' # верну   
        
        return '<img src="unknown.png"><h1><font size=20px> Ошибка <b>404 <font color="#757575">(' + w.detailed_status + ')</font></b></h1></font><br><b>Обратитесь за помощью в репозиторий GitHub, таким образом Вы поможете сделать программу лучше, спасибо.</b>' # верну
    except: # если не получилось
          return '<img src="unknown.png"><h1><font size=20px> Город <b> <font color="#757575">не найден</font></b></h1></font><b>Возможно, Вы указали несуществующий город или ввели неправильным синтаксисом. Если Вы уверены в том, что всё введено верно - попробуйте изменить название на латиницу или кириллицу (в зависимости от того, как Вы изначально вводили).</b>' # верну
          
eel.init("web") # выбираем папку для отображения страницы
eel.start("main.html", size=(650, 800)) # стартуем страницу с установленными настройками