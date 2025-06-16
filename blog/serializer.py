from crud.blog.models import CustomerReportRecord
from crud.employee import serializers




class CustomerReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerReportRecord