import hashlib
s='deltafast'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
