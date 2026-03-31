---
name: mulesoft
description: '**WORKFLOW SKILL** — Create, deploy, and manage MuleSoft integration applications and APIs. USE FOR: Mule application development, API design and management, DataWeave transformations, Anypoint Platform operations, and integration flows. DO NOT USE FOR: non-MuleSoft integration platforms, general programming, or local development outside Mule context. INVOKES: terminal for Mule commands, file system tools for configuration files, semantic search for MuleSoft patterns.'
---

# MuleSoft Integration Development Skill

## Overview

This skill provides comprehensive support for MuleSoft integration development, API management, and enterprise application connectivity. It covers Mule application development, DataWeave transformations, Anypoint Platform operations, and best practices for scalable, secure, and maintainable integration solutions.

## Key Capabilities

### Mule Application Development
- Design and implement Mule flows and subflows
- Configure connectors for various systems (HTTP, Database, JMS, etc.)
- Implement error handling and exception strategies
- Create custom components and transformers

### API Design & Management
- Design REST and SOAP APIs with RAML/OAS specifications
- Implement API policies and security
- Set up API gateways and proxy endpoints
- Manage API versions and lifecycle

### DataWeave Transformations
- Transform data between different formats (JSON, XML, CSV)
- Implement complex mapping and filtering logic
- Handle data validation and error scenarios
- Optimize transformation performance

### Anypoint Platform Operations
- Deploy applications to CloudHub and Runtime Fabric
- Configure environments and deployment strategies
- Monitor application performance and health
- Manage runtime versions and patches

## Usage Examples

### Create Mule Application
```xml
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.mulesoft.org/schema/mule/core
      http://www.mulesoft.org/schema/mule/core/current/mule.xsd">

    <flow name="exampleFlow">
        <http:listener config-ref="HTTP_Listener_config" path="/api/test"/>
        <set-payload value="Hello World!" doc:name="Set Payload"/>
        <logger level="INFO" message="Payload: #[payload]" doc:name="Logger"/>
    </flow>
</mule>
```

### DataWeave Transformation
```dataweave
%dw 2.0
output application/json
---
{
    userId: payload.user_id,
    fullName: payload.first_name ++ " " ++ payload.last_name,
    email: payload.email,
    status: if (payload.active) "ACTIVE" else "INACTIVE",
    createdDate: payload.created_at as DateTime
}
```

### API Specification (RAML)
```raml
#%RAML 1.0
title: User API
version: v1
/users:
  get:
    description: Get all users
    responses:
      200:
        body:
          application/json:
            type: array
            items: User
  post:
    description: Create a new user
    body:
      application/json:
        type: User
    responses:
      201:
        body:
          application/json:
            type: User

types:
  User:
    type: object
    properties:
      id: integer
      name: string
      email: string
```

## Common Patterns

### Error Handling Flow
```xml
<flow name="errorHandlingFlow">
    <try doc:name="Try Scope">
        <http:request config-ref="HTTP_Request_config" path="/external-api" method="GET"/>
        <set-payload value="#[payload]" doc:name="Process Response"/>
        <catch-exception-strategy doc:name="Catch Exception Strategy">
            <set-payload value="#[{error: 'Service unavailable', code: 500}]" doc:name="Set Error Response"/>
            <logger level="ERROR" message="Error occurred: #[error.description]" doc:name="Log Error"/>
        </catch-exception-strategy>
    </try>
</flow>
```

### Database Integration
```xml
<flow name="databaseFlow">
    <http:listener config-ref="HTTP_Listener_config" path="/users"/>
    <db:select config-ref="Database_Config" doc:name="Select Users">
        <db:sql>SELECT * FROM users WHERE active = 1</db:sql>
    </db:select>
    <ee:transform doc:name="Transform to JSON">
        <ee:message>
            <ee:set-payload><![CDATA[%dw 2.0
output application/json
---
payload map ((user) -> {
    id: user.id,
    name: user.name,
    email: user.email
})]]></ee:set-payload>
        </ee:message>
    </ee:transform>
</flow>
```

### API Policy Implementation
```xml
<api-platform-gw:api api-ref="user-api" doc:name="API Autodiscovery"/>
<policy:client-id-enforcement doc:name="Client ID Enforcement">
    <policy:client-id-expression>#[attributes.headers['client_id']]</policy:client-id-expression>
    <policy:client-secret-expression>#[attributes.headers['client_secret']]</policy:client-secret-expression>
</policy:client-id-enforcement>
<policy:rate-limiting doc:name="Rate Limiting">
    <policy:rate-limit-window>60</policy:rate-limit-window>
    <policy:rate-limit-requests>100</policy:rate-limit-requests>
</policy:rate-limiting>
```

## Best Practices

### Application Structure
- Use consistent naming conventions for flows and components
- Implement proper error handling at all levels
- Use configuration properties for environment-specific values
- Document flows and components with meaningful descriptions

### Performance Optimization
- Use streaming for large data processing
- Implement caching for frequently accessed data
- Optimize DataWeave transformations for performance
- Monitor memory usage and connection pools

### Security Implementation
- Use HTTPS for all external communications
- Implement proper authentication and authorization
- Validate input data to prevent injection attacks
- Use secure property placeholders for sensitive data

### Testing Strategy
- Write unit tests for custom components
- Use MUnit for integration testing
- Test error scenarios and edge cases
- Automate testing in CI/CD pipelines

## Troubleshooting

### Common Mule Runtime Issues
- **Memory Issues**: Monitor heap usage and adjust JVM settings
- **Connection Pool Exhaustion**: Configure appropriate pool sizes
- **Timeout Errors**: Adjust timeout values and implement retry logic
- **Transformation Errors**: Validate DataWeave expressions and input data

### Deployment Problems
- **Environment Configuration**: Ensure all properties are properly configured
- **Dependency Issues**: Check connector versions and compatibility
- **Resource Constraints**: Verify CPU and memory allocation
- **Network Connectivity**: Test connectivity to external systems

### API Management Issues
- **Policy Conflicts**: Review policy ordering and configuration
- **Rate Limiting**: Monitor usage patterns and adjust limits
- **Version Compatibility**: Ensure API versions are properly managed
- **Security Violations**: Check authentication and authorization settings

### DataWeave Problems
- **Type Mismatches**: Validate data types in transformations
- **Null Pointer Exceptions**: Handle null values appropriately
- **Performance Issues**: Optimize complex transformations
- **Syntax Errors**: Use DataWeave playground for testing

## Integration Points

### Development Tools
- **Anypoint Studio**: IDE for Mule application development
- **DataWeave Playground**: Tool for testing transformations
- **API Designer**: Tool for designing and documenting APIs
- **MUnit**: Testing framework for Mule applications

### Runtime Environments
- **CloudHub**: MuleSoft's cloud runtime platform
- **Runtime Fabric**: Container-based runtime for hybrid deployments
- **Runtime Manager**: Tool for managing and monitoring applications
- **Anypoint Platform**: Unified platform for API management and integration

### Connectors and Systems
- **Database Connectors**: Support for various database systems
- **Messaging Connectors**: Integration with JMS, AMQP, and Kafka
- **Cloud Connectors**: AWS, Azure, and GCP service integration
- **ERP Connectors**: SAP, Salesforce, and other enterprise systems

### Monitoring and Analytics
- **Anypoint Monitoring**: Application performance and health monitoring
- **API Analytics**: Usage analytics and performance metrics
- **Custom Dashboards**: Business intelligence and reporting
- **Alert Management**: Proactive issue detection and notification