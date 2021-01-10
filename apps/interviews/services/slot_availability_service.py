from datetime import datetime
from typing import List

from apps.interviews.exceptions import MaximumInterviewLimitReachedException, RecentBadInterviewsException, \
    NoInterviewSlotsAvailableException
from apps.interviews.models import Interview, InterviewerAvailability
from apps.interviews.services.interview_settings_service import InterviewSettingsService


class SlotAvailabilityService:
    def __init__(self, student_id: int):
        self.student_id = student_id
        self.existing_interviews = self.__get_interviews_for_student(student_id)

    def __validate(self) -> bool:
        """
        1. Check for interview limit reached
        2. Check if last `n` interviews have at least a grade of `m`
        :raises MaximumInterviewLimitReachedException, RecentBadInterviewsException
        :return:
        """
        settings_service = InterviewSettingsService()

        max_interview_limit = settings_service.get_max_mock_interviews()
        if len(self.existing_interviews) >= max_interview_limit:
            raise MaximumInterviewLimitReachedException(f'Completed {max_interview_limit} interviews already')

        if self.existing_interviews:
            interviews_to_check = settings_service.get_latest_interview_count_for_grade_check()
            min_grade_limit = settings_service.get_min_grade_for_interview_check()
            recent_grades = []
            checked_so_far = 0

            for interview in self.existing_interviews:
                if interview.is_completed:
                    checked_so_far += 1
                    recent_grades.append(interview.grade)
                    if checked_so_far >= interviews_to_check:
                        break

            if min(recent_grades) <= min_grade_limit:
                raise RecentBadInterviewsException('Recent interview performance has been bad, please contact support')

        return True

    def validate_and_get_slots(self, start_time: datetime, end_time: datetime):
        """
        :raises MaximumInterviewLimitReachedException, RecentBadInterviewsException, NoInterviewSlotsAvailableException
        :param start_time:
        :param end_time:
        :return:
        """
        self.__validate()
        slots = self.__get_slots(start_time, end_time)

        return slots

    @staticmethod
    def __get_interviews_for_student(student_id: int) -> List[Interview]:
        return Interview.objects.filter(student_id=student_id, is_cancelled=False).order_by('-end_time')

    def __get_slots(self, start_time: datetime, end_time: datetime):
        """
        :raises NoInterviewSlotsAvailableException
        :param start_time:
        :param end_time:
        :return:
        """
        exhausted_interviewer_list = []
        for interview in self.existing_interviews:
            exhausted_interviewer_list.append(interview.interviewer_id)

        available_slot_objs = InterviewerAvailability.objects \
            .filter(slot_start_time__lte=start_time, slot_end_time__gte=end_time) \
            .exclude(interviewer_id__in=exhausted_interviewer_list)

        if not available_slot_objs:
            raise NoInterviewSlotsAvailableException('No slots are available for given timings')

        available_slots = []
        for obj in available_slot_objs:
            available_slots.append(
                {
                    'interviewer_id': obj.interviewer_id,
                    'slot_start_time': obj.slot_start_time,
                    'slot_end_time': obj.slot_end_time
                }
            )

        return available_slots
