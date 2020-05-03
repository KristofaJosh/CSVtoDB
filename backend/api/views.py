from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ZenoSerializer
from .models import ZenoModel, GetRequestActivityLog
import pandas as pd


# Create your views here.
class ZenoViewSet(viewsets.ModelViewSet):
    queryset = ZenoModel.objects.all()
    serializer_class = ZenoSerializer

    @action(detail=False, methods=['PATCH'])
    def translate_data(self, request):
        file_obj = request.data['file']

        try:
            csv_data = pd.read_csv(file_obj)
            dataframe = pd.DataFrame(csv_data,
                                     columns=['id', 'timestamp', 'temperature', 'duration'])
            for row in dataframe.itertuples():
                if ZenoModel.objects.filter(csv_id=row.id).exists():
                    pass
                else:
                    fields = {'csv_id': row.id, 'csv_timestamp': row.timestamp,
                              'csv_temperature': row.temperature,
                              'csv_duration': row.duration}

                    data_serializer = ZenoSerializer(data=fields)
                    if data_serializer.is_valid():
                        data_serializer.save()

            response = {'message': 'data written to database'}
            return Response(response, status=status.HTTP_201_CREATED)

        except:
            response = {'message': 'make sure file is of right format'}
            return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(detail=False, methods=['DELETE'])
    def remove_data(self, request):
        destroy = ZenoModel.objects.all()
        destroy.delete()
        response = {'message': 'Database emptied!'}
        return Response(response, status=status.HTTP_200_OK)
