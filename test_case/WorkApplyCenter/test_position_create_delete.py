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


TestData = CaseData(ConfigHandler.data_path + r'WorkApplyCenter/position_create_delete').case_process()


@allure.epic("Merit_管理后台")
@allure.feature("推荐位管理")
class TestPositionCreateDelete:

    @allure.story("推荐位内容增删")
    @pytest.mark.parametrize('in_data', TestData, ids=[i['detail'] for i in TestData])
    def test_position_create_delete(self, in_data, case_skip):
        """
        :param :
        :return:
        """

        res = RequestControl().http_request(in_data)
        Assert(in_data['assert']).assert_equality(response_data=res[0], sql_data=res[1])

    def teardown_class(self):
        """
        数据恢复
        :return:
        """
        mysql = MysqlDB()
        remark = "自动化测试" + time.strftime('%Y-%m-%d %X')
        update_sql_1 = "UPDATE advert SET is_delete=1,remark='%s' WHERE title='自动化测试数据' ORDER BY id DESC LIMIT 1" % remark
        update_sql_2 = "UPDATE advert SET is_delete=0,remark='%s' WHERE id=59" % remark
        mysql.execute(sql=update_sql_1)
        mysql.execute(sql=update_sql_2)
        print("测试数据恢复")


if __name__ == '__main__':
    pytest.main(['test_position_create_delete.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
