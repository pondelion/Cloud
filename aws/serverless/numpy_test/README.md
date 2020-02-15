
- serverlessをグローバルにインストール
```
$ npm install -g serverless
```

- serverlessプロジェクト作成
```
$ serverless create --template aws-python3 --name numpy-test
```

```
$ cd numpy-test
```

- 必要なPythonライブラリインストール
```
$ pipenv --python 3.8
$ pipenv shell
$ pipenv install numpy
```

- serverless-python-requirementsインストール
```
$ npm install --save serverless-python-requirements
```

- デプロイ
```
$ sls deploy

Serverless: Generating requirements.txt from Pipfile...
Serverless: Adding Python requirements helper...
Serverless: Parsed requirements.txt from Pipfile in /home/username/..../requirements.txt...
Serverless: Using static cache of requirements found at /home/username/.cache/serverless-python-requirements/a40d54308da7be6f39484950d74cfe0bc47181c918fee1439dd220432bf6d2bf_slspyc ...
Serverless: Zipping required Python packages...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Removing Python requirements helper...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service numpy-test.zip file to S3 (13.1 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
...............
Serverless: Stack update finished...
Service Information
service: numpy-test
stage: dev
region: ap-northeast-1
stack: numpy-test-dev
resources: 6
api keys:
  None
endpoints:
  None
functions:
  hello: numpy-test-dev-hello
layers:
  None
Serverless: Run the "serverless" command to setup monitoring, troubleshooting and testing.
```

- 呼び出し
```
$ sls invoke -f hello --log

{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v1.0! Your function executed successfully!\", \"input\": {}, \"os.listdir('.')\": [\".requirements.zip\", \"Pipfile\", \"Pipfile.lock\", \"README.md\", \"handler.py\", \"node_modules\", \"unzip_requirements.py\"]}"
}
--------------------------------------------------------------------
START RequestId: 0403453f-5d18-4834-a8ec-77c22a96450c Version: $LATEST
[0 1 2 3 4 5 6 7 8 9]
END RequestId: 0403453f-5d18-4834-a8ec-77c22a96450c
REPORT RequestId: 0403453f-5d18-4834-a8ec-77c22a96450c  Duration: 1.32 ms       Billed Duration: 100 ms Memory Size: 1024 MB    Max Memory Used: 148 MB
```


下記の権限をIAMで付与必要  
  
- S3
- IAM
- CloudWatchLog
- CloudFormation
- Lambda