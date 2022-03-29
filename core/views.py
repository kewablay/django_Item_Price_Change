from django.shortcuts import render
from django.views import View
import pandas as pd
from core.models import Product
from django.core.paginator import Paginator


#The Home view 
class Home(View):
    #Get the request of the page
    def get(self, request):
        reader = pd.read_csv("core/templates/rice_beef_coffee_price_changes.csv") # read the data from csv file
        for _, row in reader.iterrows():
            new_file = Product(
                year = row['Year'],
                month = row['Month'],
                price_beef_kilo = row['Price_beef_kilo'],
                price_rice_kilo = row['Price_rice_kilo'],
                price_coffee_kilo = row['Price_coffee_kilo'],
                inflation_rate = row['Inflation_rate']
            )
            new_file.save()
        items = Product.objects.all() # get all the data in Product model
        paginator = Paginator(items, 50) # Show 50 items info per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'index.html', {'page_obj':page_obj})
        
        
        
