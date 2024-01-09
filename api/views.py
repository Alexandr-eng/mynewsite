from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User, Warehouse, Product
from .serializers import UserSerializer, WarehouseSerializer, ProductSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WarehouseCreateView(generics.CreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SupplyProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.quantity += int(request.data.get('quantity'))
        instance.save()

        return Response(ProductSerializer(instance).data)

class RetrieveProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_quantity = int(request.data.get('quantity'))

        if instance.quantity >= requested_quantity:
            instance.quantity -= requested_quantity
            instance.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Requested quantity is not available")

        return Response(ProductSerializer(instance).data)


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


