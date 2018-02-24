var webdriver = require('selenium-webdriver');
var Eyes = require('eyes.selenium').Eyes;
var request = require('request');
webdriver.promise.USE_PROMISE_MANAGER = false;

const username = "chase@crossbrowsertesting.com";
const authkey = "NOTMYAUTHKEY";
const hubUrl = "http://" + username + ":" + authkey + "@hub.crossbrowsertesting.com:80/wd/hub";

// choose some capabilities that will reflect
// the browser/os we want to test on. 
var caps = {
    'name': 'Applitools Example',
    'browserName': 'Chrome',
    'platform': 'Windows 10',
    'screenResolution': '1366x768'
};

var driver = new webdriver.Builder()
                .usingServer(hubUrl)
                .withCapabilities(caps)
                .build();

var eyes = new Eyes();

// This is your api key, make sure you use it in all your tests.
eyes.setApiKey('NOTMYAPIKEY');

var runTest = async () => {
    var score, session = await driver.getSession();
    try {
        sessionId = session.id_;
        await eyes.open(driver, 'CrossBrowserTesting', 'My first Applitools test with NodeJS', { width: 800, height: 600 });
        await driver.get('https://crossbrowsertesting.com/visual-testing');
        await eyes.checkWindow('Visual Testing');
        // End visual testing. Validate visual correctness.
        await eyes.close();
        score = 'pass';
    } catch (reason) {
        console.log('Eyes returned differences on ' + reason.results.hostApp);
        console.log('See the differences here ' + reason.results.appUrls.session);
        score = 'fail';
    } finally {
        await driver.quit();
        await setScore(sessionId, score);
        console.log('Test finished!', score);
    }
}

var setScore = async (sessionId, score) => {
    try {
        await request({
            method: 'PUT',
            uri: 'https://crossbrowsertesting.com/api/v3/selenium/' + sessionId,
            body: {'action': 'set_score', 'score': score },
            json: true
        }).auth(username, authkey);
    } catch (err) {
        console.log(err)
    }
}

runTest();
