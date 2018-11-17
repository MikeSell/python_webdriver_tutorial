# Configuring headless to run in Grid 

## grid

`sudo docker-compose up -d --scale chrome=3 --scale firefox=2`

## 

```python
opts = webdriver.ChromeOptions()
opts.set_headless()
driver = webdriver.Remote(command_executor = 'http://localhost:4444/wd/hub', 
                        desired_capabilities = opts.to_capabilities())
```



