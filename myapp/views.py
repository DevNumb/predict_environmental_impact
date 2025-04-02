from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

def upload_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        try:
            # Read the Excel file into a pandas DataFrame
            df = pd.read_excel(excel_file)
            
            # Convert the DataFrame to an HTML table
            excel_table = df.to_html(classes='table table-striped table-bordered', index=False)

            # Render the template and pass the table data
            return render(request, 'upload.html', {'excel_table': excel_table})
        except Exception as e:
            return HttpResponse(f"Error reading the Excel file: {e}")
    
    # If the request is a GET request, just render the upload form
    return render(request, 'upload.html')
