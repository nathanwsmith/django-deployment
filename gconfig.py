from OpenSSL.crypto import load_pkcs12, FILETYPE_PEM, FILETYPE_ASN1
import OpenSSL

with open('www.testorg1.cz.p12', 'rb') as f:
  c = f.read()
#TODO P12KEY
p = load_pkcs12(c, b'12345')
certificate = p.get_certificate()
private_key = p.get_privatekey()
# Where type is FILETYPE_PEM or FILETYPE_ASN1 (for DER).
type_ = FILETYPE_PEM
privatekey = OpenSSL.crypto.dump_privatekey(type_, private_key).decode("utf-8")
certificate_text = OpenSSL.crypto.dump_certificate(type_, certificate).decode("utf-8")

with open("privateKey.pem", "w+") as f:
  f.write(privatekey)
  f.close()

  with open("publicCert.pem", "w+") as f:
    f.write(certificate_text)
    f.close()

keyfile = 'privateKey.pem'
certfile = 'publicCert.pem'

bind = '0.0.0.0:8000'
workers = 3
