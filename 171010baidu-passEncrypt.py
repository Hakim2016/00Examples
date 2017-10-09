import rsa
import base64

# 密码加密
def get_password(password_input, pubkey):
    pub = rsa.PublicKey.load_pkcs1_openssl_pem(pubkey.encode("utf-8"))
    password_input = password_input.encode("utf-8")
    psword = rsa.encrypt(password_input, pub)
    psword = base64.b64encode(psword)
    return psword.decode("utf-8")

if __name__ == '__main__':
    get_password()
    pass