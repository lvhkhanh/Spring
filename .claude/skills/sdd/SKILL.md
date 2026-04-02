---
name: sdd
description: '**WORKFLOW SKILL** — Create, manage, and implement specification-driven development processes. USE FOR: writing requirements specifications, creating design documents, implementing test-driven development from specs, managing specification changes, and ensuring compliance with requirements. DO NOT USE FOR: general programming without specifications, agile development without documentation, or unstructured development approaches. INVOKES: file system tools for specification document creation/modification, terminal for documentation tools, semantic search for requirement analysis.'
---

# Specification-Driven Development Skill

## Overview

This skill provides comprehensive support for specification-driven development (SDD) methodologies, focusing on creating clear requirements, design specifications, and ensuring implementation compliance. It emphasizes documentation-driven development with traceability from requirements to code.

## Key Capabilities

### Requirements Engineering
- Write clear, testable requirements and user stories
- Create functional and non-functional requirement specifications
- Develop acceptance criteria and validation rules
- Establish requirement traceability matrices

### Specification Documentation
- Create detailed design specifications and technical documents
- Develop API specifications and interface contracts
- Write system architecture and component specifications
- Create data models and database schemas from requirements

### Test-Driven Implementation
- Generate test cases from specifications before implementation
- Create acceptance tests based on requirements
- Implement code that satisfies specification criteria
- Validate implementation against requirements

### Change Management
- Track specification changes and version control
- Assess impact of requirement modifications
- Update documentation and tests for changes
- Maintain requirement traceability through changes

### Quality Assurance
- Verify implementation compliance with specifications
- Perform requirement validation and verification
- Conduct specification reviews and walkthroughs
- Generate compliance reports and documentation

## Usage Examples

### Requirements Specification
```
Create a requirements specification for a user authentication system with the following features:
- User registration with email verification
- Login/logout functionality
- Password reset capability
- Session management
```

### Design Specification from Requirements
```
Based on the authentication requirements, create a detailed design specification including:
- Database schema for users and sessions
- API endpoints and request/response formats
- Security measures and validation rules
- Error handling and user feedback
```

### Test Case Generation
```
Generate comprehensive test cases for the authentication system covering:
- Happy path scenarios
- Edge cases and error conditions
- Security validation
- Performance requirements
```

## Common Patterns

### Specification Template Structure
```markdown
# System Specification Document

## 1. Introduction
- Purpose and scope
- Definitions and acronyms
- References

## 2. Requirements
- Functional requirements
- Non-functional requirements
- Interface requirements

## 3. Design Specifications
- System architecture
- Component design
- Data models

## 4. Implementation Guidelines
- Coding standards
- Testing requirements
- Deployment procedures

## 5. Validation & Verification
- Test plans
- Acceptance criteria
- Compliance checks
```

### Requirement Format
```
REQ-AUTH-001: User Registration
Description: System shall allow new users to register with email and password
Acceptance Criteria:
- Email format validation
- Password strength requirements
- Duplicate email prevention
- Verification email sent
Priority: High
```

### Test Specification Template
```gherkin
Feature: User Authentication
  As a user
  I want to authenticate securely
  So that I can access protected resources

  Scenario: Successful user registration
    Given I am on the registration page
    When I enter valid registration details
    And I submit the form
    Then I should receive a verification email
    And my account should be created in pending status
```

## Best Practices

### Requirements Management
- Use clear, unambiguous language in requirements
- Make requirements testable and measurable
- Maintain requirement traceability throughout development
- Involve stakeholders in requirement validation

### Documentation Standards
- Follow consistent document templates and formats
- Use version control for all specifications
- Maintain document change logs and approval records
- Keep documentation synchronized with code changes

### Implementation Compliance
- Implement features to exactly match specifications
- Create automated tests from acceptance criteria
- Document any deviations from specifications
- Perform regular compliance reviews

### Change Control
- Establish formal change request processes
- Assess impact of specification changes
- Update all affected documents and tests
- Communicate changes to all stakeholders

## Troubleshooting

### Requirement Ambiguity Issues
- Break down vague requirements into specific, measurable criteria
- Add examples and acceptance criteria to clarify intent
- Conduct requirement walkthroughs with stakeholders
- Create mockups or prototypes to validate understanding

### Specification Drift
- Establish regular review cycles for specifications
- Implement automated checks for specification compliance
- Use version control to track specification changes
- Maintain clear audit trails for all modifications

### Implementation Gaps
- Perform regular gap analysis between specs and implementation
- Create detailed implementation checklists
- Implement automated validation against specifications
- Schedule regular compliance audits

### Stakeholder Communication
- Establish clear communication channels for requirement changes
- Create regular status reports and progress updates
- Schedule stakeholder review meetings
- Document all decisions and rationales

## Integration Points

### Development Tools
- **Requirements Management**: Jira, Azure DevOps, IBM DOORS Next
- **Documentation**: Confluence, SharePoint, GitBook
- **Version Control**: Git with specification files
- **IDE Integration**: VS Code with specification extensions

### Testing Frameworks
- **BDD Tools**: Cucumber, SpecFlow, Behave
- **Test Management**: TestRail, Zephyr, qTest
- **API Testing**: Postman with specification validation
- **Automated Testing**: Selenium, Cypress with spec-driven tests

### Documentation Tools
- **Diagramming**: Draw.io, Lucidchart, PlantUML
- **API Documentation**: Swagger/OpenAPI, API Blueprint
- **Technical Writing**: Markdown, AsciiDoc, LaTeX
- **Review Tools**: GitHub PR reviews, Google Docs comments

### Project Management
- **Agile Tools**: Jira, Trello with specification epics
- **Change Management**: ServiceNow, Remedy for requirement changes
- **Compliance**: Audit tools, compliance reporting systems
- **Reporting**: Power BI, Tableau for specification metrics