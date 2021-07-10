from django.urls import path
from . import views
urlpatterns = [
    path("<int:key>/", views.abc),
    path("company/", views.ListCompany),
    path("company/<int:key>/", views.DetailCompany),
    path("company/Create/", views.CreateCompany),
    path("company/Update/<int:key>/", views.UpdateCompany),
    path("company/Delete/<int:key>/", views.DeleteCompany),
    path("product/", views.ListProduct),
    path("product/<int:key>/", views.DetailProduct),
    path("product/Create/", views.CreateProduct),
    path("product/Update/<int:key>/", views.UpdateProduct),
    path("product/Delete/<int:key>/", views.DeleteProduct)


]
