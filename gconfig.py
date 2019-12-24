"""
from OpenSSL.crypto import load_pkcs12, FILETYPE_PEM, FILETYPE_ASN1
import OpenSSL
from psd2bank.settings import P12_KEY

with open('www.testorg1.cz.p12', 'rb') as f:
  c = f.read()
p = load_pkcs12(c, P12_KEY)
certificate = p.get_certificate()
private_key = p.get_privatekey()
# Where type is FILETYPE_PEM or FILETYPE_ASN1 (for DER).
type_ = FILETYPE_PEM
privatekey = OpenSSL.crypto.dump_privatekey(type_, private_key).decode("utf-8")
certificate_text = OpenSSL.crypto.dump_certificate(type_, certificate).decode("utf-8")

with open("certificates/privateKey.pem", "w+") as f:
  f.write(privatekey)
  f.close()

  with open("certificates/publicCert.pem", "w+") as f:
    f.write(certificate_text)
    f.close()

keyfile = 'certificates/privateKey.pem'
certfile = 'certificates/publicCert.pem'
"""

bind = '0.0.0.0:80'
workers = 3
