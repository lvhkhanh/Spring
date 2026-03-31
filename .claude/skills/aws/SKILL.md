---
name: aws
description: '**WORKFLOW SKILL** — Create, deploy, and manage Amazon Web Services applications and infrastructure. USE FOR: AWS service configuration, Lambda deployment, EC2/S3 management, CloudFormation templates, IAM policies, and infrastructure as code. DO NOT USE FOR: non-AWS cloud platforms, general programming, or local development. INVOKES: terminal for AWS CLI commands, file system tools for configuration files, semantic search for AWS patterns.'
---

# Amazon Web Services Development Skill

## Overview

This skill provides comprehensive support for Amazon Web Services development, deployment, and operations. It covers infrastructure as code, serverless computing, data analytics, and cloud-native application development with best practices for scalability, security, and cost optimization.

## Key Capabilities

### Infrastructure as Code
- Deploy Lambda functions, ECS services, and EC2 instances
- Configure S3 buckets, DynamoDB tables, and SQS queues
- Set up VPC networks, subnets, and security groups
- Manage IAM roles, policies, and users

### Application Development
- Build serverless applications with Lambda and API Gateway
- Create data pipelines with Glue and Kinesis
- Implement microservices with ECS and EKS
- Develop ML models with SageMaker and Rekognition

### Data & Analytics
- Design DynamoDB schemas and optimize queries
- Build data lakes with S3 and Athena
- Create dashboards with QuickSight and CloudWatch
- Implement real-time analytics with Kinesis and Elasticsearch

### DevOps & Operations
- Set up CI/CD pipelines with CodePipeline and CodeBuild
- Configure monitoring with CloudWatch and X-Ray
- Implement security with WAF and Shield
- Manage costs with Cost Explorer and budget alerts

## Usage Examples

### Deploy Lambda Function
```bash
# Deploy a Python Lambda function
aws lambda create-function \
  --function-name my-function \
  --runtime python3.9 \
  --role arn:aws:iam::123456789012:role/lambda-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip
```

### Create S3 Bucket
```bash
# Create an S3 bucket with versioning enabled
aws s3 mb s3://my-bucket
aws s3api put-bucket-versioning \
  --bucket my-bucket \
  --versioning-configuration Status=Enabled
```

### CloudFormation Template
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyBucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: my-application-bucket
      VersioningConfiguration:
        Status: Enabled
```

## Common Patterns

### Serverless API with Lambda and API Gateway
```python
import json
import boto3

def lambda_handler(event, context):
    # Handle API Gateway request
    body = json.loads(event['body'])
    
    # Process data with DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('my-table')
    
    # Return response
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Success'})
    }
```

### Infrastructure as Code with CDK
```typescript
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';

export class MyStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create Lambda function
    const myFunction = new lambda.Function(this, 'MyFunction', {
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset('lambda'),
      handler: 'index.handler',
    });

    // Create API Gateway
    const api = new apigateway.RestApi(this, 'MyApi');
    const integration = new apigateway.LambdaIntegration(myFunction);
    api.root.addMethod('GET', integration);
  }
}
```

### Data Pipeline with Glue
```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read data from S3
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="my_database",
    table_name="my_table"
)

# Transform data
transformed = datasource.apply_mapping([
    ("col1", "string", "col1", "string"),
    ("col2", "int", "col2", "int")
])

# Write to S3
glueContext.write_dynamic_frame.from_options(
    frame=transformed,
    connection_type="s3",
    connection_options={"path": "s3://my-bucket/output/"},
    format="parquet"
)

job.commit()
```

## Best Practices

### Security
- Use IAM roles with least privilege principle
- Enable encryption for data at rest and in transit
- Implement multi-factor authentication
- Regularly rotate access keys and certificates

### Cost Optimization
- Use reserved instances for predictable workloads
- Implement auto-scaling for variable loads
- Monitor usage with Cost Explorer and Trusted Advisor
- Clean up unused resources regularly

### Performance
- Choose appropriate instance types for workloads
- Use CloudFront for global content delivery
- Implement caching with ElastiCache and CloudFront
- Optimize database queries and indexes

### Reliability
- Design for failure with multi-AZ deployments
- Implement backup and disaster recovery strategies
- Use health checks and auto-healing
- Monitor with CloudWatch alarms and dashboards

## Troubleshooting

### Lambda Function Issues
- **Cold start problems**: Use provisioned concurrency for predictable performance
- **Timeout errors**: Increase timeout limits or optimize function code
- **Memory issues**: Monitor memory usage and adjust allocation
- **Permission errors**: Check IAM roles and policies

### S3 Access Problems
- **403 Forbidden**: Verify bucket policies and IAM permissions
- **404 Not Found**: Check bucket name and region
- **Slow uploads**: Use multipart upload for large files
- **CORS issues**: Configure CORS policy for web applications

### CloudFormation Deployment Failures
- **Template validation errors**: Check syntax and required parameters
- **Resource creation failures**: Review CloudTrail logs for detailed errors
- **Stack update issues**: Use change sets for safe updates
- **Dependency problems**: Ensure proper resource ordering

### Database Performance Issues
- **Slow queries**: Analyze with RDS Performance Insights
- **Connection limits**: Monitor connection pools and usage
- **Storage issues**: Monitor disk space and IOPS
- **Replication lag**: Check replica status and network latency

## Integration Points

### Development Tools
- **AWS CLI**: Command-line interface for AWS services
- **AWS SDKs**: Language-specific libraries for AWS integration
- **AWS CDK**: Infrastructure as code with programming languages
- **AWS SAM**: Serverless application model for Lambda development

### Cloud Platforms
- **Multi-cloud deployments**: Integration with other cloud providers
- **Hybrid cloud**: Connection to on-premises infrastructure
- **Edge computing**: Integration with AWS Outposts and Wavelength

### Frameworks and Libraries
- **Spring Cloud AWS**: Spring integration for AWS services
- **Boto3**: Python SDK for AWS services
- **AWS SDK for JavaScript**: Node.js integration
- **Terraform AWS Provider**: Infrastructure as code

### Data Sources and Destinations
- **Database integration**: RDS, DynamoDB, Redshift connections
- **Data lakes**: S3-based data lake architectures
- **Streaming data**: Kinesis and MSK integration
- **External APIs**: API Gateway for third-party integrations

### DevOps and CI/CD
- **CodePipeline**: AWS-native CI/CD pipelines
- **GitHub Actions**: AWS deployment workflows
- **Jenkins**: AWS plugin ecosystem
- **GitLab CI**: AWS runner integration