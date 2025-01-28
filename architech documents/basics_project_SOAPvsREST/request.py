import requests

# SOAP request payload
soap_payload = """<?xml version="1.0"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="soap.calculator">
   <soapenv:Header/>
   <soapenv:Body>
      <tns:add>
         <tns:num1>10</tns:num1>
         <tns:num2>20</tns:num2>
      </tns:add>
   </soapenv:Body>
</soapenv:Envelope>"""

# Send the SOAP request
response = requests.post("http://0.0.0.0:8000", data=soap_payload, headers={"Content-Type": "text/xml"})
print("SOAP Response:", response.text)