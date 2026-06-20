import pytest
import allure

from config import settings
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

from tools.routes import AppRoute


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
class TestPositiveAuthorization:

    @allure.label("section2", "Positive")
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.authorization
    def test_positive_successful_authorization(
        self,
        login_page: LoginPage,
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
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(
            email=settings.test_user.email,
            password=settings.test_user.password,
        )
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

    @allure.label("section2", "Positive")
    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.positive
    @pytest.mark.regression
    @pytest.mark.authorization
    def test_positive_navigate_from_login_to_registration(
        self,
        login_page: LoginPage,
        registration_page: RegistrationPage,
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()
        registration_page.registration_form.check_visible(
            email="", username="", password=""
        )


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
class TestNegativeAuthorization:

    @allure.label("section2", "Negative")
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.negative
    @pytest.mark.regression
    @pytest.mark.authorization
    @pytest.mark.xdist_group(name="authorization-group")
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password"),
        ],
    )
    def test_negative_wrong_email_or_password(
        self, login_page: LoginPage, email: str, password: str
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()
