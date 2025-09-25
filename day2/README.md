# Day 2 — OWASP ZAP: Detecting & Understanding Web Vulnerabilities

## Objective
Run a DAST scan (OWASP ZAP) against a vulnerable web app, find vulnerabilities, and propose fixes.

## Steps performed
1. Launched target app (Juice Shop via Docker) and verified at http://:3000.
2. Ran OWASP ZAP scan in CI using `zap-full-scan.py` and saved `zap-report.html` as artifact.
3. Analyzed the report and documented two vulnerabilities below.

## Findings (two vulnerabilities)
1. **SQL Injection (A03:2021)**
   - **Location:** `/search?name=...`
   - **Impact:** Data exposure, unauthorized DB modification.
   - **Fix:** Parameterized queries, input validation, least-privilege DB user.

2. **Reflected XSS**
   - **Location:** `/greet?name=...`
   - **Impact:** Session theft, phishing, arbitrary JS execution.
   - **Fix:** Escape output, CSP, sanitize user input.

## Core concept answers
### 1. What is the purpose of DAST and how does it complement other security testing methods?
-   DAST (Dynamic Application Security Testing) tests an application in its running state.
-   It simulates real-world attacker behavior by sending malicious requests to the app.
-   Heps identify vulnerabilities such as XSS, SQL Injection, authentication flaws, and misconfigurations.
### 2. Explain how XSS or SQL injection vulnerabilities can affect an application and its users.
-   **Cross-Site Scripting (XSS):**
    - Allows attackers to inject and execute malicious scripts in the user’s browser.
    - Can steal cookies, session tokens, or sensitive user data.
    - May lead to account hijacking, phishing attacks, or spreading malware.

-   **SQL Injection (SQLi):**
    - Exploits unsanitized input fields to run malicious SQL queries.
    - Attackers can read, modify, or delete data in the database.
    - Can bypass authentication, leading to unauthorized access.
    - May cause full data breaches and reputational loss.

### 3. Describe the steps you would take to fix the vulnerabilities detected in your ZAP scan.
-   **For SQL Injection:**
    - Use parameterized queries / prepared statements instead of string concatenation.
    - Implement strong input validation and sanitization.
    - Apply least privilege on database accounts.

-   **For XSS:**
    - Encode or escape user inputs before rendering in HTML/JS.
    - Use frameworks/libraries with built-in XSS protection.
    - Implement a strong Content Security Policy (CSP).

-   **General Fixes:**
    - Apply secure configuration (disable default accounts, enforce HTTPS).
    - Patch and update frameworks, libraries, and dependencies regularly.
    - Add proper error handling to avoid information leakage.

### 4. How does integrating ZAP scans into CI/CD pipelines support shift-left security practices?** 
-   Shift-left means integrating security earlier in the Software Development Lifecycle (SDLC).
-   Running automated ZAP scans in CI/CD ensures vulnerabilities are caught before production release.
-   Developers get fast feedback on security issues as part of build/test stages.
-   Reduces cost of fixing vulnerabilities by detecting them early.

## Artifacts / Screenshots
- `zap-report.html` (attached as job artifact)
- Screenshots:
  - Before: Gitleaks scan showing leaks (if applicable)
  - After: Gitleaks 0 leaks
  - Running app (Docker container)
