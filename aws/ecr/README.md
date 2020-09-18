
1. Create repository from AWS console

https://ap-northeast-1.console.aws.amazon.com/ecr/repositories?region=ap-northeast-1

2. Docker client authentication

```
$ aws ecr get-login-password --region ap-northeast-1 | sudo docker login --username AWS --password-stdin ****.dkr.ecr.ap-northeast-1.amazonaws.com
```

3. Docker build

```
$ docker build -t [repository-name] .
```

4. Tagging

```
$ docker tag [repository-name]:latest ****.dkr.ecr.ap-northeast-1.amazonaws.com/[repository-name]:latest
```

5. Push to ECR

```
sudo docker push *****.dkr.ecr.ap-northeast-1.amazonaws.com/[repository-name]:latest
```

---

### local test

- Run container

```
$ sudo docker run -p 5000:5000 [repository-name]
```

- Query from another terminal

```
$ curl http://localhost:5000
{"test":"test"}
```
