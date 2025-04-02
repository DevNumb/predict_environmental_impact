from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
def home(request):
    return HttpResponse("Hello, Django!")




def upload_excel(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        
        # Read the Excel file
        df = pd.read_excel(file)
        
        # Display first few rows (for debugging)
        print(df.head())
        
        return render(request, "upload.html", {"message": "File uploaded successfully!"})

    return render(request, "upload.html")
