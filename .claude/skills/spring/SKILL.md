---
name: spring
description: '**WORKFLOW SKILL** — Create, configure, and optimize Spring Framework applications. USE FOR: Spring Boot setup, dependency injection, REST APIs, data access, security, and microservices. DO NOT USE FOR: non-Spring Java development or general JVM tasks. INVOKES: file system tools for code generation/modification, terminal for Maven/Gradle commands, Spring configuration analysis.'
---

# Spring Framework Development Skill

## Overview

This skill supports Spring Framework development across the entire application lifecycle: from Spring Boot project setup to microservices architecture, REST APIs, data access, security configuration, and production deployment. It focuses on Spring Boot, Spring MVC, Spring Data, Spring Security, and Spring Cloud best practices.

## Key Capabilities

### Project Setup & Configuration
- Bootstrap Spring Boot applications with appropriate starters
- Configure application.properties/yml for different environments
- Set up multi-module Maven/Gradle projects
- Configure embedded servers (Tomcat, Jetty, Undertow) and ports
- Enable Spring profiles and conditional configuration

### Dependency Injection & IoC
- Create Spring beans with @Component, @Service, @Repository, @Controller
- Configure dependency injection with @Autowired, constructor injection
- Set up configuration classes with @Configuration and @Bean
- Implement factory patterns and custom bean scopes
- Handle circular dependency issues and bean lifecycle

### REST API Development
- Build REST controllers with @RestController and @RequestMapping
- Implement CRUD operations with proper HTTP methods and status codes
- Handle request/response bodies with @RequestBody/@ResponseBody
- Configure content negotiation and media types
- Add validation with Bean Validation and @Valid

### Data Access & Persistence
- Configure Spring Data JPA repositories and custom queries
- Set up database connections with H2, MySQL, PostgreSQL
- Implement transaction management with @Transactional
- Handle database migrations with Flyway or Liquibase
- Configure connection pooling and JDBC properties

### Security Implementation
- Configure Spring Security with authentication and authorization
- Implement JWT token-based authentication
- Set up OAuth2/OpenID Connect integration
- Configure method-level security with @PreAuthorize/@Secured
- Handle CORS, CSRF, and security headers

### Testing & Quality
- Write unit tests with @SpringBootTest and Testcontainers
- Create integration tests for REST endpoints
- Mock dependencies with @MockBean and Mockito
- Configure test profiles and test data setup
- Implement contract testing with Spring Cloud Contract

### Microservices & Cloud
- Set up Spring Cloud Config for centralized configuration
- Implement service discovery with Eureka or Consul
- Configure load balancing with Ribbon or Spring Cloud LoadBalancer
- Add circuit breakers with Resilience4j
- Implement distributed tracing with Spring Cloud Sleuth

## Usage Examples

### Create a Spring Boot REST API

```
Create a Spring Boot application with REST endpoints for managing products:
- GET /api/products - list all products
- POST /api/products - create new product
- GET /api/products/{id} - get product by ID
- PUT /api/products/{id} - update product
- DELETE /api/products/{id} - delete product
Include JPA entity, repository, service, and controller layers.
```

### Configure database connection

```
Set up MySQL database connection in application.yml with connection pooling, JPA properties, and Flyway migrations for a user management system.
```

### Implement Spring Security

```
Add JWT-based authentication to a Spring Boot REST API with login endpoint, token refresh, and protected resources using @PreAuthorize annotations.
```

### Create microservice architecture

```
Design a Spring Cloud microservices architecture with:
- Config Server for centralized configuration
- Eureka service discovery
- API Gateway with Spring Cloud Gateway
- Circuit breaker pattern with Resilience4j
```

## Common Patterns

### Spring Boot Application Structure

```java
@SpringBootApplication
public class ProductServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(ProductServiceApplication.class, args);
    }
}
```

### REST Controller with Validation

```java
@RestController
@RequestMapping("/api/products")
@Validated
public class ProductController {

    private final ProductService productService;

    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    @GetMapping
    public ResponseEntity<List<Product>> getAllProducts() {
        return ResponseEntity.ok(productService.findAll());
    }

    @PostMapping
    public ResponseEntity<Product> createProduct(@Valid @RequestBody ProductRequest request) {
        Product product = productService.create(request);
        return ResponseEntity.created(URI.create("/api/products/" + product.getId())).body(product);
    }
}
```

### JPA Repository with Custom Queries

```java
@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {

    @Query("SELECT p FROM Product p WHERE p.category = :category AND p.price BETWEEN :minPrice AND :maxPrice")
    List<Product> findByCategoryAndPriceRange(@Param("category") String category,
                                           @Param("minPrice") BigDecimal minPrice,
                                           @Param("maxPrice") BigDecimal maxPrice);

    @Modifying
    @Query("UPDATE Product p SET p.stockQuantity = p.stockQuantity - :quantity WHERE p.id = :id")
    int reduceStock(@Param("id") Long id, @Param("quantity") int quantity);
}
```

### Configuration Properties

```java
@ConfigurationProperties(prefix = "app.security")
public class SecurityProperties {
    private Jwt jwt = new Jwt();

    public static class Jwt {
        private String secret;
        private long expirationTime;

        // getters and setters
    }
}
```

## Best Practices

- Use constructor injection over field injection for better testability
- Keep controllers thin and delegate business logic to services
- Use DTOs for API requests/responses to decouple from entities
- Implement proper exception handling with @ControllerAdvice
- Use Spring profiles for environment-specific configuration
- Follow REST conventions and use appropriate HTTP status codes
- Implement proper logging with SLF4J and structured logging
- Use Spring Boot Actuator for monitoring and health checks
- Keep dependencies updated and use Spring Boot's dependency management

## Troubleshooting

### Common Spring Boot Issues

- **Application won't start**: Check for port conflicts, database connections, and circular dependencies
- **Bean creation errors**: Verify @ComponentScan packages and @Autowired dependencies
- **Database connection failures**: Check JDBC URL, credentials, and connection pool settings
- **Security configuration problems**: Ensure proper filter chain order and authentication setup

### REST API Issues

- **404 errors**: Verify @RequestMapping paths and HTTP methods
- **400 Bad Request**: Check @Valid validation and request body format
- **415 Unsupported Media Type**: Configure content negotiation properly
- **CORS errors**: Set up @CrossOrigin or global CORS configuration

### Performance Problems

- **Slow startup**: Reduce component scanning, use lazy initialization selectively
- **Memory leaks**: Check for improper bean scopes and resource cleanup
- **Database performance**: Optimize queries, use pagination, and connection pooling
- **Thread pool exhaustion**: Configure async executors and connection pools properly

### Testing Issues

- **Tests not running**: Check @SpringBootTest configuration and test dependencies
- **Mocking failures**: Use @MockBean correctly and avoid over-mocking
- **Integration test failures**: Ensure test database setup and cleanup

## Integration Points

- Spring Boot Starters (Web, Data JPA, Security, Cloud)
- Database: MySQL, PostgreSQL, MongoDB, Redis
- Messaging: RabbitMQ, Apache Kafka
- Cloud: AWS, Azure, GCP with Spring Cloud
- Monitoring: Spring Boot Actuator, Micrometer, Prometheus
- Testing: JUnit 5, Mockito, Testcontainers
- Build tools: Maven, Gradle
- IDE support: Spring Tools Suite, IntelliJ IDEA Spring plugins