from django.shortcuts import render
from .models import Update
import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect


def updates(request):
  items = Update.objects.all()
  #f = open('my_updates.py', 'w')
  #f.write("my_updates = [\n")
  #for i in items.iterator():
  #  f.write("[\"%s\", \"%s\"],\n" % (str(i.item), str(i.date_added)) )
  #f.write("]")
  #f.close()
  context = {'items': items}
  return render(request, 'updates/updates.html', context)


def add_item(request):
  if request.method == 'POST':
    item = request.POST.get('id_update')
    date_added = datetime.datetime.now()
    date_added = timezone.now()
    update = Update(item = item, date_added = date_added)
    update.save()
    return HttpResponseRedirect('/updates')
  return render(request, 'updates/add_item.html', {})


def update_item(request, item_id = None):
  item_to_update = Update.objects.filter(id = item_id).first()
  if request.method == "POST":
    item = request.POST.get('id_update')
    date_added = item_to_update.date_added
    update = Update(id=item_id, item=item, date_added=date_added)
    update.save()
    return HttpResponseRedirect('/updates')
  return render(request, 'updates/update_item.html', {'update': item_to_update})


def delete_item(request, item_id = None):
  item = Update.objects.filter(id = item_id).first()
  item.delete()
  return HttpResponseRedirect('/updates')


# using HTMX
def delete_update_item(request, item_id):
  # delete updated item from updates
  Update.objects.filter(id = item_id).first().delete()

  items = Update.objects.all()
  context = {'items': items}
  return render(request, 'updates/items.html', context)


def confirm_delete(request, item_id):
  item = Update.objects.filter(id = item_id).first()
  context = {'item' : item}
  return render(request, 'updates/confirm.html', context)
