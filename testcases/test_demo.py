import pytest
import softest as softest

from pages.productrequest import ProductRequest
from utilities.utils import Utils
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestDemo(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.request = ProductRequest(self.driver)
        self.utils = Utils()

    @data(*Utils.read_data_from_excel("C:\\Users\\Dhanush\\PycharmProjects\\Automation\\testdata\\testdata.xlsx", "data"))
    @unpack
    def test_demo_a(self, name, email, ph_no):
        actual = self.request.enter_data(name, email, ph_no)
        self.soft_assert(self.assertEqual, "partnerName", actual)
        self.assert_all()

    def test_demo_b(self):
        actual = self.request.enter_data("dd", "ddd", "987")
        self.soft_assert(self.assertEqual, "partnerName1", actual)
        self.assert_all()