rom selenium import webdriver

username = "yukta";
password = "1234";

url = "https://www.stealmylogin.com/demo.html";
driver = webdriver.Chrome("/Users/vanshikakaul/Downloads/chromedriver_mac64/chromedriver");

driver.get(url);

driver.find_element("name", "username").send_keys(username);
driver.find_element("name", "password").send_keys(password);
driver.find_element("css selector", "input[type=\"submit\" i]").click();

print("Logged in");

input("Press enter to exit");
