from django.conf.urls import patterns, url

from form import views

urlpatterns = patterns('',
    url(r'^upload.html',
                'form.views.upload_file', name='upload file'),
)
