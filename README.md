# snow-report
An AWS Lambda function to query snow reports from local mountains. This consists of a simple python script that will query and parse the snow report, and a handler to allow this to be called as an AWS Lambda function.

## iOS Shortcuts
Since an API gateway can be provisioned for this function, a simple iOS shortcuts flow can call this and display the results on demand. The API returns JSON containg a list of objects, and the shortcut can parse through and display the data in a more readable format.

### Shortcut config
```yaml
url:
  - https://your.lambda.url.com
getContentsOfUrl:
  - headers:
    - x-api-key: your-api-key
repeatWithEach:
  - text: repeatItem[report]
  - setVariable: report
  - text:
    - repeatItem[name]
    - report[runs] runs
    - report[lifts] lifts
    - report[acres]
  - addToVariable:
    - result
showResult:
  - result 
```

### Shortcuts screenshots
![snow-report shortcuts icon](/assets/shortcutsIcon.JPG?raw=true)
![snow-report shortcuts REPORT](/assets/shortcutsReport.JPG?raw=true)

## Deploy
```
$ serverless deploy
```

## curl
```
$ curl -H "x-api-key: your-api-key" https://your.lambda.url.com
```

## Running locally
```
$ sls invoke local --function fetch
```
