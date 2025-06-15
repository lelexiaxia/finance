import requests
import pandas as pd
from typing import Dict, Any, Optional

class BaseFinancialSpider:
    def __init__(self, base_url: str = None):
        """
        初始化基础金融数据爬虫
        
        :param base_url: 基础URL
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def fetch_data(self, url: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        """
        获取网页数据
        
        :param url: 目标URL
        :param params: 请求参数
        :return: 响应对象
        """
        try:
            response = self.session.get(
                url, 
                headers=self.headers, 
                params=params, 
                timeout=10
            )
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"数据获取失败: {e}")
            return None
    
    def save_to_excel(self, data: pd.DataFrame, filename: str):
        """
        将数据保存为Excel文件
        
        :param data: 数据DataFrame
        :param filename: 文件名
        """
        try:
            data.to_excel(f'../data/{filename}', index=False, engine='openpyxl')
            print(f"数据已保存到 {filename}")
        except Exception as e:
            print(f"保存文件失败: {e}")
    
    def save_to_csv(self, data: pd.DataFrame, filename: str):
        """
        将数据保存为CSV文件
        
        :param data: 数据DataFrame
        :param filename: 文件名
        """
        try:
            data.to_csv(f'../data/{filename}', index=False)
            print(f"数据已保存到 {filename}")
        except Exception as e:
            print(f"保存文件失败: {e}") 