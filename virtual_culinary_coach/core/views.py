# views.py
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import MealPlan, CoachingSession, User  # Import User from your models
from .serializers import MealPlanSerializer, CoachingSessionSerializer
from django.http import HttpResponse

class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

class CoachingSessionViewSet(viewsets.ModelViewSet):
    queryset = CoachingSession.objects.all()
    serializer_class = CoachingSessionSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response(
                {'error': 'Please provide both email and password'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Check if user already exists
        if User.objects.filter(email=email).exists():
            return Response(
                {'error': 'User with this email already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Create user using the custom User model
        user = User.objects.create_user(
            email=email,
            password=password,
            username=email  # Since you're using email as username
        )
        
        # Generate tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'email': user.email,
                'id': user.id
            }
        }, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

def home(request):
    return HttpResponse("Welcome to the Virtual Culinary Coach!")