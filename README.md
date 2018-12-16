# snow-report
An AWS Lambda function to query snow reports from local mountains. This consists of a simple python script that will query and parse the snow report, and a handler to allow this to be called as an AWS Lambda function.

## iOS Shortcuts
Since an API gateway can be provisioned for this function, a simple iOS shortcuts flow can call this and display the results on demand. This was the intended usage when writting this script.

### Shortcuts config
`URL`-> `Get Contents of URL` (with the api key in the header) -> `Show Result` (Contents of URL)

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
