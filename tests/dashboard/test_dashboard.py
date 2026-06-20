import pytest
import allure
from allure_commons.types import Severity

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.routes import AppRoute


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.tag(AllureTag.REGISTRATION, AllureTag.DASHBOARD)
class TestPositiveDashboard:

    @allure.label("section2", "Positive")
    @allure.title("Check displaying of dashboard page")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.positive
    @pytest.mark.dashboard
    @pytest.mark.regression
    def test_positive_dashboard_displaying(
        self, dashboard_page_with_state: DashboardPage
    ):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_activities_chart()
