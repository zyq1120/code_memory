# -*- coding: utf-8 -*-
"""
浏览器自动化访问技能
使用 Selenium 实现网页浏览、截图、交互等能力
"""

import sys
import os
import time
from datetime import datetime

def check_selenium():
    """检查 Selenium 是否可用"""
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from webdriver_manager.chrome import ChromeDriverManager
        return True
    except ImportError as e:
        print(f"缺少依赖: {e}")
        return False

def browse_website(url, headless=True, screenshot_path=None, wait_time=3):
    """
    访问网站并获取内容
    
    参数:
        url: 网站地址
        headless: 是否无头模式（不显示浏览器窗口）
        screenshot_path: 截图保存路径（可选）
        wait_time: 等待页面加载时间（秒）
    
    返回:
        dict: 包含页面标题、内容、链接等信息
    """
    if not check_selenium():
        return {"error": "Selenium 未安装"}
    
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    
    # 配置 Chrome 选项
    chrome_options = Options()
    if headless:
        chrome_options.add_argument('--headless')  # 无头模式
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    driver = None
    try:
        # 自动下载并配置 ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print(f"正在访问: {url}")
        driver.get(url)
        
        # 等待页面加载
        time.sleep(wait_time)
        
        # 获取页面信息
        result = {
            "url": url,
            "title": driver.title,
            "current_url": driver.current_url,
        }
        
        # 获取页面文本内容
        try:
            body = driver.find_element(By.TAG_NAME, "body")
            result["text_content"] = body.text[:5000]  # 限制文本长度
        except:
            result["text_content"] = ""
        
        # 获取所有链接
        try:
            links = driver.find_elements(By.TAG_NAME, "a")
            result["links"] = [
                {"text": link.text, "href": link.get_attribute("href")}
                for link in links[:50]  # 限制链接数量
                if link.get_attribute("href")
            ]
        except:
            result["links"] = []
        
        # 获取页面源码（部分）
        result["page_source_length"] = len(driver.page_source)
        
        # 截图
        if screenshot_path:
            driver.save_screenshot(screenshot_path)
            result["screenshot"] = screenshot_path
            print(f"截图已保存: {screenshot_path}")
        
        return result
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        if driver:
            driver.quit()

def take_full_screenshot(url, output_path, wait_time=5):
    """
    获取网页完整截图
    
    参数:
        url: 网站地址
        output_path: 截图保存路径
        wait_time: 等待页面加载时间（秒）
    """
    if not check_selenium():
        return {"error": "Selenium 未安装"}
    
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.get(url)
        time.sleep(wait_time)
        
        # 获取页面总高度
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, total_height)
        
        driver.save_screenshot(output_path)
        return {"success": True, "path": output_path}
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        if driver:
            driver.quit()

def search_and_browse(search_query, num_results=3):
    """
    使用 Google 搜索并浏览结果
    
    参数:
        search_query: 搜索关键词
        num_results: 要浏览的结果数量
    """
    if not check_selenium():
        return {"error": "Selenium 未安装"}
    
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # 使用百度搜索（国内环境）
        search_url = f"https://www.baidu.com/s?wd={search_query}"
        driver.get(search_url)
        time.sleep(3)
        
        # 获取搜索结果
        results = []
        result_elements = driver.find_elements(By.CSS_SELECTOR, ".result")[:num_results]
        
        for elem in result_elements:
            try:
                title = elem.find_element(By.CSS_SELECTOR, "h3").text
                link = elem.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                snippet = elem.find_element(By.CSS_SELECTOR, ".c-abstract").text if elem.find_elements(By.CSS_SELECTOR, ".c-abstract") else ""
                results.append({
                    "title": title,
                    "link": link,
                    "snippet": snippet
                })
            except:
                continue
        
        return {"query": search_query, "results": results}
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        if driver:
            driver.quit()


# 测试代码
if __name__ == "__main__":
    print("=" * 60)
    print("浏览器自动化访问测试")
    print("=" * 60)
    
    # 测试1: 访问马鞍山学院官网
    print("\n测试1: 访问马鞍山学院官网")
    result = browse_website(
        "https://www.masu.edu.cn",
        headless=True,
        screenshot_path=r"C:\Users\yg\Desktop\masu_screenshot.png"
    )
    
    if "error" in result:
        print(f"错误: {result['error']}")
    else:
        print(f"页面标题: {result['title']}")
        print(f"当前URL: {result['current_url']}")
        print(f"链接数量: {len(result['links'])}")
        if result.get('screenshot'):
            print(f"截图位置: {result['screenshot']}")
    
    print("\n测试完成！")
