from schemas import LeaseSchema
from datetime import datetime
from tests.time import Time


class TestLeaseValidations:
    def test_dateTimeStart_is_required(self):
        validation_errors = LeaseSchema().validate({})

        assert 'dateTimeStart' in validation_errors

    def test_dateTimeStart_validates_valid_format(self):
        validation_errors = LeaseSchema().validate(
            {'dateTimeStart': Time.today()}
        )

        assert 'dateTimeStart' not in validation_errors

    def test_dateTimeStart_with_invalid_format(self):
        validation_errors = LeaseSchema().validate(
            {'dateTimeStart': Time.format_date_by_year(datetime.now())}
        )

        assert 'dateTimeStart' in validation_errors

    def test_dateTimeEnd_is_required(self):
        validation_errors = LeaseSchema().validate({})

        assert 'dateTimeEnd' in validation_errors

    def test_dateTimeEnd_validates_valid_date_format(self):
        validation_errors = LeaseSchema().validate(
            {'dateTimeEnd': Time.today()}
        )

        assert 'dateTimeEnd' not in validation_errors

    def test_dateTimeEnd_with_invalid_date_format(self):
        validation_errors = LeaseSchema().validate(
            {'dateTimeEnd': Time.format_date_by_year(datetime.now())}
        )

        assert 'dateTimeEnd' in validation_errors

    def test_created_at_is_dump_only(self):
        validation_errors = LeaseSchema().validate(
            {'created_at': Time.format_date_by_year(datetime.now())}
        )

        assert 'created_at' in validation_errors

    def test_updated_at_is_dump_only(self):
        validation_errors = LeaseSchema().validate(
            {'updated_at': Time.format_date_by_year(datetime.now())}
        )

        assert 'updated_at' in validation_errors

    def test_tenantID_is_required(self):
        validation_errors = LeaseSchema().validate({})

        assert 'tenantID' in validation_errors