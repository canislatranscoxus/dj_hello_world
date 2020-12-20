from django.urls    import path
from my_app         import views

app_name = 'my_app'
urlpatterns = [
    path( ''                , views.hello        , name= 'index' ),
    path( 'hello/'          , views.hello        , name= 'hello' ),
    path( 'get_date_time/'  , views.get_date_time, name= 'get_date_time' )

]
