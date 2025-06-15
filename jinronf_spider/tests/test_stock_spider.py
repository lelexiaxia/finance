import unittest
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.stock_spider import StockSpider

class TestStockSpider(unittest.TestCase):
    def setUp(self):
        # 注意：测试前需要替换为实际的Tushare Pro Token
        self.token = 'your_tushare_pro_token'
        self.spider = StockSpider(self.token)
    
    def test_get_stock_list(self):
        """测试获取股票列表"""
        stocks = self.spider.get_stock_list()
        self.assertFalse(stocks.empty, "股票列表不应为空")
        self.assertTrue('ts_code' in stocks.columns, "应包含ts_code列")
    
    def test_get_daily_quotes(self):
        """测试获取股票日行情"""
        # 获取一个股票代码进行测试
        stocks = self.spider.get_stock_list()
        if not stocks.empty:
            sample_stock = stocks.iloc[0]['ts_code']
            daily_quotes = self.spider.get_daily_quotes(
                sample_stock, 
                start_date='20230101', 
                end_date='20230131'
            )
            self.assertFalse(daily_quotes.empty, f"获取{sample_stock}的日行情数据失败")

if __name__ == '__main__':
    unittest.main() 