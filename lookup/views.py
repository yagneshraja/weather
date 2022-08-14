from django.shortcuts import render,redirect


import json
import requests




def home(request):
    
    if request.method == 'POST':
        zip_code = request.POST['zipcode']

        # API for getting weather
        api_request =  requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zip_code+"&distance=5&API_KEY=32C193A7-4A58-4DBD-A11B-AC874CD67212")
        
        try:
            api = json.loads(api_request.content)
            print(api)
        except Execption as e:
            api = "Error"
       
        if api!='Error':
            if not api == []:
                if api[0]['Category']['Name'] == 'Good':
                    category_description = '(0-50) Air quality is considered to be satisfactory, and air pollution poses little or no risk'
                    category_color = 'good'
                elif api[0]['Category']['Name'] == 'Moderate' :
                    category_description = '(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern.'
                    category_color = 'good'
                elif api[0]['Category']['Name'] == 'Unhealthy' :
                    category_description = '(101-150)ne my begin to experience health effects....'
                    category_color = 'good'
                elif api[0]['Category']['Name'] == 'Very Unhealthy' :
                    category_description = '(151-200) Alert: Everyone will experience health issues...'
                    category_color = 'good'
                else: 
                    category_description = '(>200) Health w of emergency conditions' 
                    category_color = 'good'
                return render(request,'home.html',{'api':api,'category_description':category_description,'category_color':category_color})

                
            else: 
                api = 'Error'
                return render(request,'home.html',{'api':api})
        else:
            return render(request,'home.html',{'api':api})


       


    else:
        return render(request,'home.html')
        

        

def about(request):
    return render(request,'about.html',{})