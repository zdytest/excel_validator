import BaseValidator
from datetime import datetime

class DateTimeValidator(BaseValidator.BaseValidator):

    message = "This value is not valid datetime"
    format = "%Y-%m-%d"

    def validate(self, value):

        #possible null values
        if value is None:

            return True

        value = super(DateTimeValidator, self).validate(value)

        if type(value) is datetime:
            value = value.strftime(self.format)

        try:
            if type(value) is unicode or type(value) is str:
                datetime.strptime(value, self.format)

                return True

        except ValueError:

            return False

        return False

    def __init__(self, params):
        super(DateTimeValidator, self).__init__(params)
