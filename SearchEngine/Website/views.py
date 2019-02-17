from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .form import searchForm
from .json_reader import Json_Reader
from .Products import Product
from .firebase_loader import firebase_loader

class HomeView(TemplateView):
    template_name = 'webs/index.html'

    def get(self, request):
        form = searchForm()

        args = {
                'form': form
            }

        return render(request, self.template_name, args)

    def post(self, request):
        form = searchForm(request.POST)
        json = Json_Reader()
        products = []

        # data = json.read_file()

        if form.is_valid():
            text = form.cleaned_data['Search']
        
        firebase_loader.initiate(self)
        data = firebase_loader.makeQuery(self,text)

        for product in data:
            print((data[product] ," --\n"))
            title = None
            brand = None
            feature = None
            price = None
            image = None
            if 'title' in data[product]:
                title = data[product]['title']
            
            if(title):
                if text.lower() in title.lower():
                    title = data[product]['title']
                    asin = data[product]['asin']
                    if 'brand' in data[product]:
                        brand = data[product]['brand']
                    if 'feature' in data[product]:
                        feature = data[product]['feature']
                    if 'price' in data[product]:
                        price = data[product]['price']
                    if 'Image' in data[product]:
                        image = data[product]['Image']
                    # if 'catagories' in data[product]:
                    #     categories = product['catagories']
                    categories = "catagory"

                    product = Product(asin, title, brand, feature, price, image, categories)
                    products.append(product)
        args = {
            'form': form,
            'text': text,
            'data': data, 
            'products': products,
        }

        return render(request, self.template_name, args)