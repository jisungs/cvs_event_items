from django.shortcuts import render
from django.http import HttpResponse
import csv
from datetime import datetime
from .models import Product

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def index(request):
    
    # Product.objects.get(pk=1).delete()
    product_list = Product.objects.all().order_by('id')
    paginator = Paginator(product_list, 16)
    page = request.GET.get('page', 1)
    paged_products = paginator.get_page(page)
    # paged_products.adjusted_elided_pages = paginator.get_elided_page_range(page)
    try:
        paged_products.adjusted_elided_pages = paginator.get_elided_page_range(page)
    except (PageNotAnInteger, TypeError):
        paged_products = request.GET.get('page', 1)

    product_count = product_list.count()
    
    context = {
        'product_list':paged_products,
        'product_count':product_count,
    }

    return render(request, 'cvsmarket/index.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product_list = Product.objects.order_by('-created_data').filter(product_name__icontains=keyword)
            product_count = product_list.count()
    context = {
        'product_list':product_list,
        'product_count':product_count,
    }
    return render(request, 'cvsmarket/index.html', context)

def csv_reader(request):
    # with open("static/seven_event_item_3.csv") as fp:
    #     reader = csv.reader(fp, delimiter=",", quotechar='"')
    #     data_read = [row for row in reader]
    #     del data_read[0]
    #     print(data_read[1])
    #     for data in data_read:
    #        product = Product(market = data[0], product_name = data[1], img_url = data[2], price=data[3], event_type=data[4] , created_data=datetime.today().strftime('%Y-%m-%d'))
    #        try:
    #         product.save()
    #        except Exception as e:
    #         print(f"there was a problem to save {e}")
       
        # product_list = Product.objects.all()
        # for item in product_list:
        #     print(item)

    return HttpResponse('<h1>CSVREAder</h1>')