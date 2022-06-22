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

TestData = CaseData(ConfigHandler.data_path + r'WorkApplyCenter/tag_list_edit').case_process()


@allure.epic("Merit_管理后台")
@allure.feature("标签管理")
class TestPositionCreateDelete:

    @allure.story("标签改查")
    @pytest.mark.parametrize('in_data', TestData, ids=[i['detail'] for i in TestData])
    def test_tag_list_edit(self, in_data, case_skip):
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
        update_sql_2 = "UPDATE tag SET tag_name='自动化编辑数据',remark='%s' WHERE id=14" % remark
        mysql.execute(sql=update_sql_2)
        print("测试数据恢复")


if __name__ == '__main__':
    pytest.main(['test_tag_list_edit.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
