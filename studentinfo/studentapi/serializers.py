from rest_framework import serializers
from .models import studentmd

class studentserializer(serializers.ModelSerializer):
	class Meta:
		model = studentmd
		fields = ['id','stdname','stdclass','stdrollno']

		