import pytest

from api_cematpshop_excel.api.api import Api
from api_cematpshop_excel.tools.common_assert import common_assert
from api_cematpshop_excel.tools.file_tool import FileTool
import allure
from api_cematpshop_excel.tools.get_log import GetLog
log = GetLog.get_logger()
@allure.feature("订单模块")
@allure.issue("http://www.baidu.com", name="issue_url")
@allure.link("http://www.baidu.com", name="link_url")
@allure.testcase("http://www.baidu.com", name="testcase_url")
@allure.description("登录--获取商品信息--获取个人信息--添加购物车--订单创建")
class Test01:
    # 1. 实例化获取工具类对象
    tool = FileTool("case1.xlsx")
    # 2. 读取Excel ->将数据从excel中读取并写入到json文中
    tool.read_excel()

    # 3. 测试方法
    @allure.story("订单创建成功")
    @allure.severity(allure.severity_level.CRITICAL)
    # @allure.step("测试成功步骤")
    @pytest.mark.parametrize("case", tool.read_json())
    def test01(self, case):
        log.info("正在执行调用执行数据：{}".format(case))
        # with allure.step("1登录--2获取商品信息--3获取个人信息--4添加购物车--5订单创建"):
        try:
            # 调用 执行接口方法
            r = Api(case).run_method()
            print("响应数据为：", r.text)
            print("响应状态码：", r.status_code)
            # 断言
            common_assert(r, case)
            # 将执行结果写入报告
            Test01.tool.write_excel(case.get("x_y"), "执行通过！")
        except Exception as e:
            Test01.tool.write_excel(case.get("x_y"), "执行失败！原因：{}".format(e))
            log.error("错误，原因：{}".format(e))
            raise
