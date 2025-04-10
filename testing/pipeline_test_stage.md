# CI/CD Testing Pipeline Stages with Sample Tools and Code

This document outlines a typical CI/CD testing pipeline with examples of tools and code/pipeline snippets for each stage.

---

## Pre-commit Testing

### ✅ Linting and Static Code Analysis
- **Tools:** `ESLint`, `Flake8`, `SonarQube`

#### Example (JavaScript with ESLint)
```bash
npm install eslint --save-dev
npx eslint .
```

#### Example (Python with Flake8)
```bash
pip install flake8
flake8 your_module/
```

#### Example (SonarQube Scanner)
```bash
sonar-scanner \
  -Dsonar.projectKey=my_project \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=<your_token>
```

---

## Build Stage

### ✅ Unit Testing
- **Tools:** `JUnit`, `PyTest`, `Mocha`

#### Example (Python with PyTest)
```bash
pip install pytest
pytest tests/unit/
```

### ✅ Integration Testing
- **Tools:** `Testcontainers`, `Postman/Newman`, `PyTest`

#### Example (Node.js using Mocha)
```bash
npm install mocha chai --save-dev
mocha tests/integration/
```

---

## Post-build Stage

### ✅ API Testing
- **Tools:** `Postman`, `Newman`

#### Example (Newman CLI)
```bash
newman run collection.json
```

### ✅ Performance Testing
- **Tools:** `JMeter`, `k6`, `Locust`

#### Example (k6)
```bash
k6 run loadtest.js
```

---

## Staging / Pre-Production

### ✅ Acceptance Testing
- **Tools:** `Cucumber`, `Robot Framework`

#### Example (Cucumber for BDD)
```gherkin
Feature: User login
  Scenario: Valid credentials
    Given I am on the login page
    When I enter valid credentials
    Then I should be redirected to the dashboard
```

### ✅ Regression Testing
- **Tools:** `Selenium`, `TestNG`

#### Example (Selenium + TestNG)
```java
@Test
public void verifyHomePageTitle() {
  WebDriver driver = new ChromeDriver();
  driver.get("http://example.com");
  Assert.assertEquals(driver.getTitle(), "Home");
  driver.quit();
}
```

### ✅ Security Testing
- **Tools:** `OWASP ZAP`, `SonarQube`, `Checkmarx`

#### Example (OWASP ZAP CLI)
```bash
zap-cli quick-scan --self-contained http://localhost:8080
```

---

## Production

### ✅ Smoke Testing
- **Tools:** `Selenium`, `Postman`, Custom Scripts

#### Example (Postman with Newman)
```bash
newman run smoke-tests.postman_collection.json
```

### ✅ Monitoring and Health Checks
- **Tools:** `Prometheus`, `Grafana`, `Datadog`, `ELK Stack`

#### Example (Health Endpoint Check with Curl)
```bash
curl -f http://localhost:8080/health || exit 1
```

---

## Summary

Each stage helps in ensuring software quality and stability. Automating them improves efficiency and reduces human error. Integrate these tools into your CI/CD pipelines using Jenkins, GitHub Actions, GitLab CI, or Azure DevOps.
