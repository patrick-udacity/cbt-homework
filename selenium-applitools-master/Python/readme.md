### Python and Applitools

Run your Applitools Eyes tests using Python and CBT. To run, clone the repository, then:

```
cd Python
pip install selenium requests eyes-selenium
```

Be sure to enter your username and authorization key for [CrossBrowserTesting](https://app.crossbrowsertesting.com/account), as well as your [Applitools API key](http://support.applitools.com/customer/en/portal/articles/2118694-the-runner-key-api-key-). This should be done on lines 5, 6, and 11 of test.py. Once all the dependencies are installed and the script has been updated, run your test with:

```
python test.py
```
