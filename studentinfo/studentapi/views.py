from django.shortcuts import render
from rest_framework import generics, permissions
from .models import studentmd
from .forms import CreateUserform
from django.contrib.auth.forms import UserCreationForm
from .serializers import studentserializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

res = 'Student'

def index(request):
	form = CreateUserform()
	global res
	if request.method == 'POST':
		form = CreateUserform(request.POST)
		if form.is_valid():
			res = request.POST.get('inputGroupSelect01','') 
			print(res)

			form.save()
	context = {'form':form}
	return render(request,'studentapi/index.html',context);



class stdlist(generics.ListCreateAPIView):
	queryset = studentmd.objects.all()
	serializer_class = studentserializer
	if res == 'Student':

		permission_classes = [permissions.IsAuthenticatedOrReadOnly]
		authentication_classes = [JWTAuthentication]

	elif res == 'Teacher':
		permission_classes = [permissions.IsAuthenticated]
		authentication_classes = [JWTAuthentication]

class stdalter(generics.RetrieveUpdateDestroyAPIView):
	queryset = studentmd.objects.all()
	serializer_class = studentserializer
	permission_classes = [permissions.IsAuthenticated]