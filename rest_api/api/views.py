from .models import Record
from .serializers import RecordSerializer
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
def landing_page(request):
    return render(request, 'home.html')


@api_view(['GET'])
def get_records(request):
    # Check if records already exist in the database
    if Record.objects.exists():
        # Retrieve all records from the database
        records = Record.objects.all()
    else:
        # Load records from the CSV file (assuming the CSV file path is known)
        csv_file_path = 'C:\\Users\\somay\\OneDrive\\Documents\\st_test\\cleaned_data.csv'  # Replace with the actual path
        Record.load_from_csv(csv_file_path)
        # Retrieve all records from the database (including newly loaded ones)
        records = Record.objects.all()

    # Serialize the records using the RecordSerializer
    serializer = RecordSerializer(records, many=True)

    # Return the serialized data
    # return Response(serializer.data)
    return render(request, "get_records.html", {"records": serializer.data})

@csrf_exempt
# @api_view(["POST"])
def filter_records(request):
    # return Response(data=data, status=status.HTTP_200_OK)
    return render(request, "filter_records.html")

@csrf_exempt
def show_result(request):
    min_price = request.POST["min_price"]
    max_price = request.POST["max_price"]
    records = Record.objects.filter(price__gte=min_price, price__lte=max_price)
    serializer = RecordSerializer(records, many=True)
    data = serializer.data
    return render(request, "show_result.html", {"records_data": data})


@csrf_exempt
# @api_view(["POST"])
def insert_record(request):
        return render(request, 'insert_record.html')


# @csrf_exempt
# @api_view(["POST"])
def record_inserted(request):
    keys = ['id', 'name', 'price', 'quantity', 'category']
    print([request.POST.get(key) for key in keys])
    data = [request.POST.get(key) for key in keys]
    serializer = RecordSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
