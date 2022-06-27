from app_data.views import Form_Presidente_View, Form_Ministro_View, Form_Partido_View
from django.urls import path

urlpatterns = [
    path('reg_pres/', Form_Presidente_View.register_president, name='presidente'),
    path('sav_pres/', Form_Presidente_View.check_info_president, name='savePresidente'),
    path('reg_min/', Form_Ministro_View.register_minister, name='ministro'),
    path('sav_min/', Form_Ministro_View.check_info_minister ,name='saveMinistro'),
    path('reg_par/', Form_Partido_View.register_party, name='partido'),
    path('sav_par/', Form_Partido_View.check_info_party, name='savePartido'),
    path('sea_pres/', Form_Presidente_View.search_president, name='buscarpresidente'),
    path('sea_min/', Form_Ministro_View.search_ministro, name='buscarministro'),
    path('sea_par/', Form_Partido_View.search_partido, name='buscarpartido'),
]