#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022-04-07 21:03:43
import allure
import pytest
import time
from config.setting import ConfigHandler
from utils.readFilesUtils.get_yaml_data_analysis import CaseData
from utils.assertUtils.assertControl import Assert
from utils.requestsUtils.requestControl import RequestControl
from utils.mysqlUtils.mysqlControl import MysqlDB


TestData = CaseData(ConfigHandler.data_path + r'WorkApplyCenter/create_advert').case_process()


@allure.epic("Merit_管理后台")
@allure.feature("推荐位管理")
class TestCreateAdvert:

    @allure.story("推荐位新增")
    @pytest.mark.parametrize('in_data', TestData, ids=[i['detail'] for i in TestData])
    def test_create_advert(self, in_data, case_skip):
        """
        :param :
        :return:
        """

        res = RequestControl().http_request(in_data)
        Assert(in_data['assert']).assert_equality(response_data=res[0], sql_data=res[1])

    def teardown_class(self):
        mysql = MysqlDB()
        remark = "自动化测试" + time.strftime('%Y-%m-%d %X')
        update_sql = "UPDATE advert_position_info SET is_delete=1,remark='%s' WHERE position_name='123123' ORDER BY id DESC LIMIT 1" % remark
        mysql.execute(sql=update_sql)
        print("测试数据恢复方法是否可用")


if __name__ == '__main__':
    pytest.main(['test_create_advert.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
