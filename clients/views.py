from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client, Investment
from .serializers import ClientSerializer, InvestmentSerializer


class ClientCreateView(APIView):

    def get(self, request):
        clients = Client.objects.all()
        paginator = PageNumberPagination()
        paginated_clients = paginator.paginate_queryset(clients, request)
        serializer = ClientSerializer(paginated_clients, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvestCreateView(APIView):
    def get(self, request, client_id):
        """
        Возвращает все записи Investment для конкретного пользователя.
        """
        investments = Investment.objects.filter(client_id=client_id)
        paginator = PageNumberPagination()
        paginated_investments = paginator.paginate_queryset(investments, request)
        serializer = InvestmentSerializer(paginated_investments, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, client_id):
        """
        Добавляет новую запись Investment для конкретного пользователя.
        """
        data = request.data
        data['client'] = client_id
        serializer = InvestmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
