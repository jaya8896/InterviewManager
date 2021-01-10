from apps.commons.settings_service import SettingsService
from apps.interviews.models import InterviewSettings


class InterviewSettingsService(SettingsService):

    def set_settings_model(self):
        self.settingsModel = InterviewSettings

    def get_max_mock_interviews(self) -> int:
        key = 'MAX_MOCK_INTERVIEWS_PER_STUDENT_KEY'
        return self.get_as_int(key, default=15)

    def get_latest_interview_count_for_grade_check(self) -> int:
        key = 'INTERVIEWS_FOR_GRADE_CHECK_KEY'
        return self.get_as_int(key, 2)

    def get_min_grade_for_interview_check(self) -> int:
        key = 'MIN_INTERVIEW_GRADE_KEY'
        return self.get_as_int(key, 1)
