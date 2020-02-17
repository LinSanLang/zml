
from django.conf.urls import url
from django.http import FileResponse
def load(request,filename):
    return FileResponse(open(filename, "rb"), content_type="application/msword", filename=filename,
                 as_attachment=True)

app_name = 'download'
urlpatterns = [
    url(r'^(.*?)/$',load)
]