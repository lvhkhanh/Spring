---
name: salesforce
description: '**WORKFLOW SKILL** — Create, deploy, and manage Salesforce applications and integrations. USE FOR: Salesforce development, Apex programming, Lightning components, data modeling, integration with external systems, and Salesforce administration. DO NOT USE FOR: non-Salesforce platforms, general programming, or unrelated CRM systems. INVOKES: terminal for Salesforce CLI commands, file system tools for metadata files, semantic search for Salesforce patterns.'
---

# Salesforce Development Skill

## Overview

This skill provides comprehensive support for Salesforce development, including Apex programming, Lightning component development, data modeling, integration, and platform administration. It covers best practices for building scalable, secure, and maintainable Salesforce applications and integrations.

## Key Capabilities

### Apex Development
- Write and debug Apex classes and triggers
- Implement SOQL and SOSL queries
- Handle bulk operations and governor limits
- Create custom controllers and extensions

### Lightning Development
- Build Lightning Web Components (LWC)
- Develop Aura components and applications
- Implement Lightning Data Service operations
- Create responsive user interfaces

### Data Modeling & Administration
- Design custom objects and relationships
- Configure page layouts and record types
- Set up validation rules and workflows
- Manage security and sharing models

### Integration & APIs
- Implement REST and SOAP API integrations
- Configure external data sources
- Set up connected apps and OAuth
- Handle data synchronization

## Usage Examples

### Apex Class with SOQL Query
```apex
public class AccountController {
    @AuraEnabled(cacheable=true)
    public static List<Account> getAccounts() {
        return [SELECT Id, Name, Type, Industry, AnnualRevenue
                FROM Account
                WHERE AnnualRevenue > 1000000
                ORDER BY AnnualRevenue DESC
                LIMIT 10];
    }
}
```

### Lightning Web Component
```javascript
// accountList.js
import { LightningElement, wire } from 'lwc';
import getAccounts from '@salesforce/apex/AccountController.getAccounts';

export default class AccountList extends LightningElement {
    @wire(getAccounts)
    accounts;

    get accountCount() {
        return this.accounts?.data?.length || 0;
    }
}
```

### DataWeave Transformation for Salesforce
```dataweave
%dw 2.0
output application/json
---
payload map (item) -> {
    Name: item.companyName,
    Type: item.customerType,
    Industry: item.businessSector,
    AnnualRevenue: item.revenue as Number,
    BillingStreet: item.address.street,
    BillingCity: item.address.city,
    BillingState: item.address.state,
    BillingPostalCode: item.address.zipCode,
    BillingCountry: item.address.country
}
```

## Common Patterns

### Bulk Data Processing
```apex
public class BulkDataProcessor {
    public static void processAccounts(List<Account> accounts) {
        List<Account> accountsToUpdate = new List<Account>();

        for(Account acc : accounts) {
            if(acc.AnnualRevenue == null) {
                acc.AnnualRevenue = 0;
                accountsToUpdate.add(acc);
            }
        }

        if(!accountsToUpdate.isEmpty()) {
            update accountsToUpdate;
        }
    }
}
```

### Lightning Component Communication
```javascript
// Parent Component
import { LightningElement } from 'lwc';

export default class ParentComponent extends LightningElement {
    handleAccountSelected(event) {
        const accountId = event.detail.accountId;
        // Handle account selection
    }
}

// Child Component
import { LightningElement, api } from 'lwc';

export default class ChildComponent extends LightningElement {
    @api account;

    handleSelect() {
        this.dispatchEvent(new CustomEvent('accountselected', {
            detail: { accountId: this.account.Id }
        }));
    }
}
```

### Integration with External Systems
```apex
public class ExternalSystemIntegration {
    @future(callout=true)
    public static void syncToExternalSystem(Id accountId) {
        Account acc = [SELECT Id, Name, Type FROM Account WHERE Id = :accountId];

        HttpRequest req = new HttpRequest();
        req.setEndpoint('https://api.external-system.com/accounts');
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');
        req.setBody(JSON.serialize(acc));

        Http http = new Http();
        HttpResponse res = http.send(req);

        if(res.getStatusCode() == 200) {
            // Success handling
        } else {
            // Error handling
        }
    }
}
```

## Best Practices

### Apex Development
- Always bulkify operations to handle governor limits
- Use selective SOQL queries to avoid performance issues
- Implement proper error handling and logging
- Follow naming conventions and code organization

### Lightning Development
- Use Lightning Data Service for better performance
- Implement proper component communication patterns
- Optimize bundle sizes and loading performance
- Follow accessibility guidelines

### Security & Governance
- Implement proper sharing rules and field-level security
- Use platform encryption for sensitive data
- Follow least privilege principles
- Regular security reviews and penetration testing

### Data Management
- Implement data validation at multiple levels
- Use platform features for data integrity
- Plan for data archiving and cleanup
- Monitor data usage and storage limits

## Troubleshooting

### Governor Limit Issues
- **Problem**: Apex hitting execution limits
- **Solution**: Bulkify operations, use @future for callouts, optimize SOQL queries
- **Prevention**: Monitor limits in development, implement efficient algorithms

### Lightning Component Performance
- **Problem**: Slow component loading or rendering
- **Solution**: Optimize bundle sizes, use Lightning Data Service, implement lazy loading
- **Prevention**: Regular performance testing, code splitting, efficient data fetching

### Integration Failures
- **Problem**: API calls failing or timing out
- **Solution**: Implement retry logic, proper error handling, monitor API limits
- **Prevention**: Circuit breaker patterns, proper timeout handling, rate limiting

### Data Synchronization Issues
- **Problem**: Data inconsistencies between systems
- **Solution**: Implement proper error handling, logging, and reconciliation processes
- **Prevention**: Transaction management, data validation, monitoring and alerting

## Integration Points

### Development Tools
- **Salesforce CLI**: Command-line interface for development and deployment
- **VS Code Extensions**: Salesforce-specific development tools
- **DevOps Tools**: CI/CD pipelines for automated deployment

### Platform Features
- **Salesforce APIs**: REST, SOAP, Bulk, and Streaming APIs
- **AppExchange**: Third-party applications and components
- **Salesforce Connect**: External data source integration

### External Systems
- **ERP Systems**: SAP, Oracle, Microsoft Dynamics
- **Marketing Tools**: Marketo, HubSpot, Mailchimp
- **Communication Platforms**: Slack, Microsoft Teams, email systems

### Cloud Platforms
- **AWS**: Lambda functions, S3 storage, API Gateway
- **Azure**: Functions, Blob storage, API Management
- **Google Cloud**: Cloud Functions, Cloud Storage, API Gateway