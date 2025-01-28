from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

# SOAP Service Definition
class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(self, num1, num2):
        """Add two numbers."""
        return num1 + num2

# Create the SOAP application
soap_app = Application([CalculatorService],
                       tns='soap.calculator',
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())

# Wrap the SOAP application in a WSGI container
wsgi_app = WsgiApplication(soap_app)

if __name__ == '__main__':
    # Start the SOAP server
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("SOAP service running on http://0.0.0.0:8000")
    server.serve_forever()