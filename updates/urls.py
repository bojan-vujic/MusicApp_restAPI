from django.urls import path
from . import views

urlpatterns = [
  path('updates/', views.updates, name="updates"),
  path('updates/add_item/', views.add_item, name="add_item"),
  path('updates/update_item/<item_id>', views.update_item, name="update_item"),
  path('updates/delete_item/<item_id>', views.delete_item, name="delete_item"),
  path('updates/delete_update_item/<item_id>', views.delete_update_item, name="delete_update_item"),
  path('updates/confirm/<item_id>', views.confirm_delete, name="confirm_delete"),
]