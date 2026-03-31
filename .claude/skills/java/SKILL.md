---
name: java
description: '**WORKFLOW SKILL** — Create, refactor, debug, and optimize Java applications and libraries. USE FOR: writing classes, interfaces, packages, unit tests, build scripts, dependency management, and JVM debugging. DO NOT USE FOR: non-Java languages or JVM-irrelevant tasks. INVOKES: file system tools for code generation/modification, terminal for Maven/Gradle commands, language analysis for refactorings and diagnostics.'
---

# Java Development Skill

## Overview

This skill supports Java development across the entire lifecycle: from new class generation to architecture, testing, dependency management, and production debugging. It aims for idiomatic Java, stable builds, and maintainable application structure.

## Key Capabilities

### Code Generation
- Create Java classes, interfaces, enums, and records from requirements
- Generate constructors, getters/setters, builders, and standard `toString`/`equals`/`hashCode`
- Implement design patterns (Singleton, Factory, Strategy, Visitor, etc.)
- Generate Javadoc comments and API-level documentation stubs

### Project Setup
- Scaffold Maven and Gradle projects
- Configure dependency management (Maven pom.xml, Gradle build.gradle)
- Set source/target compatibility (Java 8-21+)
- Add modules and multi-module project structure

### Testing & Quality
- Write JUnit 5 and Mockito tests
- Create integration tests with Testcontainers and Spring Boot Test
- Enforce code style with Checkstyle, SpotBugs, PMD, and Google Java Format
- Add analysis for SonarQube rules and static checkers

### Refactoring
- Extract methods, classes, and constants
- Apply SOLID principles and clean architecture
- Convert loops to streams and vice versa when appropriate
- Remove duplication and improve naming and encapsulation

### Debugging & Troubleshooting
- Diagnose common exceptions (NullPointerException, ClassNotFoundException, ConcurrentModificationException)
- Interpret stack traces and log output
- Use `jdb`, remote debugging, and IDE breakpoints effectively
- Tune GC settings and memory diagnostics for JVM applications

### Build & Deployment
- Run Maven/Gradle commands (`clean install`, `test`, `package`, `bootJar`)
- Create CI pipelines (GitHub Actions, GitLab CI, Jenkins) with Java workflow examples
- Build Docker images for Java apps
- Apply deployment best practices for Spring Boot and Java microservices

## Usage Examples

### Create a simple service class

```
Create a Java class `UserService` in package `com.example.service` with methods:
- `User findById(String id)`
- `List<User> findAll()`
- `void save(User user)`
Include constructor injection for `UserRepository`.
```

### Add a JUnit test

```
Add JUnit 5 tests for `UserService` and mock `UserRepository` with Mockito. Verify `findById` returns the expected user and `save` calls repository save method.
```

### Refactor a legacy method

```
Refactor method `public BigDecimal computeDiscount(Order order)` in `OrderCalculator` to apply different discount tiers without nested if statements.
```

### Fix compilation error

```
Resolve "package com.example.util does not exist" in `InvoiceProcessor`. Suggest updated package layout and imports.
```

## Common Patterns

### Try-with-resources

```java
try (BufferedReader reader = Files.newBufferedReader(path)) {
    return reader.lines().collect(Collectors.toList());
}
```

### Stream processing

```java
List<String> names = users.stream()
    .filter(u -> u.isActive())
    .map(User::getName)
    .sorted()
    .collect(Collectors.toList());
```

### Optional usage

```java
Optional<User> maybeUser = userRepository.findById(id);
return maybeUser.orElseThrow(() -> new NoSuchElementException("User not found"));
```

### Spring Boot REST controller

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable String id) {
        return ResponseEntity.ok(userService.findById(id));
    }
}
```

## Best Practices

- Prefer immutable objects and avoid public field mutation
- Validate inputs and fail fast
- Keep methods short (ideally < 20 lines) and focused
- Use meaningful names for variables, methods, and classes
- Favor composition over inheritance
- Keep dependencies up to date and avoid version conflicts
- Incremental and repeatable tests: unit, integration, contract

## Troubleshooting

### Common compile-time issues

- `cannot find symbol` → fix import/package names and classpath
- `incompatible types` → ensure generics are correctly parameterized
- `method does not override or implement a method from a supertype` → check `@Override` and method signatures

### Runtime exceptions

- `NullPointerException` → add null checks, use `Objects.requireNonNull`, and `Optional`
- `ClassNotFoundException` / `NoClassDefFoundError` → fix classpath and dependency scope
- `ConcurrentModificationException` → avoid modifying collections during iteration; use `Iterator` or concurrent collections

### Build issues

- Maven version mismatch: align `maven.compiler.source` and `target`
- Dependency resolution failure: clear local cache (`mvn dependency:purge-local-repository`) and retry
- Spring Boot startup failure: inspect `application.properties` and embedded server port conflicts

## Integration Points

- Spring Boot / Spring MVC / WebFlux
- Jakarta EE / Jakarta RESTful Web Services
- Hibernate/JPA, JDBC, MyBatis
- Messaging: Kafka, RabbitMQ, ActiveMQ
- Cloud SDKs: AWS, GCP, Azure
- Testing: JUnit 5, Mockito, Testcontainers
- Build tools: Maven, Gradle
- Monitoring: Micrometer, Prometheus, New Relic
