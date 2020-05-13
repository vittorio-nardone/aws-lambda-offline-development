# OFFLINE LAMBDA DEVELOPMENT

A simple docker environment to offline develop and test python AWS Lambda functions.

![Lambda Execution](https://www.vittorionardone.it/wp-content/uploads/2020/05/lambda-offline-execution-2-1536x874.png)

More datails on [this post](https://www.vittorionardone.it/en/2020/05/12/aws-lambda-offline-development-with-docker/) on my Digital Transformation Blog.

### CloudFormation Lambda sample definition

```
    SampleFunction:
        Type: AWS::Lambda::Function
        Properties:
            Runtime: python3.7
            Description: This is an amazing function
            Handler: src/lambda_function.lambda_handler
            Role: 
                Fn::GetAtt: [ "SampleFunctionRole", "Arn" ]
            Environment:
                Variables:
                    PYTHONPATH: "/var/task/src:/var/task/lib"
            Timeout: 20
            MemorySize: 512
            Code:
                S3Bucket: 
                    Ref: SourceBucket
                S3Key: 
                    Fn::Sub: '${SourceBucketFolder}/SampleFunction.zip'
```
