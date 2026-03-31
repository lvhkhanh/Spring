---
name: dotnet
description: '**WORKFLOW SKILL** — Create, refactor, debug, and optimize .NET applications and libraries. USE FOR: building web APIs, console apps, class libraries, and services; implementing C# patterns and best practices; managing NuGet packages and dependencies; debugging runtime issues; setting up project structure and configuration. DO NOT USE FOR: non-.NET languages, low-level system programming, or infrastructure provisioning. INVOKES: file system tools for project creation/modification, terminal for dotnet CLI commands, language analysis for C# refactoring and diagnostics.'
---

# .NET Development Skill

## Overview

This skill provides complete support for .NET development tasks across web applications, APIs, console applications, and class libraries. It is optimized for clean, maintainable C# code and modern .NET patterns.

## Key Capabilities

### Project Creation & Setup
- Create .NET projects: Web API, MVC, Console, Class Library, Worker Service
- Setup project structure with proper folder organization
- Configure appsettings.json, launchSettings.json, and environment-specific settings
- Initialize git repository and add .gitignore for .NET projects

### Code Generation
- Build C# classes, interfaces, and records with proper naming conventions
- Implement dependency injection patterns and service registration
- Create controllers, services, repositories, and data transfer objects
- Generate async/await patterns for I/O operations

### Architecture & Patterns
- Apply SOLID principles and clean architecture
- Implement repository pattern, unit of work, and CQRS
- Create layered architecture: API, Application, Domain, Infrastructure
- Use dependency injection and service locator patterns

### Testing & Quality
- Add xUnit/NUnit test projects and test classes
- Write unit, integration, and end-to-end tests
- Use Moq for mocking and FluentAssertions for assertions
- Implement test fixtures and data-driven tests

### Debugging & Troubleshooting
- Identify compilation errors and runtime exceptions
- Debug async/await deadlocks and threading issues
- Fix dependency injection configuration problems
- Diagnose performance issues and memory leaks

### Tooling & Deployment
- Manage NuGet packages and package references
- Configure build pipelines and CI/CD workflows
- Setup Docker containers for .NET applications
- Handle publishing and deployment configurations

## Usage Examples

### Web API from requirement
```
Create a REST API for managing products with CRUD operations, including validation and error handling.
```

### Refactor to clean architecture
```
Refactor a monolithic controller into separate service, repository, and DTO layers with proper dependency injection.
```

### Add comprehensive testing
```
Add unit tests for a service class with mocking of external dependencies and edge case coverage.
```

## Common Patterns

### Dependency Injection Setup
```csharp
// Program.cs or Startup.cs
builder.Services.AddScoped<IProductService, ProductService>();
builder.Services.AddScoped<IProductRepository, ProductRepository>();
```

### Repository Pattern
```csharp
public interface IProductRepository
{
    Task<Product?> GetByIdAsync(int id);
    Task<IEnumerable<Product>> GetAllAsync();
    Task AddAsync(Product product);
    Task UpdateAsync(Product product);
    Task DeleteAsync(int id);
}

public class ProductRepository : IProductRepository
{
    private readonly ApplicationDbContext _context;

    public ProductRepository(ApplicationDbContext context)
    {
        _context = context;
    }

    // Implementation methods...
}
```

### Service Layer
```csharp
public interface IProductService
{
    Task<ProductDto?> GetProductAsync(int id);
    Task<IEnumerable<ProductDto>> GetProductsAsync();
    Task CreateProductAsync(CreateProductDto dto);
    Task UpdateProductAsync(int id, UpdateProductDto dto);
    Task DeleteProductAsync(int id);
}

public class ProductService : IProductService
{
    private readonly IProductRepository _repository;
    private readonly ILogger<ProductService> _logger;

    public ProductService(IProductRepository repository, ILogger<ProductService> logger)
    {
        _repository = repository;
        _logger = logger;
    }

    // Implementation methods...
}
```

### Controller with Validation
```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    private readonly IProductService _service;

    public ProductsController(IProductService service)
    {
        _service = service;
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<ProductDto>> GetProduct(int id)
    {
        var product = await _service.GetProductAsync(id);
        if (product == null)
            return NotFound();

        return Ok(product);
    }

    [HttpPost]
    public async Task<ActionResult<ProductDto>> CreateProduct(CreateProductDto dto)
    {
        if (!ModelState.IsValid)
            return BadRequest(ModelState);

        var product = await _service.CreateProductAsync(dto);
        return CreatedAtAction(nameof(GetProduct), new { id = product.Id }, product);
    }
}
```

### Unit Test Example
```csharp
public class ProductServiceTests
{
    private readonly Mock<IProductRepository> _repositoryMock;
    private readonly Mock<ILogger<ProductService>> _loggerMock;
    private readonly ProductService _service;

    public ProductServiceTests()
    {
        _repositoryMock = new Mock<IProductRepository>();
        _loggerMock = new Mock<ILogger<ProductService>>();
        _service = new ProductService(_repositoryMock.Object, _loggerMock.Object);
    }

    [Fact]
    public async Task GetProductAsync_ExistingId_ReturnsProduct()
    {
        // Arrange
        var productId = 1;
        var expectedProduct = new Product { Id = productId, Name = "Test Product" };
        _repositoryMock.Setup(r => r.GetByIdAsync(productId))
            .ReturnsAsync(expectedProduct);

        // Act
        var result = await _service.GetProductAsync(productId);

        // Assert
        Assert.NotNull(result);
        Assert.Equal(productId, result.Id);
        _repositoryMock.Verify(r => r.GetByIdAsync(productId), Times.Once);
    }
}
```

## Best Practices

### Code Organization
- Use meaningful namespaces and folder structure
- Separate concerns with single responsibility principle
- Keep methods small and focused (under 20 lines when possible)
- Use async/await consistently for I/O operations

### Naming Conventions
- PascalCase for classes, methods, properties, and namespaces
- camelCase for local variables and method parameters
- Use descriptive names that convey intent
- Prefix interfaces with 'I' (IProductService)

### Error Handling
- Use try/catch blocks for expected exceptions
- Implement global exception handling with middleware
- Return appropriate HTTP status codes from APIs
- Log errors with structured logging (Serilog, NLog)

### Performance
- Use async/await for scalability
- Implement caching where appropriate (IMemoryCache, IDistributedCache)
- Use Entity Framework Core change tracking wisely
- Profile and optimize database queries

### Security
- Validate all inputs and use model validation
- Implement authentication and authorization
- Use HTTPS and secure headers
- Sanitize data to prevent injection attacks

## Troubleshooting

### Common Build Issues
- **CS0246: Type or namespace not found**: Check using statements and package references
- **CS0234: Type or namespace does not exist**: Verify project references and target frameworks
- **CS0012: Type is defined in an assembly not referenced**: Add missing NuGet package references

### Runtime Issues
- **NullReferenceException**: Check for null values before accessing properties/methods
- **InvalidOperationException in EF Core**: Ensure DbContext is properly configured and migrations are applied
- **Deadlock in async code**: Avoid blocking calls in async methods, use ConfigureAwait(false)

### Dependency Injection Problems
- **Unable to resolve service**: Check service registration in Program.cs/Startup.cs
- **Circular dependency**: Refactor to use interfaces or factory patterns
- **Scoped service in singleton**: Ensure proper service lifetimes

### Database Issues
- **Migration errors**: Check migration files and database schema
- **Connection timeout**: Verify connection strings and database availability
- **Concurrency conflicts**: Implement optimistic concurrency with rowversion

### Testing Problems
- **Mock setup not working**: Verify mock configuration and verify calls
- **Async test hanging**: Ensure async operations complete properly
- **Integration test database**: Use test database or in-memory database

## Integration Points

### Development Tools
- **Visual Studio/VS Code**: IDE support with IntelliSense and debugging
- **dotnet CLI**: Command-line tooling for build, test, and publish operations
- **NuGet**: Package management for .NET libraries and tools

### Frameworks & Libraries
- **ASP.NET Core**: Web framework for APIs and MVC applications
- **Entity Framework Core**: ORM for database operations
- **xUnit/NUnit**: Testing frameworks for unit and integration tests
- **Serilog/NLog**: Structured logging libraries

### Cloud Platforms
- **Azure**: App Service, Functions, SQL Database, Blob Storage
- **AWS**: Lambda, API Gateway, RDS, S3
- **Google Cloud**: Cloud Run, Cloud SQL, Cloud Storage

### Databases
- **SQL Server**: Relational database with Entity Framework Core
- **PostgreSQL**: Open-source database with Npgsql provider
- **MongoDB**: NoSQL database with MongoDB driver
- **Redis**: In-memory data structure store for caching

### DevOps & CI/CD
- **GitHub Actions**: Automated build and deployment pipelines
- **Azure DevOps**: Comprehensive DevOps platform
- **Docker**: Containerization for consistent deployments
- **Kubernetes**: Orchestration for microservices deployment