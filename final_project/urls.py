from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('final_project.common.urls')),
    path('book/', include('final_project.book.urls')),
    path('author/', include('final_project.author.urls')),
    path('account/', include('final_project.account.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

