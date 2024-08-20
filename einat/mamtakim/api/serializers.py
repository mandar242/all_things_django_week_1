from rest_framework import serializers
from mamtakim_store.models import Mamtak

class MamtakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mamtak
        fields = '__all__'