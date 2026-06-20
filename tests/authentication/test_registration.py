import pytest
import allure

from config import settings
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity

from tools.routes import AppRoute


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
class TestPositiveRegistration:

    @allure.label("section2", "Positive")
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.registration
    @pytest.mark.xdist_group(name="authorization-group")
    def test_positive_successful_registration(
        self,
        dashboard_page: DashboardPage,
        registration_page: RegistrationPage,
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password,
        )
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
