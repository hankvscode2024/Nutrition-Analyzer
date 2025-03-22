from django.shortcuts import render
import requests,json

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'TiZJZvHH9BEfmKL0T1Z/VA==p5y8o6SfMrhHNhEv'})
        
        try:
            api=json.loads(response.content)
            items = api.get("items", []) 
            # print(response.content)
        except Exception as e:
            items = "Error...Error...Error"
   
        return render(request, 'index.html',{'api':items})
    
    else:
        return render(request, 'index.html',{'query':'Enter a valid Food Item'})
    
