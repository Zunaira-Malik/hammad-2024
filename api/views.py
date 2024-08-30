from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from urllib.parse import urlparse
from datetime import datetime
import socket
import ipaddress
from .models import Query  

def index(request):
    version = "1.0.1"
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    kubernetes = False
    return JsonResponse({'version': version, 'date': timestamp, 'kubernetes': kubernetes})


@api_view(['GET'])
def get_ipv4(request):
    domain = request.query_params.get('domain')
    if domain:
        try:
            parsed_url = urlparse(domain)
            hostname = parsed_url.hostname if parsed_url.hostname else domain
            ipv4 = socket.gethostbyname(hostname)

            Query.objects.create(
                domain=hostname,
                ipv4_addresses=[ipv4]
            )

            return Response({'domain': hostname, 'ipv4': ipv4})
        except socket.gaierror:
            return Response({'error': 'Invalid domain or domain not found'}, status=400)
    else:
        return Response({'error': 'Domain parameter is required'}, status=400)


@api_view(['GET'])
def validate_ipv4(request):
    ipv4 = request.query_params.get('ipv4')
    if ipv4:
        try:
            ipaddress.ip_address(ipv4)
            return Response({'ipv4': ipv4, 'valid': True})
        except ValueError:
            return Response({'ipv4': ipv4, 'valid': False, 'error': 'Invalid IPv4 address'}, status=400)
    else:
        return Response({'error': 'IPv4 parameter is required'}, status=400)


@api_view(['GET'])
def get_history(request):
    queries = Query.objects.all().order_by('-timestamp')[:20]
    
    query_list = [
        {
            'domain': query.domain,
            'ipv4_addresses': query.ipv4_addresses,
            'timestamp': query.timestamp
        }
        for query in queries
    ]
    
    return Response(query_list)