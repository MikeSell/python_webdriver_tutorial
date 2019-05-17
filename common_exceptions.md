# Webdriver exceptions 

- **NoSuchElementException**: Webdriver is unable to identify the elements during runtime, i.e. FindBy method can’t find the element.
   - Selector is not correctly constructed
   - Element not yet loaded - if wait is not used 
- **NoSuchWindowException**: Webdriver is switching to an invalid window, which is not available.
- **ElementNotVisibleException**: Although an element is present in the DOM, it is not visible (cannot be interacted with). For example: Hidden Elements – defined in HTML using type=”hidden”.
- **ElementNotSelectableException**: Although an element is present in the DOM, it may be disabled (cannot be clicked/selected).
- **InvalidSelectorException**: Selector used to find an element does not return a WebElement. Say XPath expression is used which is either syntactically invalid or does not select WebElement.
- **NoAlertPresentException**: Webdriver is switching to an invalid alert, which is not available.
- **StaleElementReferenceException**: The referenced element is no longer present on the DOM page (reference to an element is now Stale). For example: the element belongs to a different frame than the current one OR the user has navigated away to another page.
- **SessionNotFoundException**: The Webdriver is performing the action immediately after ‘quitting’ the browser.
- **TimeoutException**: The command did not complete in enough time. E.g. the element didn’t display in the specified time. Encountered when working with waits.
- **WebDriverException**: Webdriver is performing the action immediately after ‘closing’ the browser.

