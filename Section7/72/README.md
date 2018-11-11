# Configuring headless to run in Grid 

```python
opts = webdriver.ChromeOptions()
opts.set_headless()
driver = webdriver.Remote(command_executor = 'http://192.168.122.60:4444/wd/hub', 
                        desired_capabilities = opts.to_capabilities())
```



