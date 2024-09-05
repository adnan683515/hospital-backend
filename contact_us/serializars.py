from rest_framework import serializers
from .models import ContactUs

#serializers: python ar complex object json a convert korar jonno serializers user kora hoi
# json mean 'key': 'value'  pair

#complex obj -> json 


class ContactUsserializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
        