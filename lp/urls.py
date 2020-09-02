from django.conf.urls import url, include
from . import views as lpviews



urlpatterns =[


            url(r'^$', lpviews.index, name='index'),
            url(r'^thanks$', lpviews.thanks, name='thanks'),
                    

    ]





