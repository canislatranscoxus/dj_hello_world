from django.urls        import path
from my_app     import views


urlpatterns = [
    path( ''                , views.hello         ),
    path( 'hello/'          , views.hello         ),
    path( 'get_date_time/'  , views.get_date_time )

]
