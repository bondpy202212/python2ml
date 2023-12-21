import calendar


a = calendar.LocaleHTMLCalendar(locale='Usa_Usa')
with open('calendar.html', 'w') as g:
    print(a.formatyear(2022, width=3), file=g)
