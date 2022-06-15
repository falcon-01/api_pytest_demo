import pytest
import requests
from time import sleep
from api.template_api import TemplateAPI
from tools.get_log import GetLog
from tools.read_file import read_json
import allure


log = GetLog.get_log()


@allure.feature('test template')
class TestTemplate:
    session = None

    @classmethod
    def setup_class(cls):
        cls.session = requests.Session()  # initialize session object
        cls.template = TemplateAPI()

    @classmethod
    def teardown_class(cls):
        cls.session.close()

    @classmethod
    def setup(cls):
        sleep(1.5)

    @allure.story("template_add")
    # @pytest.mark.skip
    @pytest.mark.parametrize(("url", "headers", "body", "expect"), read_json("test_add"))
    def test_add(self, url, headers, body, expect):
        response = self.template.api_add(self.session, url, headers, body)
        log.info("add function-status_code is: {}".format(response.status_code))
        assert response.status_code == expect, "status code validation failure"

    @allure.story("template_update")
    # @pytest.mark.skip
    @pytest.mark.parametrize(("url", "headers", "body", "expect"), read_json("test_update"))
    def test_update(self, url, headers, body, expect):
        response = self.template.api_update(self.session, url, headers, body)
        log.info("update function-status_code is: {}".format(response.status_code))
        assert response.status_code == expect, "status code validation failure"

    @allure.story("template_get")
    @pytest.mark.parametrize(("url", "headers", "params", "expect"), read_json("test_get"))
    def test_get(self, url, headers, params, expect):
        response = self.template.api_get(self.session, url, headers, params)
        log.info("get function-status_code is: {}".format(response.status_code))
        assert response.status_code == expect, "status code validation failure"

    @allure.story("template_delete")
    # @pytest.mark.skip
    @pytest.mark.parametrize(("url", "headers", "uid", "expect"), read_json("test_delete"))
    def test_delete(self, url, uid, headers, expect):
        response = self.template.api_delete(self.session, url, headers, uid)
        log.info("delete function-status_code is: {}".format(response.status_code))
        assert response.status_code == expect, "status code validation failure"
