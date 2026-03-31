---
name: angular
description: '**WORKFLOW SKILL** — Create, develop, and optimize Angular applications. USE FOR: building web applications, implementing components, managing state, integrating APIs, debugging performance issues, and deploying to production. DO NOT USE FOR: non-Angular web development, mobile apps, or backend services. INVOKES: file system tools for project creation/modification, terminal for Angular CLI commands, language analysis for TypeScript optimization.'
---

# Angular Development Skill

## Overview

This skill provides comprehensive support for Angular application development, covering everything from project setup and component design to state management, API integration, testing, and deployment. It focuses on creating scalable, maintainable web applications using Angular best practices and modern TypeScript patterns.

## Key Capabilities

### Project Setup & Architecture
- Create new Angular projects with Angular CLI
- Configure TypeScript and project structure
- Set up state management solutions (NgRx, Akita, Services)
- Implement component architecture patterns (Smart/Dumb components)
- Configure routing with Angular Router and lazy loading

### Component Development
- Build reusable Angular components with TypeScript
- Create custom directives and pipes for shared logic
- Implement component lifecycle management and change detection
- Handle input/output properties with proper typing
- Optimize component performance with OnPush change detection

### State Management & Data Flow
- Implement local state with component properties and services
- Manage global state with NgRx or state management libraries
- Handle side effects with RxJS operators and effects
- Integrate with REST APIs and GraphQL endpoints
- Implement reactive data flow with Observables

### Performance & Optimization
- Optimize change detection with OnPush strategy and trackBy functions
- Implement lazy loading for modules and components
- Use Angular DevTools for performance profiling and debugging
- Optimize bundle size with tree shaking and differential loading
- Implement virtualization for large datasets

### Testing & Quality Assurance
- Write unit tests with Jasmine and Angular Testing Utilities
- Create integration tests for component interactions
- Implement end-to-end tests with Protractor or Cypress
- Set up testing utilities and custom test helpers
- Configure test coverage and CI/CD integration

### Deployment & DevOps
- Configure build processes for production deployment
- Set up environment configurations and build optimizations
- Implement Progressive Web App (PWA) features
- Configure server-side rendering with Angular Universal
- Set up deployment pipelines for various hosting platforms

## Usage Examples

### Creating a New Angular Project
```bash
ng new my-angular-app --routing --style=scss
cd my-angular-app
ng serve
```

### Generating Components and Services
```bash
ng generate component user-profile
ng generate service data
ng generate guard auth
```

### Implementing Reactive Forms
```typescript
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-user-form',
  template: `
    <form [formGroup]="userForm" (ngSubmit)="onSubmit()">
      <input formControlName="name" placeholder="Name">
      <input formControlName="email" type="email" placeholder="Email">
      <button type="submit" [disabled]="!userForm.valid">Submit</button>
    </form>
  `
})
export class UserFormComponent {
  userForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.userForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]]
    });
  }

  onSubmit() {
    if (this.userForm.valid) {
      console.log(this.userForm.value);
    }
  }
}
```

### State Management with NgRx
```typescript
// Actions
export const loadUsers = createAction('[User] Load Users');
export const loadUsersSuccess = createAction(
  '[User] Load Users Success',
  props<{ users: User[] }>()
);

// Reducer
const userReducer = createReducer(
  initialState,
  on(loadUsers, state => ({ ...state, loading: true })),
  on(loadUsersSuccess, (state, { users }) => ({
    ...state,
    users,
    loading: false
  }))
);

// Effects
@Injectable()
export class UserEffects {
  loadUsers$ = createEffect(() =>
    this.actions$.pipe(
      ofType(loadUsers),
      mergeMap(() => this.userService.getUsers().pipe(
        map(users => loadUsersSuccess({ users })),
        catchError(() => EMPTY)
      ))
    )
  );
}
```

### HTTP Service with Interceptors
```typescript
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private http: HttpClient) {}

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>('/api/users');
  }

  createUser(user: User): Observable<User> {
    return this.http.post<User>('/api/users', user);
  }
}

// HTTP Interceptor
@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const authReq = req.clone({
      setHeaders: {
        Authorization: `Bearer ${this.authService.getToken()}`
      }
    });
    return next.handle(authReq);
  }
}
```

## Common Patterns

### Smart/Dumb Component Pattern
```typescript
// Smart Component (Container)
@Component({
  selector: 'app-user-list-container',
  template: `
    <app-user-list
      [users]="users$ | async"
      [loading]="loading$ | async"
      (userSelected)="onUserSelected($event)">
    </app-user-list>
  `
})
export class UserListContainerComponent {
  users$ = this.store.select(selectUsers);
  loading$ = this.store.select(selectLoading);

  constructor(private store: Store) {}

  onUserSelected(user: User) {
    this.store.dispatch(selectUser({ user }));
  }
}

// Dumb Component (Presentation)
@Component({
  selector: 'app-user-list',
  template: `
    <div *ngIf="loading">Loading...</div>
    <div *ngFor="let user of users; trackBy: trackByUserId"
         (click)="userSelected.emit(user)">
      {{ user.name }}
    </div>
  `
})
export class UserListComponent {
  @Input() users: User[];
  @Input() loading: boolean;
  @Output() userSelected = new EventEmitter<User>();

  trackByUserId(index: number, user: User): number {
    return user.id;
  }
}
```

### Custom Directive for Input Validation
```typescript
@Directive({
  selector: '[appPasswordStrength]'
})
export class PasswordStrengthDirective implements Validator {
  validate(control: AbstractControl): ValidationErrors | null {
    const value = control.value;
    if (!value) return null;

    const hasUpperCase = /[A-Z]/.test(value);
    const hasLowerCase = /[a-z]/.test(value);
    const hasNumeric = /[0-9]/.test(value);
    const hasSpecial = /[#?!@$%^&*-]/.test(value);

    const passwordValid = hasUpperCase && hasLowerCase && hasNumeric && hasSpecial;
    return !passwordValid ? { invalidPassword: true } : null;
  }
}
```

### Route Guards for Authentication
```typescript
@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<boolean> | Promise<boolean> | boolean {
    return this.authService.isAuthenticated().pipe(
      tap(isAuth => {
        if (!isAuth) {
          this.router.navigate(['/login']);
        }
      })
    );
  }
}
```

### Custom Pipe for Data Transformation
```typescript
@Pipe({
  name: 'filter',
  pure: false
})
export class FilterPipe implements PipeTransform {
  transform(items: any[], searchText: string): any[] {
    if (!items || !searchText) {
      return items;
    }
    return items.filter(item =>
      item.name.toLowerCase().includes(searchText.toLowerCase())
    );
  }
}
```

## Best Practices

### Code Organization
- Follow Angular style guide and naming conventions
- Use feature modules to organize related components
- Implement proper folder structure (core, shared, features)
- Use index.ts files for clean imports
- Separate business logic from presentation logic

### Performance Optimization
- Use OnPush change detection strategy
- Implement lazy loading for feature modules
- Use trackBy functions in *ngFor directives
- Optimize bundle size with tree shaking
- Implement proper caching strategies

### State Management
- Use services for component communication
- Implement proper RxJS patterns for data flow
- Use NgRx for complex state management
- Handle errors gracefully with catchError
- Implement proper loading states

### Testing Strategy
- Write unit tests for all components and services
- Use Angular Testing Utilities for component testing
- Mock HTTP calls and external dependencies
- Implement integration tests for critical flows
- Maintain high test coverage (>80%)

### Security Considerations
- Implement proper input validation and sanitization
- Use Angular's built-in XSS protection
- Implement authentication and authorization guards
- Secure HTTP communications with HTTPS
- Handle sensitive data appropriately

## Troubleshooting

### Build and Compilation Issues
- **Problem**: TypeScript compilation errors
  **Solution**: Check tsconfig.json settings, ensure proper type definitions, use strict mode appropriately

- **Problem**: Module resolution issues
  **Solution**: Verify import paths, check angular.json configuration, ensure proper module declarations

- **Problem**: Bundle size too large
  **Solution**: Implement lazy loading, remove unused dependencies, use tree shaking, analyze with webpack-bundle-analyzer

### Runtime Performance Issues
- **Problem**: Slow initial load times
  **Solution**: Implement lazy loading, use AOT compilation, optimize images and assets, implement service workers

- **Problem**: Excessive change detection cycles
  **Solution**: Use OnPush strategy, implement trackBy functions, avoid complex computations in templates

- **Problem**: Memory leaks
  **Solution**: Properly unsubscribe from observables, use takeUntil pattern, avoid circular references

### Component and Template Issues
- **Problem**: ExpressionChangedAfterItHasBeenCheckedError
  **Solution**: Use ChangeDetectorRef.markForCheck(), implement proper change detection strategy, avoid direct DOM manipulation

- **Problem**: ViewDestroyedError
  **Solution**: Use takeUntil pattern for unsubscribing, check component lifecycle before updating views

- **Problem**: Form validation not working
  **Solution**: Ensure proper form setup, check validator implementations, verify template bindings

### HTTP and API Integration Issues
- **Problem**: CORS errors
  **Solution**: Configure proxy settings for development, implement proper CORS headers on server

- **Problem**: Interceptor not working
  **Solution**: Ensure interceptor is provided in app module, check interceptor implementation, verify HTTP client usage

- **Problem**: Observable not updating UI
  **Solution**: Use async pipe in templates, implement proper change detection, check for OnPush strategy conflicts

### State Management Problems
- **Problem**: State not updating in components
  **Solution**: Check selector implementations, ensure proper action dispatching, verify reducer logic

- **Problem**: Effects not triggering
  **Solution**: Check effect registration, verify action types, ensure proper observable handling

- **Problem**: Store not initialized
  **Solution**: Ensure store is configured in app module, check initial state setup, verify imports

## Integration Points

### Development Tools
- **Angular CLI**: Project scaffolding, code generation, build optimization
- **Angular DevTools**: Performance profiling, component inspection, debugging
- **VS Code Extensions**: Angular Language Service, Angular Snippets, TypeScript support

### State Management Libraries
- **NgRx**: Reactive state management with actions, reducers, effects, and selectors
- **Akita**: Simple state management with entity stores and queries
- **NgXS**: Modern state management with action handlers and state operators

### UI Component Libraries
- **Angular Material**: Material Design components for consistent UI
- **PrimeNG**: Rich component library with data tables, charts, and forms
- **Ionic**: Mobile-first UI components for hybrid applications

### Backend Integration
- **REST APIs**: HttpClient for RESTful service integration
- **GraphQL**: Apollo Angular for GraphQL client implementation
- **WebSockets**: Real-time communication with Socket.io or native WebSockets

### Testing Frameworks
- **Jasmine**: Behavior-driven testing framework
- **Karma**: Test runner for unit tests
- **Protractor/Cypress**: End-to-end testing frameworks

### Build Tools & Deployment
- **Webpack**: Module bundling and optimization
- **Docker**: Containerization for consistent deployment
- **Firebase/Netlify/Vercel**: Hosting platforms with Angular support

### Data Visualization
- **Chart.js**: Simple chart library integration
- **D3.js**: Advanced data visualization and manipulation
- **ngx-charts**: Angular-specific charting library

This skill enables comprehensive Angular application development with modern best practices, performance optimization, and robust testing strategies.