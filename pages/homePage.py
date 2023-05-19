class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_xpath = "swag labs"
        self.product_link_xpath = "Sauce lab backpacks"
        self.product_add_to_cart_id = "add-to-cart-sauce-labs-backpack"
        self.back_to_products_id = "back to product"
        self.shopping_cart_container_id = "shopping_cart_container"
        self.checkout_id = "checkout"
        self.First_Name = "first-name"
        self.Last_Name = "last-name"
        self.Postal_Code = "postal-code"
        self.Continue = "continue"
        self.Finish = "finish"
        self.Back_HomePage = "back-to-products"
        self.Menu_Button = "react-burger-menu-btn"
        self.logout = "self.logout_link_linkText"

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_xpath).click()

    def click_product(self):
        self.driver.find_element_by_id(self.product_link_xpath).click()

    def click_product_add_to_cart(self):
        self.driver.find_element_by_id(self.product_add_to_cart_id).click()

    def click_back_to_products(self):
        self.driver.find_element_by_id(self.back_to_products_id).click()

    def click_shopping_cart_container(self):
        self.driver.find_element_by.id(self.shopping_cart_container_id).click()

    def click_checkout(self):
        self.driver.find_element_by_id(self.click_checkout).click()

    def click_First_Name(self):
        self.driver.find_element_by_id(self.First_Name).send_keys("Upend ra")

    def click_Last_Name(self):
        self.driver.find_element_by_id(self.Last_Name).send_keys("Singh")

    def click_Postal_Code(self):
        self.driver.find_element_by_id(self.Postal_Code).send_keys("226041")

    def click_Continue(self):
        self.driver.find_element_by_id(self.Continue).click()

    def click_Finish(self):
        self.driver.find_element_by_id(self.Finish).click()

    def click_Back_HomePage(self):
        self.driver.find_element_by_id(self.Back_HomePage).click()

    def click_Menu_Button(self):
        self.driver.find_element_by_id(self.Menu_Button).click()

    def click_logout(self):
        self.driver.find_element_by_id(self.logout).click()
