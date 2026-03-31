---
name: flutter
description: '**WORKFLOW SKILL** — Create, develop, and optimize Flutter applications. USE FOR: building cross-platform mobile apps, implementing UI components, managing state, integrating APIs, debugging performance issues, and deploying to app stores. DO NOT USE FOR: non-Flutter mobile development, backend services, or web-only applications. INVOKES: file system tools for project creation/modification, terminal for Flutter commands, language analysis for Dart code optimization.'
---

# Flutter Development Skill

## Overview

This skill provides comprehensive support for Flutter application development, covering everything from project setup and UI design to state management, API integration, testing, and deployment. It focuses on creating performant, maintainable cross-platform mobile applications using Dart and Flutter best practices.

## Key Capabilities

### Project Setup & Architecture
- Create new Flutter projects with proper folder structure
- Configure app icons, splash screens, and launch configurations
- Set up state management solutions (Provider, Riverpod, Bloc)
- Implement clean architecture patterns (presentation, domain, data layers)
- Configure routing and navigation patterns

### UI/UX Development
- Build responsive layouts with Material Design and Cupertino widgets
- Create custom widgets and reusable component libraries
- Implement animations and transitions
- Handle different screen sizes and orientations
- Apply theming and styling systems

### State Management & Data Flow
- Implement reactive state management patterns
- Handle local data persistence (SQLite, Hive, SharedPreferences)
- Integrate with REST APIs and GraphQL endpoints
- Manage authentication and user sessions
- Implement offline-first capabilities

### Performance & Optimization
- Optimize widget rebuilds and tree structures
- Implement lazy loading and pagination
- Profile and fix memory leaks
- Optimize app startup time and bundle size
- Handle platform-specific optimizations

### Testing & Quality Assurance
- Write unit tests for business logic and utilities
- Create widget tests for UI components
- Implement integration tests for user flows
- Set up CI/CD pipelines for automated testing
- Use Flutter's testing framework and tools

### Platform Integration & Deployment
- Configure platform-specific features (camera, location, notifications)
- Handle app store deployment (Google Play, App Store)
- Implement deep linking and app-to-app communication
- Configure push notifications and background tasks
- Manage app versioning and release processes

## Usage Examples

### Create a new Flutter app
```
Create a Flutter app for a task management system with the following features:
- Task list with add/edit/delete functionality
- Categories and priority levels
- Local storage with SQLite
- Clean Material Design UI
```

### Implement state management
```
Add Provider-based state management to handle user authentication and task data across the app.
```

### API integration
```
Integrate with a REST API for syncing tasks between devices, including offline support and conflict resolution.
```

## Common Patterns

### Widget Structure
```dart
class TaskCard extends StatelessWidget {
  final Task task;
  final VoidCallback onTap;
  final VoidCallback onDelete;

  const TaskCard({
    super.key,
    required this.task,
    required this.onTap,
    required this.onDelete,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        title: Text(task.title),
        subtitle: Text(task.description),
        trailing: IconButton(
          icon: Icon(Icons.delete),
          onPressed: onDelete,
        ),
        onTap: onTap,
      ),
    );
  }
}
```

### State Management with Provider
```dart
class TaskProvider extends ChangeNotifier {
  List<Task> _tasks = [];

  List<Task> get tasks => _tasks;

  void addTask(Task task) {
    _tasks.add(task);
    notifyListeners();
  }

  void removeTask(String id) {
    _tasks.removeWhere((task) => task.id == id);
    notifyListeners();
  }
}
```

### API Service
```dart
class ApiService {
  final Dio _dio = Dio(BaseOptions(
    baseUrl: 'https://api.example.com',
    connectTimeout: Duration(seconds: 5),
    receiveTimeout: Duration(seconds: 3),
  ));

  Future<List<Task>> getTasks() async {
    try {
      final response = await _dio.get('/tasks');
      return (response.data as List)
          .map((json) => Task.fromJson(json))
          .toList();
    } catch (e) {
      throw Exception('Failed to load tasks: $e');
    }
  }
}
```

## Best Practices

### Code Organization
- Use feature-first folder structure over type-first
- Keep widgets small and focused on single responsibilities
- Extract business logic into separate service classes
- Use dependency injection for testability

### Performance
- Use const constructors for static widgets
- Implement proper key usage for list items
- Avoid unnecessary rebuilds with Consumer and Selector
- Profile with Flutter DevTools regularly

### State Management
- Choose state management based on app complexity
- Keep state close to where it's used
- Use immutable data models
- Handle loading and error states properly

### Testing
- Write tests for all business logic
- Test widget behavior, not implementation details
- Use mock services for external dependencies
- Maintain high test coverage (>80%)

### Platform Considerations
- Test on both iOS and Android regularly
- Handle platform differences gracefully
- Use platform channels for native functionality
- Follow platform-specific design guidelines

## Troubleshooting

### Build Issues
- **Gradle build failures**: Clean and rebuild project, check Android SDK versions
- **iOS build errors**: Ensure Xcode and CocoaPods are up to date
- **Plugin conflicts**: Check plugin versions and compatibility

### Runtime Issues
- **Widget not updating**: Check if state changes trigger notifyListeners()
- **Memory leaks**: Use Flutter DevTools to identify retaining objects
- **Performance drops**: Profile with DevTools, check for expensive operations in build methods

### Platform-Specific Problems
- **Android permissions**: Ensure proper manifest declarations
- **iOS entitlements**: Configure capabilities in Xcode
- **Plugin not working**: Verify platform-specific setup in native code

### Common Flutter Pitfalls
- **SetState called after dispose**: Check mounted property before calling setState
- **Provider not found**: Ensure proper provider scope and context
- **Hot reload not working**: Check for syntax errors preventing compilation

### Debugging Techniques
- Use Flutter DevTools for performance profiling
- Enable logging for API calls and state changes
- Use breakpoints in VS Code/Android Studio
- Check device logs for native platform issues

## Integration Points

### Development Tools
- **VS Code/Android Studio**: Primary IDEs with Flutter extensions
- **Flutter DevTools**: Performance profiling and debugging
- **Dart DevTools**: Memory and CPU analysis

### State Management Libraries
- **Provider/Riverpod**: Reactive state management
- **Bloc**: Event-driven architecture
- **MobX**: Observable-based state management

### Backend Integration
- **Firebase**: Authentication, database, and analytics
- **Supabase**: Open-source Firebase alternative
- **Custom APIs**: REST, GraphQL, and WebSocket connections

### Data Storage
- **SQLite**: Local database with sqflite
- **Hive**: Lightweight NoSQL database
- **SharedPreferences**: Simple key-value storage

### Testing Frameworks
- **flutter_test**: Built-in testing framework
- **integration_test**: End-to-end testing
- **mockito**: Mocking framework for Dart

### CI/CD Platforms
- **GitHub Actions**: Automated testing and deployment
- **Codemagic**: Mobile-specific CI/CD
- **Bitrise**: Cross-platform mobile pipelines

### App Distribution
- **Google Play**: Android app distribution
- **App Store**: iOS app distribution
- **Firebase App Distribution**: Beta testing and distribution