package org.cbt.applitools;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import java.net.MalformedURLException;
import java.net.URL;
import com.applitools.eyes.selenium.Eyes;
import com.applitools.eyes.RectangleSize;

public class ApplitoolsTest extends TestCase {
    private String username = "chase%40crossbrowsertesting.com", authkey = "NOTMYAUTHKEY", score = "fail",
                   hubUrl = "http://" + username + ":" + authkey + "@hub.crossbrowsertesting.com:80/wd/hub";
    private CBTHelper cbt;
    private RemoteWebDriver driver;
    private Eyes eyes;

    public void setUp() throws MalformedURLException {
        DesiredCapabilities caps = new DesiredCapabilities();
        cbt = new CBTHelper(username, authkey, false);
        caps.setCapability("name", "Applitools Example");
        caps.setCapability("browserName", "Chrome");
        caps.setCapability("platform", "Windows 10");
        caps.setCapability("screenResolution", "1366x768");

        eyes = new Eyes();
        eyes.setApiKey("NOTMYAPIKEY");

        // create a new RemoteWebDriver object
        driver = new RemoteWebDriver(new URL(hubUrl), caps);
    }

    public void testApp() {
        // open a new instance of eyes
        eyes.open(driver, "CrossBrowserTesting", "My first Selenium Java test!",
                   new RectangleSize(800, 600));
        
        // navigate to the webpage we'd like to capture
        driver.get("https://crossbrowsertesting.com/visual-testing");

        // Visual checkpoint
        eyes.checkWindow("Visual Testing");

        eyes.close();
        score = "pass";
    }

    public void tearDown() {
        cbt.setSessionId(driver.getSessionId().toString());
        cbt.setScore(score);
        if (driver != null)
            driver.quit();
        eyes.abortIfNotClosed();
    }
}
