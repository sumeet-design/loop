from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import StoreStatusSerializer, BusinessHoursSerializer, StoreTimezoneSerializer
import uuid
# def report_gen():
    

# Data output requirement

# We want to output a report to the user that has the following schema

# `store_id, uptime_last_hour(in minutes), uptime_last_day(in hours), update_last_week(in hours), downtime_last_hour(in minutes), downtime_last_day(in hours), downtime_last_week(in hours)` 

# 1. Uptime and downtime should only include observations within business hours. 
# 2. You need to extrapolate uptime and downtime based on the periodic polls we have ingested, to the entire time interval.
#     1. eg, business hours for a store are 9 AM to 12 PM on Monday
#         1. we only have 2 observations for this store on a particular date (Monday) in our data at 10:14 AM and 11:15 AM
#         2. we need to fill the entire business hours interval with uptime and downtime from these 2 observations based on some sane interpolation logic

# Note: The data we have given is a static data set, so you can hard code the current timestamp to be the max timestamp among all the observations in the first CSV.
class TriggerReport(APIView):
    def get(self, request, format=None):
        # Implement logic to trigger report generation
        # Create a report_id and start generating the report
        # Return the report_id
        report_id = uuid.uuid4()  # Generate a random report ID here
        store_id = bussiness_hour.objects.all()[0].store_id
        print("this is store_id",store_id)
        get_store_status = store_status.objects.filter(store_id=store_id).values()
        print(get_store_status)
        return Response({"report_id": report_id}, status=status.HTTP_200_OK)

class GetReport(APIView):
    def get(self, request, report_id, format=None):
        # Implement logic to check report status and generate CSV
        # If report generation is complete, return the CSV
        # Otherwise, return "Running"
        report_status = "Complete"  # Replace with actual logic to check status
        if report_status == "Complete":
            # Generate CSV content here based on the report data
            csv_content = "store_id,uptime_last_hour,...\n1,120,24,..."
            response = Response(csv_content, content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="report.csv"'
            return response
        else:
            return Response("Running", status=status.HTTP_200_OK)
