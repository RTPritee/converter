import csv
import json
from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     return render(request, "home.html")

def home(request):
    if request.method == "POST" and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        data = json.load(uploaded_file)

        # to handle missing values and convert to CSV file
        csv_data = []
        headers = ['balance', 'debit', 'credit', 'transaction_details', 'gregorian_date'] # provided columns
        csv_data.append(headers)

        for i in range(len(data['balance'])):
            row = [
                data['balance'][i].get('value', 'unknown'),  #for missing value using unknown
                data['debit'][i].get('value', 'unknown') if i < len(data['debit']) else 'unknown',
                data['credit'][i].get('value', 'unknown') if i < len(data['credit']) else 'unknown',
                data['transaction_details'][i].get('value', 'unknown') if i < len(data['transaction_details']) else 'unknown',
                data['gregorian_date'][i].get('value', 'unknown') if i < len(data['gregorian_date']) else 'unknown'
            ]
            csv_data.append(row)

        # create CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="output.csv"'
        writer = csv.writer(response)
        writer.writerows(csv_data)
        return response

    return render(request, 'home.html')

def convert_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")

        response = request.post(
            "http://127.0.0.1:8000/convert",  # api end point from the fastAPI part
            files={"file": uploaded_file},
        )

        if response.status_code == 200:   # successfull 
            csv_file = response.content
            response = HttpResponse(csv_file, content_type="text/csv")
            response["Content"] = "attachment; filename=output.csv"
            return response

        return HttpResponse("Error during conversion", status=400)
    return HttpResponse("Invalid request", status=400)
