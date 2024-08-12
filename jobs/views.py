from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer
from .scheduler import schedule_job
from drf_spectacular.utils import extend_schema


@api_view(['GET'])
def jobs(request):
    """
    Get all scheduled Jobs.
    ---
    responses:
        200:
            description: A successful response,
        500:
            description: Internal server Error.
    """
    try:
        if request.method == 'GET':
            jobs = Job.objects.all()
            serializer = JobSerializer(jobs, many=True)
            return Response(serializer.data)
    except Exception as e:
        return Response(Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR))



@extend_schema(
    request=JobSerializer,  # Specify the request serializer
    responses={200: JobSerializer}  # Specify the response serializer
)
@api_view(['POST'])
def createJobs(request):
    """
    Create background Jobs.
    ---
    requestBody:
    required: true
    content:
        application/json:
        schema:
            type: object
    responses:
    201:
        description: Created
    400:
        description: Bad request
    500:
        description: Internal server error
    """
    # try:
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        job = serializer.save()
        
        # Schedule an email notification when a job is created
        schedule_job(job.id, job.schedule_type, job.schedule_details)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # except Exception as e:
    #     return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def job_detail(request, pk):
    """
    Get specific scheduled Job details with job id.
    ---
    responses:
        200:
            description: A successful response,
        404:
            description: Job not found.
    """
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)
