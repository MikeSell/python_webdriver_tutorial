# Selenium Grid setup 

## Installation 

### Requirement - Java 

#### Suse opensuse Leap 42.3 installed with Java development kit 
```shell
mstan@grid-suse:~> java -version
openjdk version "1.8.0_181"
OpenJDK Runtime Environment (IcedTea 3.9.0) (build 1.8.0_181-b13 suse-27.1-x86_64)
OpenJDK 64-Bit Server VM (build 25.181-b13, mixed mode)
```

#### Ubuntu 18
sudo apt-get install default-jdk

```shell
mstan@grid-ubnt:~ $ java -version
openjdk version "10.0.2" 2018-07-17
OpenJDK Runtime Environment (build 10.0.2+13-Ubuntu-1ubuntu0.18.04.3)
OpenJDK 64-Bit Server VM (build 10.0.2+13-Ubuntu-1ubuntu0.18.04.3, mixed mode)
```

### Download the jar file 
http://selenium-release.storage.googleapis.com/index.html

wget http://selenium-release.storage.googleapis.com/3.9/selenium-server-standalone-3.9.1.jar

#### Start a hub 
java -jar selenium-server-standalone-3.9.1.jar -role hub

#### Start a node 
java -jar selenium-server-standalone-3.9.1.jar -role node  -hub http://192.168.122.60:4444/grid/register

## Using Grid

### Firefox and gechodriver
drv_firefox = webdriver.Remote(
   command_executor='http://192.168.122.60:4444/wd/hub',
   desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})

### Chrome and chromedriver

drv_chrome = webdriver.Remote(
   command_executor='http://192.168.122.60:4444/wd/hub',
   desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

#### headless and custom options 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
capabilities = {'browserName': 'chrome', 'javascriptEnabled': True}
capabilities.update(chrome_options.to_capabilities())
drv_chrome = webdriver.Remote(command_executor='http://192.168.122.60:4444/wd/hub', capabilities)
