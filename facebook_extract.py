#!/usr/bin/python
# -*- coding: utf8 -*-py

# Импорт необходимых библиотек

import string
from datetime import date, timedelta
import re
import html5lib
import argparse

# Задаем параметры для работы с командной строки

parser = argparse.ArgumentParser(description='Извлечение количества действий на Facebook' + \
                                 ' со страницы Журнала действий.')
parser.add_argument('inFile', metavar='I', type=str, nargs='?',
                   help='Имя HTML-файла с журналом действий')
parser.add_argument('outFile', metavar='O', type=str, nargs='?',
                   help='Имя CSV-файла с результатом', default = "result.csv")

args = parser.parse_args()

filename = args.inFile
output = args.outFile
textOutput = "value,date\n"

# Пользовательская функция для чтения даты

def date_convert(text):
    if text == u"Сегодня":
        d = str(date.today())
    elif text == u"Вчера":
        d = str(date.today()- timedelta(1))
    else:
        text = text.replace(u" Январь","-01-").\
        replace(u" Февраль","-02-").\
        replace(u" Март","-03-").\
        replace(u" Апрель","-04-").\
        replace(u" Май","-05-").\
        replace(u" Июнь","-06-").\
        replace(u" Июль","-07-").\
        replace(u" Август","-08-").\
        replace(u" Сентябрь","-09-").\
        replace(u" Октябрь","-10-").\
        replace(u" Ноябрь","-11-").\
        replace(u" Декабрь","-12-")
        text += "2014"
        result = re.search("(\d{1,2})\-(\d{2})\-(\d{4})", text)
        day = result.group(1)
        month = result.group(2)
        year = result.group(3)
        if len(day) == 1:
            day = "0" + day
        d = year + "-" + month + "-" + day
    
    return d

# Работа с HTML-файлом

with open(filename,"r") as f:
    text = f.read()

preprocessed_text = html5lib.parse(text, treebuilder='lxml',\
    namespaceHTMLElements=False)

# Первый класс содержит дату событий, второй - само событие

xpath_pattern = '//div[@class="pam _5ep8 uiBoxWhite bottomborder"' + \
    ' or @class="pam _5shk uiBoxWhite bottomborder"]'

divs = preprocessed_text.xpath(xpath_pattern)

counter = 0
for i in divs:
    if (i.get('class') == "pam _5ep8 uiBoxWhite bottomborder"):
        if counter == 0:
            d = date_convert(i.text)
        else:
            textOutput += str(counter) + "," + d + "\n"
            d = date_convert(i.text)
            counter = 0
    else:
        counter+=1

textOutput += str(counter) + "," + d

# Вывод файла

with open(output,"w") as f:
    f.write(textOutput)