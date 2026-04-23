from django.apps import apps
from django.core.checks import run_checks
from django.test import SimpleTestCase


class ModelCheckTests(SimpleTestCase):
    def test_core_models_have_no_system_check_errors(self):
        core_config = apps.get_app_config("core")
        errors = run_checks(app_configs=[core_config])
        self.assertEqual(errors, [])
