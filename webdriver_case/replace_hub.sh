sed -i 's#^.*self.driver=webdriver.*$#        self.driver=webdriver.Remote("http://172.19.2.136:3344/wd/hub",webdriver.DesiredCapabilities.FIREFOX)#g' `grep "self.driver=webdriver" -rl /home/webdriver_case/bank_test/`

sed -i 's#^.*self.driver=webdriver.*$#        self.driver=webdriver.Remote("http://172.19.2.136:3345/wd/hub",webdriver.DesiredCapabilities.FIREFOX)#g' `grep "self.driver=webdriver" -rl /home/webdriver_case/bank_test/bank_websitecase/*`
