from django.shortcuts import render
from django.http import HttpResponse
import csv
from datetime import datetime
from .models import Product
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

def csv_reader(request):
    with open("static/event_item.csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
        
        # print(data_read[1])
        # for data in data_read:
        #    product = Product(product_name = data[0], img_url = data[1], price=data[2], event_type=data[3] , created_data=datetime.today().strftime('%Y-%m-%d'))
        #    try:
        #     product.save()
        #    except Exception as e:
        #     print(f"there was a problem to save {e}")
       
        product_list = Product.objects.all()
        for item in product_list:
            print(item)

    return HttpResponse('<h1>CSVREAder</h1>')