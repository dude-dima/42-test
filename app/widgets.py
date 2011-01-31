from django import forms


class JQCalendarWidget(forms.DateInput):

    class Media:
        css = {
            'all': (
                "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/themes\
/ui-lightness/jquery-ui.css",
            )}
        js = (
            '/js/jquery.ui.min.js',
            "/js/jquery.ui.datepicker.ru.js",
            '/js/calendar.js',
        )
