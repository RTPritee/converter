import os
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

# Login feature: Handle user login and authentication
def user_login(request):
    if request.method == "POST":
        # Get the submitted username and password from the form
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # If authentication is successful, log the user in
            return redirect('landing')  # Redirect to landing page after successful login
        else:
            return HttpResponse("Invalid login credentials", status=401)  # If authentication fails, return error

    return render(request, "login.html") 

# Logout feature
def user_logout(request):
    logout(request) 
    return redirect('login') 

# Landing page -Accessible only to logged-in users
@login_required
def landing(request):
    return render(request, "landing.html") 


# Convert file using FastAPI: Sends the file to a FastAPI endpoint for conversion

@login_required
def file_upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")
        if not uploaded_file:
            return JsonResponse({"error": "No file uploaded"}, status=400)

        try:
            # Send the file to the FastAPI endpoint for conversion
            response = requests.post(
                "http://127.0.0.1:8000/convert",
                files={"file": uploaded_file},
            )

            # If FastAPI successfully converts the file
            if response.status_code == 200:
                # ensuring the media directory exists
                if not os.path.exists(settings.MEDIA_ROOT):
                    os.makedirs(settings.MEDIA_ROOT)

                # Saving the converted CSV temporarily
                csv_file_path = os.path.join(settings.MEDIA_ROOT, "converted_output.csv")
                with open(csv_file_path, "wb") as csv_file:
                    csv_file.write(response.content)

                # Return success message with download flag
                return JsonResponse({"message": "File converted successfully", "download": True})

            # Handle FastAPI errors
            return JsonResponse({"error": f"FastAPI error: {response.text}"}, status=response.status_code)

        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": f"Communication error with FastAPI: {str(e)}"}, status=500)

    return render(request, "file_upload.html")

@login_required
def download_csv(request):
    # Path to the converted CSV file
    csv_file_path = os.path.join(settings.MEDIA_ROOT, "converted_output.csv")

    # Checking if the file exists
    if not os.path.exists(csv_file_path):
        return HttpResponse("No converted file available for download", status=404)

    # Serve the file as a downloadable response
    with open(csv_file_path, "rb") as csv_file:
        response = HttpResponse(csv_file, content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=converted_output.csv"
        return response

