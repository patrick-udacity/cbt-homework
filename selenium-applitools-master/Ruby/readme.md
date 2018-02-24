### Ruby and Applitools

Run your Applitools Eyes tests using Ruby and CBT. If you don't already have [bundle](http://bundler.io/) installed, its very helpful for grabbing the dependencies you need quickly. From there, clone the repository, then:

```
cd Ruby
bundle install
```

Be sure to enter your username and authorization key for [CrossBrowserTesting](https://app.crossbrowsertesting.com/account), as well as your [Applitools API key](http://support.applitools.com/customer/en/portal/articles/2118694-the-runner-key-api-key-). These credentials should be changed on lines 17, 19, 20 of test.rb.  Once all the necessary gems have been installed and your script has been updated, run with:

```
ruby test.rb
```
