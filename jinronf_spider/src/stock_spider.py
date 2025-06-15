import tushare as ts
import pandas as pd
from base_spider import BaseFinancialSpider

class StockSpider(BaseFinancialSpider):
    def __init__(self, token: str = None):
        """
        初始化股票数据爬虫
        
        :param token: Tushare Pro API Token
        """
        super().__init__()
        self.pro = ts.pro_api(token) if token else None
    
    def get_stock_list(self, exchange: str = 'SSE') -> pd.DataFrame:
        """
        获取股票列表
        
        :param exchange: 交易所，默认上海证券交易所
        :return: 股票列表DataFrame
        """
        try:
            stock_list = self.pro.stock_basic(
                exchange=exchange, 
                list_status='L', 
                fields='ts_code,symbol,name,area,industry,list_date'
            )
            return stock_list
        except Exception as e:
            print(f"获取股票列表失败: {e}")
            return pd.DataFrame()
    
    def get_daily_quotes(self, ts_code: str, start_date: str, end_date: str) -> pd.DataFrame:
        """
        获取股票日行情数据
        
        :param ts_code: 股票代码
        :param start_date: 开始日期
        :param end_date: 结束日期
        :return: 日行情数据DataFrame
        """
        try:
            daily_data = self.pro.daily(
                ts_code=ts_code, 
                start_date=start_date, 
                end_date=end_date
            )
            return daily_data
        except Exception as e:
            print(f"获取股票日行情失败: {e}")
            return pd.DataFrame()
    
    def main(self, token: str):
        """
        主程序示例
        
        :param token: Tushare Pro API Token
        """
        # 初始化
        self.pro = ts.pro_api(token)
        
        # 获取股票列表
        stocks = self.get_stock_list()
        self.save_to_excel(stocks, 'stock_list.xlsx')
        
        # 获取某只股票的日行情数据（示例）
        if not stocks.empty:
            sample_stock = stocks.iloc[0]['ts_code']
            daily_quotes = self.get_daily_quotes(
                sample_stock, 
                start_date='20230101', 
                end_date='20231231'
            )
            self.save_to_excel(daily_quotes, f'{sample_stock}_daily_quotes.xlsx')

if __name__ == '__main__':
    # 使用前请替换为您的Tushare Pro Token
    TUSHARE_TOKEN = 'your_tushare_pro_token'
    spider = StockSpider()
    spider.main(TUSHARE_TOKEN) 