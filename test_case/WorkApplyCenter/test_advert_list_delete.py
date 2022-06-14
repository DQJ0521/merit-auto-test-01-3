import time
import allure
import pytest
from config.setting import ConfigHandler
from utils.readFilesUtils.get_yaml_data_analysis import CaseData
from utils.assertUtils.assertControl import Assert
from utils.requestsUtils.requestControl import RequestControl
from utils.mysqlUtils.mysqlControl import MysqlDB

TestData = CaseData(ConfigHandler.data_path + r'WorkApplyCenter/advert_list_delete').case_process()


@allure.epic("Merit_管理后台")
@allure.feature("推荐位管理")
class TestSupApplyList:

    @allure.story("推荐位列表")
    @pytest.mark.parametrize('in_data', TestData, ids=[i['detail'] for i in TestData])
    def test_advert_list_delete(self, in_data, case_skip):
        """
        :param :
        :return:
        """

        res = RequestControl().http_request(in_data)
        Assert(in_data['assert']).assert_equality(response_data=res[0], sql_data=res[1])

    def teardown_class(self):
        mysql = MysqlDB()
        remark = "自动化测试" + time.strftime('%Y-%m-%d %X')
        update_sql = "UPDATE advert_position_info SET is_delete=0,remark='%s' WHERE id=13" % remark
        mysql.execute(sql=update_sql)
        print("测试数据恢复方法是否可用")


if __name__ == '__main__':
    pytest.main(['test_advert_list_delete.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
