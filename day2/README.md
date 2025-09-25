# Hands-On OWASP ZAP: Juice Shop DAST Exercise (Day 2)

## What this pipeline does
Runs OWASP Juice Shop (vulnerable app) and executes OWASP ZAP full scan. The pipeline stores `zap-report.html` and `zap-report.json` as artifacts.

## How to run (locally)
1. `docker pull bkimminich/juice-shop:latest`
2. `docker run -d --name juice -p 3000:3000 bkimminich/juice-shop:latest`
3. `docker run --rm -v $(pwd):/zap/wrk:rw ghcr.io/zaproxy/zaproxy:stable zap-full-scan.py -t http://localhost:3000 -r /zap/wrk/zap-report.html`

## Core concept questions
(Place answers here — see sample answers in project docs.)

## Submission checklist
- Screenshot of ZAP report (alerts list)
- Short description of 2 detected vulnerabilities (impact + recommended fix)