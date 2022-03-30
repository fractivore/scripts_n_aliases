import jwt

key = 'iamalittleguywithafunnylittlethingamajig'

encoded = jwt.encode({
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}, key, algorithm="HS256", headers={
  "alg": "HS256"
})

print(encoded)
