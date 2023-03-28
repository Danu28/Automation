import pytest
import softest as softest
from pages.loginpage import LoginPage
from utilities.utils import Utils
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestLoginPage(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login_page = LoginPage(self.driver)
        self.utils = Utils()

    @data(*Utils.read_data_from_excel("testdata/testdata.xlsx", "login_page"))
    @unpack
    def test_validate_user(self, username, password):
        actual = self.login_page.validate_user(username, password)
        self.soft_assert(self.assertEqual, True, actual)
        self.assert_all()
