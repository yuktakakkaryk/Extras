from selenium import webdriver

username = "abc";
password = "abc";

url = "https://ssp-qa.dx.aod.labs.broadcom.net/list/";
#url2 = "https://broadcom.oktapreview.com/app/broadcom_aiopsselfserviceqaportal_1/exk1jeoj6airiWSko0h8/sso/saml?SAMLRequest=nVJBbsIwEPxK5HviBFpULIgEpVWRgCISWqkXtCQGDIltvA6lv68JLagXDj3ueEY7s%2BOOxJD1KruRM76vOFrvWBYSmYO7pDKSKUDhRig5MpuxpDcesUYQMm2UVZkqyEUQ3RYAIjdWKEm84aBLRO7Pe%2BNkMlmvUnnXnj%2F1qwnx3rhBR%2BkSp3A8xIoPJVqQ1kFho%2BmHTT%2BK0qjNmi123%2F4g3sB5FhJsrdpYq5FRujQK8kyVgdpZ0IYfBP8M3ExB68vjAoTSzlSxcsYOIuN70MpYKBYR5cddtOVq2wJhxHuyU%2BHmgSIqilC6yNOf8H0hcyHXt4MvzyRkL2k69aevSUq83u8xHpXEquQmOVuYz0bXFIja30OQHwNQeVDAEoNLMMlt7aWxAFcehQwpiTuuBFYfzXjPypRgbzs7Ia6HVU1lXFphv0j8z%2FUdet0en4a%2F%2Fyr%2BBg%3D%3D";
driver = webdriver.Chrome("/Users/vanshikakaul/Downloads/chromedriver_mac64/chromedriver");

driver.get(url);
driver.get("https://broadcom.oktapreview.com/app/broadcom_aiopsselfserviceqaportal_1/exk1jeoj6airiWSko0h8/sso/saml?SAMLRequest=nVJBbsIwEPxK5HviBFpULIgEpVWRgCISWqkXtCQGDIltvA6lv68JLagXDj3ueEY7s%2BOOxJD1KruRM76vOFrvWBYSmYO7pDKSKUDhRig5MpuxpDcesUYQMm2UVZkqyEUQ3RYAIjdWKEm84aBLRO7Pe%2BNkMlmvUnnXnj%2F1qwnx3rhBR%2BkSp3A8xIoPJVqQ1kFho%2BmHTT%2BK0qjNmi123%2F4g3sB5FhJsrdpYq5FRujQK8kyVgdpZ0IYfBP8M3ExB68vjAoTSzlSxcsYOIuN70MpYKBYR5cddtOVq2wJhxHuyU%2BHmgSIqilC6yNOf8H0hcyHXt4MvzyRkL2k69aevSUq83u8xHpXEquQmOVuYz0bXFIja30OQHwNQeVDAEoNLMMlt7aWxAFcehQwpiTuuBFYfzXjPypRgbzs7Ia6HVU1lXFphv0j8z%2FUdet0en4a%2F%2Fyr%2BBg%3D%3D");

print(driver.find_element("id", "input43").send_keys(username));


print("Logged in");

input("Press enter to exit");
