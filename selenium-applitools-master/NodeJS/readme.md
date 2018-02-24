### NodeJS and Applitools

Run your Applitools Eyes tests using NodeJS and CBT. To run, clone the repository, then:

```
cd NodeJS
npm install
```

Be sure to enter your username and authorization key for [CrossBrowserTesting](https://app.crossbrowsertesting.com/account), as well as your [Applitools API key](http://support.applitools.com/customer/en/portal/articles/2118694-the-runner-key-api-key-). This should be done on lines 5, 6, and 29 of test.py One all the necessary packages have been installed and your script has been updated, run with:

```
npm test
```