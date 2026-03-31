---
name: mybatis
description: '**WORKFLOW SKILL** — Create, configure, and optimize MyBatis applications for Java persistence. USE FOR: SQL mapping, dynamic queries, result mapping, caching, and database integration. DO NOT USE FOR: non-Java persistence or general ORM tasks. INVOKES: file system tools for XML mapping/modification, terminal for Maven/Gradle commands, MyBatis configuration analysis.'
---

# MyBatis Development Skill

## Overview

This skill supports MyBatis development for Java applications: from configuration setup to complex SQL mapping, dynamic queries, result mapping, caching strategies, and database integration. It focuses on MyBatis Core, MyBatis Spring integration, and best practices for enterprise applications.

## Key Capabilities

### Configuration & Setup
- Configure MyBatis with XML and Java-based configuration
- Set up SqlSessionFactory and SqlSession management
- Integrate MyBatis with Spring Framework
- Configure database connections and connection pooling
- Set up multiple data sources and environments

### SQL Mapping & Statements
- Create XML mapper files with select, insert, update, delete statements
- Implement dynamic SQL with if, choose, when, otherwise, foreach
- Use result maps for complex object relationships
- Configure parameter mapping and result mapping
- Handle one-to-one, one-to-many, and many-to-many relationships

### Annotations & Interface Mapping
- Use @Select, @Insert, @Update, @Delete annotations
- Implement @Results and @Result for result mapping
- Configure @One and @Many for nested mappings
- Use @Param for parameter naming
- Create mapper interfaces with method signatures

### Dynamic SQL & Advanced Features
- Build dynamic queries with OGNL expressions
- Implement pagination with RowBounds and PageHelper
- Use stored procedures and functions
- Configure type handlers for custom data types
- Implement custom SQL providers

### Caching & Performance
- Configure first-level and second-level caching
- Implement custom cache implementations
- Set up cache eviction strategies
- Optimize query performance with lazy loading
- Monitor and tune cache hit ratios

### Transaction Management
- Configure transaction managers for different databases
- Implement programmatic and declarative transactions
- Handle transaction propagation and isolation levels
- Manage transaction rollbacks and commit strategies
- Integrate with Spring transaction management

## Usage Examples

### Set up MyBatis with Spring Boot

```
Create a Spring Boot application with MyBatis integration:
- Configure MyBatis properties in application.yml
- Set up @MapperScan for automatic mapper detection
- Create User entity and UserMapper interface
- Implement CRUD operations with XML mappings
- Add transaction management
```

### Implement complex SQL queries

```
Build a user management system with:
- Dynamic search queries with multiple filters
- Pagination for large result sets
- Complex joins with result mapping
- Batch insert/update operations
- Stored procedure calls for complex business logic
```

### Configure caching strategy

```
Implement multi-level caching for a product catalog:
- First-level session cache for user-specific data
- Second-level application cache for shared data
- Custom cache implementation with Redis
- Cache eviction on data updates
- Performance monitoring and tuning
```

### Handle complex relationships

```
Create an e-commerce system with:
- Product-to-category many-to-many relationships
- Order-to-orderItems one-to-many mappings
- User-to-orders lazy loading
- Nested result mapping for complex objects
- Custom type handlers for special data types
```

## Common Patterns

### MyBatis Configuration

```java
@Configuration
@MapperScan("com.example.mapper")
public class MyBatisConfig {

    @Bean
    public SqlSessionFactory sqlSessionFactory(DataSource dataSource) throws Exception {
        SqlSessionFactoryBean factoryBean = new SqlSessionFactoryBean();
        factoryBean.setDataSource(dataSource);

        // Configure MyBatis settings
        org.apache.ibatis.session.Configuration configuration = new org.apache.ibatis.session.Configuration();
        configuration.setMapUnderscoreToCamelCase(true);
        configuration.setCacheEnabled(true);
        factoryBean.setConfiguration(configuration);

        return factoryBean.getObject();
    }
}
```

### XML Mapper with Dynamic SQL

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="com.example.mapper.UserMapper">

    <resultMap id="userResultMap" type="com.example.model.User">
        <id column="id" property="id"/>
        <result column="username" property="username"/>
        <result column="email" property="email"/>
        <result column="created_at" property="createdAt"/>
    </resultMap>

    <select id="findUsers" resultMap="userResultMap">
        SELECT id, username, email, created_at
        FROM users
        <where>
            <if test="username != null">
                AND username LIKE CONCAT('%', #{username}, '%')
            </if>
            <if test="email != null">
                AND email = #{email}
            </if>
            <if test="startDate != null">
                AND created_at >= #{startDate}
            </if>
        </where>
        ORDER BY created_at DESC
    </select>

    <insert id="insertUser" useGeneratedKeys="true" keyProperty="id">
        INSERT INTO users (username, email, created_at)
        VALUES (#{username}, #{email}, #{createdAt})
    </insert>

</mapper>
```

### Mapper Interface

```java
@Mapper
public interface UserMapper {

    @Select("SELECT id, username, email, created_at FROM users WHERE id = #{id}")
    @Results({
        @Result(property = "createdAt", column = "created_at")
    })
    User findById(@Param("id") Long id);

    @Select("<script>" +
            "SELECT * FROM users" +
            "<where>" +
            "<if test='username != null'>AND username LIKE CONCAT('%', #{username}, '%')</if>" +
            "<if test='email != null'>AND email = #{email}</if>" +
            "</where>" +
            "</script>")
    List<User> findUsers(UserSearchCriteria criteria);

    @Insert("INSERT INTO users (username, email, created_at) VALUES (#{username}, #{email}, #{createdAt})")
    @Options(useGeneratedKeys = true, keyProperty = "id")
    int insert(User user);

    @Update("UPDATE users SET username = #{username}, email = #{email} WHERE id = #{id}")
    int update(User user);

    @Delete("DELETE FROM users WHERE id = #{id}")
    int delete(@Param("id") Long id);
}
```

### Custom Type Handler

```java
@MappedTypes(JsonNode.class)
public class JsonNodeTypeHandler extends BaseTypeHandler<JsonNode> {

    @Override
    public void setNonNullParameter(PreparedStatement ps, int i, JsonNode parameter, JdbcType jdbcType) throws SQLException {
        ps.setString(i, parameter.toString());
    }

    @Override
    public JsonNode getNullableResult(ResultSet rs, String columnName) throws SQLException {
        String json = rs.getString(columnName);
        if (json != null) {
            try {
                return new ObjectMapper().readTree(json);
            } catch (IOException e) {
                throw new SQLException("Failed to parse JSON", e);
            }
        }
        return null;
    }

    @Override
    public JsonNode getNullableResult(ResultSet rs, int columnIndex) throws SQLException {
        return getNullableResult(rs, rs.getMetaData().getColumnName(columnIndex));
    }

    @Override
    public JsonNode getNullableResult(CallableStatement cs, int columnIndex) throws SQLException {
        return getNullableResult(cs, cs.getMetaData().getColumnName(columnIndex));
    }
}
```

## Best Practices

- Use XML mappers for complex SQL and annotations for simple queries
- Enable camel case mapping for Java property naming conventions
- Implement proper result mapping to avoid N+1 query problems
- Use dynamic SQL judiciously to avoid SQL injection
- Configure appropriate cache levels based on data volatility
- Use transactions for data consistency and integrity
- Implement proper error handling and logging
- Use connection pooling for better performance
- Keep SQL logic separate from Java business logic
- Test mappers thoroughly with various data scenarios

## Troubleshooting

### Configuration Issues

- **SqlSessionFactory creation fails**: Check database connection properties and driver dependencies
- **Mapper not found**: Verify @MapperScan packages and XML mapper locations
- **Type handler not working**: Ensure proper registration in MyBatis configuration

### SQL Mapping Problems

- **Result mapping errors**: Check column names match property names or use result maps
- **Parameter not found**: Use @Param annotations for method parameters
- **Dynamic SQL not working**: Verify OGNL expressions and test conditions

### Performance Issues

- **Slow queries**: Enable SQL logging, check execution plans, and optimize indexes
- **Memory leaks**: Monitor SqlSession lifecycle and close sessions properly
- **Cache not working**: Verify cache configuration and eviction policies
- **Connection pool exhaustion**: Adjust pool size and timeout settings

### Transaction Problems

- **Transaction not committed**: Check transaction boundaries and rollback conditions
- **Deadlock issues**: Analyze lock ordering and reduce transaction scope
- **Isolation level problems**: Choose appropriate isolation levels for consistency

## Integration Points

- Spring Framework: MyBatis-Spring integration
- Databases: MySQL, PostgreSQL, Oracle, SQL Server
- Connection pools: HikariCP, Apache DBCP, C3P0
- Caching: EhCache, Redis, Hazelcast
- Testing: JUnit, Mockito, Spring Test
- Build tools: Maven, Gradle
- IDE support: MyBatis plugin for IntelliJ IDEA
- Monitoring: MyBatis logging, SQL performance monitoring