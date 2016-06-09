
cat <<EOF
*************************************************
*****输入客户机ip及端口ex：172.19.2.136:3344*****
*************************************************
EOF
read Read

if [ "$Read" == "" ];then
    echo -e "\033[0;31m输入为空 重新输入！！\033[0m"
    exit 1
fi

path=${PWD}
reg='([0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,4}$'
if [[ "$Read" =~ $reg ]];then
        echo -e "\033[0;31m----执行客户机批量替换----\033[0m"
        sed -i 's#^.*self.driver=webdriver.*$#        self.driver=webdriver.Remote("http://'$Read'/wd/hub",webdriver.DesiredCapabilities.FIREFOX)#g' `grep "self.driver=webdriver" -rl $path/bank_websitecase/*`
        sed -i 's#^.*self.driver=webdriver.*$#        self.driver=webdriver.Remote("http://'$Read'/wd/hub",webdriver.DesiredCapabilities.FIREFOX)#g' `grep "self.driver=webdriver" -rl $path/bank_omscase/*`
else
    echo -e "\033[0;31m输入不符合规则重新输入！！\033[0m"
fi
