var webdriver = require('selenium-webdriver');
var Eyes = require('eyes.selenium').Eyes;
var request = require('request');
 
var username = 'chase@crossbrowsertesting.com';
var authkey = 'NOTMYAUTHKEY';
var score = 'pass';
var sessionId;
var hubUrl = 'http://' + username + ':' + authkey + '@hub.crossbrowsertesting.com:80/wd/hub';

// choose some capabilities that will reflect
// the browser/os we want to test on. 
var caps = {
    'name': 'Applitools Example',
    'browserName': 'Chrome',
    'platform': 'Windows 10',
    'screenResolution': '1366x768'
};

var driver = new webdriver.Builder().usingServer(hubUrl).withCapabilities(caps).build();

driver.getSession().then(function(session) {
    sessionId = session.id_;
});

var eyes = new Eyes();

// This is your api key, make sure you use it in all your tests.
eyes.setApiKey('NOTMYAPIKEY');

// Start visual testing with browser viewport set to 800x600.
// Make sure to use the driver returned through 'then' from this point on.
eyes.open(driver, 'CrossBrowserTesting', 'My first Applitools test with NodeJS', { width: 800, height: 600 })
    .then((driver) => {
        // navigate to the page we'd like to test
        driver.get('https://crossbrowsertesting.com');
        // Visual validation point
        eyes.checkWindow('Visual Testing');
        // End visual testing. Validate visual correctness.
        eyes.close();
    
    }).catch((reason) => {
        console.log('Eyes returned differences on ' + reason.results.hostApp);
        console.log('See the differences here ' + reason.results.appUrls.session);
        score = 'fail';
    
    }).then(() => {
        driver.quit();
        setScore(sessionId, score);
        console.log('Test finished!', score);
    });


var setScore = (sessionId, score) => {
    if (sessionId) {
        request({
            method: 'PUT',
            uri: 'https://crossbrowsertesting.com/api/v3/selenium/' + sessionId,
            body: {'action': 'set_score', 'score': score },
            json: true
        },
        function(error, response, body) {
            if (error) {
                console.log(error);
            }
        })
        .auth(username, authkey);
    }
}