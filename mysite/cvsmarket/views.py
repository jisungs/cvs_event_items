from django.shortcuts import render
from django.http import HttpResponse
import csv
# Create your views here.

def index(request):
    with open("static/event_item.csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
    item_list = []
    for data in data_read:
        item_dict = {}
        item_dict["itemName"] = data[0]
        item_dict["imgURL"] = data[1]
        item_dict["price"] = data[2]
        item_dict["event"] = data[3]
        item_list.append(item_dict)
    del item_list[0]
    context = {
        'items' : item_list,
    }

    return render(request, 'cvsmarket/index.html', context)
