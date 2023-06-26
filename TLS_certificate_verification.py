import ssl
import socket
import hashlib
 
# addr = 'token.actions.githubusercontent.com'
addr = 'dst.dk'
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
wrappedSocket = ssl.wrap_socket(sock)

try:
  wrappedSocket.connect((addr, 443))
  print (wrappedSocket)
except:
  response = False
else:
  der_cert = wrappedSocket.getpeercert(True)
  pem_cert = ssl.DER_cert_to_PEM_cert(wrappedSocket.getpeercert(True))
  print(pem_cert)
 
  #Print SHA1 Thumbprint
  thumb_sha1 = hashlib.sha1(der_cert).hexdigest()
  print("SHA1: " + thumb_sha1)
