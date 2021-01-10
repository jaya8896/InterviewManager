from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from apps.interviews.exceptions import MaximumInterviewLimitReachedException, RecentBadInterviewsException, \
    NoInterviewSlotsAvailableException
from apps.interviews.serializers import AvailableInterviewSlotsSerializers
from apps.interviews.services.slot_availability_service import SlotAvailabilityService


class AvailableInterviewSlotsView(APIView):
    http_method_names = ['get', ]

    permission_classes = []

    def get(self, request):
        serializer = AvailableInterviewSlotsSerializers(data=request.GET)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        student_id = request.GET['studentId']
        start_time = request.GET['startDateTime']
        end_time = request.GET['endDateTime']

        service = SlotAvailabilityService(student_id)
        try:
            response = service.validate_and_get_slots(start_time, end_time)
        except (
                MaximumInterviewLimitReachedException,
                RecentBadInterviewsException,
                NoInterviewSlotsAvailableException
        ) as e:
            return Response(str(e), status=HTTP_400_BAD_REQUEST)

        return Response(response)
