### Java and Applitools

Run your Applitools Eyes tests using Java and CBT. To run, clone the repository, then:

```
cd Java/cbt
mvn compile
```

Be sure to enter your username and authorization key for [CrossBrowserTesting](https://app.crossbrowsertesting.com/account), as well as your [Applitools API key](http://support.applitools.com/customer/en/portal/articles/2118694-the-runner-key-api-key-). This change should be made on lines 14 and 29 of ApplitoolsTest.java. Once your script has been updated, run your tests with:

```
mvn test
```

