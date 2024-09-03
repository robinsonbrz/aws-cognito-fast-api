# AWS Cognito with Fastapi

## by awsmasterchef

API Authentication Using AWS Cognito | Python Flask FastAPI

https://www.youtube.com/watch?v=KJ3R3pa6PnU

Traduzido e adaptado por @robinsonbrz

## Setup python e .env

Criar pool cognito na AWS e extrair as informações e colar no arquivo **.envEXEMPLO**

```sh
POOL_REGION=us-east-1
POOL_ID=us-east-1_Wasddas
CLIENT_ID=6n1oasdghyjyjjgh4
```

Renomear o arquivo **.envEXEMPLO** para **.env**

## Criar o ambiente virtual


```sh
python -m venv .venv
source .venv/bin/activate 
python -m pip install --upgrade pip
pip install -r requirements.txt
```



![](assets/ksnip_20240903-151720.png)
![](assets/ksnip_20240903-151954.png)
![](assets/ksnip_20240903-152043.png)
![](assets/ksnip_20240903-152120.png)
![](assets/ksnip_20240903-152217.png)
![](assets/ksnip_20240903-152247.png)
![](assets/ksnip_20240903-152345.png)
![](assets/ksnip_20240903-152507.png)
![](assets/ksnip_20240903-152624.png)
![](assets/ksnip_20240903-152908.png)
![](assets/ksnip_20240903-152946.png)
![](assets/ksnip_20240903-153050.png)
![](assets/ksnip_20240903-153107.png)
![](assets/ksnip_20240903-153423.png)
![](assets/ksnip_20240903-153435.png)
![](assets/ksnip_20240903-153450.png)
![](assets/ksnip_20240903-153711.png)

Autenticar na UI Amazon
![Autenticar na UI Amazon](assets/ksnip_20240903-153721.png)

Em seguida voltar na Console AWS e confirmar o usuário
![](assets/ksnip_20240903-154100.png)
![](assets/ksnip_20240903-154112.png)
![](assets/ksnip_20240903-154436.png)
![](assets/ksnip_20240903-154505.png)
![](assets/ksnip_20240903-154529.png)
![](assets/ksnip_20240903-154607.png)

Depois de autenticar com sucesso o Token será entregue como uma query string no browser

Retirar o Access Token e utilizar no Postman

´´´
#access_token=eyJraWQiOiJmdGY4OFNTRUtSeVwvRVFNcGJHQjdcL0pBOU4wT3pkTUM5YVE4OFlcL25WYXBZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJmNDk4NzRkOC0xMGUxLTcwOGUtOGIyYi1iYmVlZDNmYWQzYzYiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6InBob25lIG9wZW5pZCBlbWFpbCIsImF1dGhfdGltZSI6MTcyNTM4OTI1OSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfV0xqcEhIdjRMIiwiZXhwIjoxNzI1MzkyODU5LCJpYXQiOjE3MjUzODkyNTksInZlcnNpb24iOjIsImp0aSI6IjI3NmFmOWM3LTY4MzEtNGY4ZS05M2E5LWNlNTNiOTQwOTAyZCIsImNsaWVudF9pZCI6IjZuMW81b2xyamJpZnFlb290dWNwY21xcGQ0IiwidXNlcm5hbWUiOiJyb2ItYXdzLWNvZ25pdG8ifQ.Las6TwBLgyhMUCR2sGiwaInib4IjeNoofAiMovP8LJCi6-lb6-3E1ixDEjshOxZZp4XraNI0AQPp_VhcT2d3RwAVY6zP_4CO9pzFqYJrE9-2wZlRzubmEggG8zz0SDAyOPR5Z_trbip7u8e5zkzE2ib7MUVM-QNQ61BLINphSwxKCKev85nmVKJlmb61RiC2ljD4D_oMtMyek-dYP4RG3RMgzCOjFhccoEKNpR3a8zgwZQfjWYJAbSAjvQHXbmiqIy8J9nbnSUdq2QOsIuNSrIylYVthCmRSNGGj10Vv16TnOEDQnZWJWzS6OOZGfPWYXVbJdCWpviPTzpl6lksRPA&id_token=eyJraWQiOiJmSVwvM3Voc1ZvUFlHZ1N0T2JxSE5LMXdXVnRlcUd1Y1lJRnROemt5azVjYz0iLCJhbGciOiJSUzI1NiJ9.eyJhdF9oYXNoIjoiZkFPWDE2aG5OeDZSRTJwMF9vNXI0dyIsInN1YiI6ImY0OTg3NGQ4LTEwZTEtNzA4ZS04YjJiLWJiZWVkM2ZhZDNjNiIsImF1ZCI6IjZuMW81b2xyamJpZnFlb290dWNwY21xcGQ0IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE3MjUzODkyNTksImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX1dManBISHY0TCIsImNvZ25pdG86dXNlcm5hbWUiOiJyb2ItYXdzLWNvZ25pdG8iLCJleHAiOjE3MjUzOTI4NTksImlhdCI6MTcyNTM4OTI1OSwianRpIjoiODc0Y2Q3NTEtNWIxMS00NmY3LWIwY2EtYzQ3ODc5NDlmZDg5In0.qrnjT18_zmy-1H-Cem1BPdqG00BhWZ2XzoFh9s7kJM2hfjCqMq5vIJy1vNBi04Q2UTLRo71U4qoTwyNPe9n7p_jEUFrKVnjMrBWruvp60_WZP_kUNPljjZVpVtmqH4aif7SMP_zANJJwyk4KOJRNar9G9rn7tAUxfzhEXkziO1eXtoXW78qGLBlpF74KWOOHcIBTAoDiUQzPb-cswzhzRAebsdpfLVZx0in7ndfXxN--5R5u9QHyYPeZdsmNouJ5G6W0bHmzMq1w9z6BlSw6ajqd-AxqWRyS8-bzTxbnTfa4_BoDszHApWMmcIowvo6xSwh8Dk67hVX-JtpYnSRwMw&token_type=Bearer&expires_in=3600
´´´

## Executar o programa

```sh
python main.py 
```


Colar no modo autenticação bearer Token

![](assets/ksnip_20240903-160723.png)