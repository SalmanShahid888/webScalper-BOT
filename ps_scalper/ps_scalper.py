import time
from selenium import webdriver

# FOR USING CHROME 
option = webdriver.ChromeOptions()

#You Will have to add the path or file location of CHROME on your PC in the following field
option.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
chrome_driver_binary = r"C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options = option)
driver.delete_all_cookies()
#AUTOMATED LOGIN
time.sleep(5)
#driver.get("https://www.texonware.com/")

#INSERT URL OF THE WEBSITE YOU WANT TO CRAWL
driver.get("")

# INSERT SIGN IN BUTTON ELEMENT XPATH / ID 
signInbtn = driver.find_element_by_xpath('//*[@id="masthead"]/div[1]/div/div[3]/div[1]/a')
signInbtn.click()
#TYPES USERNAME IN THE GIVEN FIELD 
time.sleep(2)
username = driver.find_element_by_id('panel_username')
username.click()
type(username)
#Insert Username in the braces between COLONS
username.send_keys(" ")
#TYPES PASSWORD
time.sleep(2)
password = driver.find_element_by_id('panel_password')
password.click()
type(password)
#Insert Password Here like you did in Username
password.send_keys(" ")
#SIGNS IN THE USER
time.sleep(60)
#userSignInBtn = driver.find_element_by_xpath('//*[@id="login-panel"]/div[2]/div[3]/form[1]/p[4]/button')
#userSignInBtn.click()



# Actual Technoware Website LINK

# Dummy URL
#time.sleep(10)
#driver.get("https://www.texonware.com/product/gamdias-kratos-e1-500w-80-plus-rgb-psu-price-in-pakistan/")


# LOGIC

#IN THIS SECTION OF THE CODE YOU'LL NEED TO ADD FIELDS YOU WANT TO AUTOMATICALLY FILL

buyButton = False 
while not buyButton: 

    try:
        #if this works then the button is not pytopen
        addtoCartbtn = addButton = driver.find_element_by_class_name("out-of-stock")

        print("*****Button isn't Ready Yet*****")

        time.sleep(1)
        driver.refresh()

    except:
#ADDS TO CART BUTTON IS CLICKED
            addtoCartbtn = addButton = driver.find_element_by_class_name("single_add_to_cart_button")

            print("*****Button was clicked*****")
            addtoCartbtn.click()
            buyButton = True
#CLICKS ON THE CART BUTTON IN THE HEADER
            time.sleep(6)
            openCartToggle = driver.find_element_by_xpath('//*[@id="masthead"]/div[1]/div/div[3]/div[3]/a')
            openCartToggle.click() 
            print("*****Cart Toggle Button was clicked*****")
#CLICKS ON THE CHECKOUT BUTTON
            time.sleep(2)
            checkOutbtn = driver.find_element_by_xpath('//*[@id="cart-panel"]/div[2]/div[3]/div[1]/p[2]/a[2]')
            checkOutbtn.click()

            print("*****Checkout Button was Clicked*****")
#TERMS AND CONDITION CHECK            
            time.sleep(2.5)
            termsAndCond = driver.find_element_by_xpath('//*[@id="payment"]/div/div/p/label')
            termsAndCond.click()
            print("*****TERMS AND CONDITIONS CHECKED***")
# PLACE ORDER BUTTON
            time.sleep(2)
            placeOrderBtn = driver.find_element_by_xpath('//*[@id="place_order"]')
            placeOrderBtn.click()
            print("****ORDER HAS BEEN PLACED****")

