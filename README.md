Content-Security-Policy Report URI for AWS Lambda
=================================================

Simple python application which runs on AWS Lambda and writes CSP reports into S3 for later processing.

Configuration
-------------

Deploy to Lambda and create a POST API with API Gateway, set this as the `report-uri` in your Content-Security-Policy header e.g.

``
  default-src 'self'; report-uri http://example.org/csp-report.cgi
``

Future ideas
------------

 * Integrate with other services on AWS
  - SNS to alert on new reports
 * Tools for processing reports from S3
