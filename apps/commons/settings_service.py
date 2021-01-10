import datetime
import json
from abc import ABC

from django.core.exceptions import ObjectDoesNotExist


class SettingsService(ABC):
    TRUE_STRINGS = ['True', '1']
    settingsModel = None

    def __init__(self):
        self.set_settings_model()

    def set_settings_model(self):
        raise NotImplementedError('`set_settings_model()` must be implemented.')

    def __fetch_value(self, key):
        try:
            setting = self.settingsModel.objects.get(key=key)
            value = setting.value
        except ObjectDoesNotExist:
            return None
        except AttributeError:
            return None

        return value

    def set_value(self, key: str, value: str):
        if not type(value) == str:
            raise TypeError(
                "Invalid type for value. Expected: str. Got: %(type)s. ToString method won't be used here" %
                {"type": type(value)})

        try:
            entry = self.settingsModel.objects.get(key=key)
        except ObjectDoesNotExist:
            entry = self.settingsModel()
            entry.key = key

        entry.value = value
        entry.save()

    def del_key(self, key: str):
        self.settingsModel.objects.filter(key=key).delete()

    def get_as_string(self, key, default=None):
        value = self.__fetch_value(key)
        if value:
            return value

        return default

    def get_as_float(self, key, default=None):
        value = self.__fetch_value(key)
        if value:
            try:
                value = float(value)
            except ValueError:
                value = default

            return value

        return default

    def get_as_int(self, key, default=None):
        value = self.__fetch_value(key)
        if value:
            try:
                value = int(value)
            except ValueError:
                value = default

            return value

        return default

    def get_as_bool(self, key, default=None):
        value = self.__fetch_value(key)
        if value:
            if value in self.TRUE_STRINGS:
                return True
            else:
                return False

        return default

    def get_as_json(self, key, default=None):
        value = self.__fetch_value(key)
        if value:
            try:
                value = json.loads(value)
            except json.decoder.JSONDecodeError:
                value = default

            return value

        return default

    def get_as_date(self, key, datefmt, default=None):
        value = self.__fetch_value(key)
        if value:
            try:
                value = datetime.datetime.strptime(value, datefmt).date()
            except ValueError:
                value = default

            return value

        return default

    def get_as_datetime(self, key, datetimefmt, default=None):
        value = self.__fetch_value(key)
        if value:
            try:
                value = datetime.datetime.strptime(value, datetimefmt)
            except ValueError:
                value = default

            return value

        return default

    def get_as_timedelta(self, key, default=None):
        value = self.__fetch_value(key)

        if value:
            try:
                value = datetime.timedelta(seconds=int(value))
            except TypeError:
                value = default

            return value

        return default

    def get_as_time(self, key: str, timefmt: str, default: datetime.time = None) -> datetime.time:
        value = self.__fetch_value(key)
        if value:
            try:
                value = datetime.datetime.strptime(value, timefmt).time()
            except ValueError:
                value = default

            return value

        return default
