from selenium import webdriver

#/Users/yangnuocheng/Desktop/JavaExercise/第二次作业/JavaJsoup_Ecode/JavaSelenium/Googledrive/chromedriver

path = "/Users/yangnuocheng/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=path)

#如何伪装成一般浏览器？
driver.get("https://passport.damai.cn/login?ru=https%3A%2F%2Fdetail.damai.cn%2Fitem.htm%3Fspm%3Da2oeg.search_category.0.0.58835c611US41f%26id%3D602853549027%26clicktitle%3D2019%25E5%2591%25A8%25E6%25B7%25B1%25E2%2580%259CC-929%25E6%2598%259F%25E7%2590%2583%25E2%2580%259D%25E5%25B7%25A1%25E5%259B%259E%25E6%25BC%2594%25E5%2594%25B1%25E4%25BC%259A-%25E4%25B8%258A%25E6%25B5%25B7%25E7%25AB%2599")
session_url = driver.command_executor._url
session_id = driver.session_id
print(driver.command_executor._url)
print(driver.session_id)
