# Подсчет действий на Facebook

Данный скрипт позволяет извлечь из HTML-файла с Журналом действий Facebook даты
и количество действий, которые были произведены пользователем в указанный день.

Для использования скрипта зайдите на страницу Журнала действий:

[https://www.facebook.com/[имя пользователя]/allactivity](#)

Пролистайте страницу вниз до нужного Вам периода (для выполнения всех необходимых
AJAX-запросов). Скопируйте все содержимое страницы в Web Inspector и сохраните его
в отдельный файл с данным скриптом.

Далее воспользуйтесь командой:

facebook_extract.py "имя HTML файла" "имя файла вывода"