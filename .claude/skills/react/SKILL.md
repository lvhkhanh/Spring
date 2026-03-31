---
name: react
description: '**WORKFLOW SKILL** — Create, develop, and optimize React applications. USE FOR: building web applications, implementing UI components, managing state, integrating APIs, debugging performance issues, and deploying to production. DO NOT USE FOR: non-React web development, mobile apps, or backend services. INVOKES: file system tools for project creation/modification, terminal for npm/yarn commands, language analysis for JavaScript/TypeScript optimization.'
---

# React Development Skill

## Overview

This skill provides comprehensive support for React application development, covering everything from project setup and component design to state management, API integration, testing, and deployment. It focuses on creating performant, maintainable web applications using React best practices and modern JavaScript/TypeScript patterns.

## Key Capabilities

### Project Setup & Architecture
- Create new React projects with Create React App, Vite, or Next.js
- Configure TypeScript and JavaScript project structure
- Set up state management solutions (Redux, Zustand, Context API)
- Implement component architecture patterns (Atomic Design, Container/Presentational)
- Configure routing with React Router or Next.js routing

### Component Development
- Build reusable React components with hooks and functional patterns
- Create custom hooks for shared logic and state management
- Implement component composition and higher-order components
- Handle props validation with PropTypes or TypeScript interfaces
- Optimize component rendering with memoization and lazy loading

### State Management & Data Flow
- Implement local state with useState and useReducer hooks
- Manage global state with Context API or state management libraries
- Handle side effects with useEffect and custom hooks
- Integrate with REST APIs and GraphQL endpoints
- Implement data fetching patterns (React Query, SWR, Apollo)

### Performance & Optimization
- Optimize component re-renders with React.memo and useMemo
- Implement code splitting and lazy loading for better performance
- Use React DevTools for performance profiling and debugging
- Optimize bundle size with tree shaking and dynamic imports
- Implement virtualization for large lists and tables

### Testing & Quality Assurance
- Write unit tests with Jest and React Testing Library
- Create integration tests for component interactions
- Implement end-to-end tests with Cypress or Playwright
- Set up testing utilities and custom render functions
- Configure test coverage and CI/CD integration

### Deployment & DevOps
- Configure build processes for production deployment
- Set up CI/CD pipelines for automated testing and deployment
- Implement environment configuration and secrets management
- Optimize for different deployment platforms (Vercel, Netlify, AWS)
- Handle service worker implementation for PWA features

## Usage Examples

### Creating a New React Project
```bash
# With Create React App
npx create-react-app my-app --template typescript

# With Vite
npm create vite@latest my-app -- --template react-ts

# With Next.js
npx create-next-app@latest my-app --typescript
```

### Component with Hooks
```typescript
import React, { useState, useEffect } from 'react';

interface User {
  id: number;
  name: string;
  email: string;
}

const UserList: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await fetch('/api/users');
        if (!response.ok) throw new Error('Failed to fetch users');
        const data = await response.json();
        setUsers(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An error occurred');
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h2>Users</h2>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;
```

### State Management with Context
```typescript
import React, { createContext, useContext, useReducer, ReactNode } from 'react';

interface AppState {
  user: User | null;
  theme: 'light' | 'dark';
}

type AppAction =
  | { type: 'SET_USER'; payload: User }
  | { type: 'LOGOUT' }
  | { type: 'SET_THEME'; payload: 'light' | 'dark' };

const initialState: AppState = {
  user: null,
  theme: 'light',
};

const appReducer = (state: AppState, action: AppAction): AppState => {
  switch (action.type) {
    case 'SET_USER':
      return { ...state, user: action.payload };
    case 'LOGOUT':
      return { ...state, user: null };
    case 'SET_THEME':
      return { ...state, theme: action.payload };
    default:
      return state;
  }
};

const AppContext = createContext<{
  state: AppState;
  dispatch: React.Dispatch<AppAction>;
} | null>(null);

export const AppProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(appReducer, initialState);

  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
};

export const useApp = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp must be used within an AppProvider');
  }
  return context;
};
```

### Custom Hook for API Calls
```typescript
import { useState, useEffect } from 'react';

interface UseApiState<T> {
  data: T | null;
  loading: boolean;
  error: string | null;
}

export function useApi<T>(url: string, options?: RequestInit) {
  const [state, setState] = useState<UseApiState<T>>({
    data: null,
    loading: true,
    error: null,
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        setState(prev => ({ ...prev, loading: true, error: null }));
        const response = await fetch(url, options);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setState({ data, loading: false, error: null });
      } catch (error) {
        setState({
          data: null,
          loading: false,
          error: error instanceof Error ? error.message : 'An error occurred',
        });
      }
    };

    fetchData();
  }, [url, JSON.stringify(options)]);

  return state;
}

// Usage
const { data: posts, loading, error } = useApi<Post[]>('/api/posts');
```

## Common Patterns

### Component Composition
```typescript
// Base component
const Button: React.FC<{
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
  onClick?: () => void;
}> = ({ variant = 'primary', size = 'md', children, onClick }) => {
  const baseClasses = 'rounded font-medium transition-colors';
  const variantClasses = {
    primary: 'bg-blue-500 text-white hover:bg-blue-600',
    secondary: 'bg-gray-200 text-gray-800 hover:bg-gray-300',
  };
  const sizeClasses = {
    sm: 'px-3 py-1 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg',
  };

  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
};

// Composed component
const IconButton: React.FC<{
  icon: React.ReactNode;
  label: string;
  onClick?: () => void;
}> = ({ icon, label, onClick }) => (
  <Button onClick={onClick}>
    <span className="flex items-center gap-2">
      {icon}
      {label}
    </span>
  </Button>
);

// Usage
<IconButton
  icon={<PlusIcon />}
  label="Add Item"
  onClick={handleAdd}
/>
```

### Error Boundary
```typescript
import React from 'react';

interface ErrorBoundaryState {
  hasError: boolean;
  error?: Error;
}

class ErrorBoundary extends React.Component<
  React.PropsWithChildren<{ fallback?: React.ComponentType<{ error?: Error }> }>,
  ErrorBoundaryState
> {
  constructor(props: React.PropsWithChildren<{ fallback?: React.ComponentType<{ error?: Error }> }>) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      const FallbackComponent = this.props.fallback || DefaultErrorFallback;
      return <FallbackComponent error={this.state.error} />;
    }

    return this.props.children;
  }
}

const DefaultErrorFallback: React.FC<{ error?: Error }> = ({ error }) => (
  <div className="error-boundary">
    <h2>Something went wrong</h2>
    <p>{error?.message || 'An unexpected error occurred'}</p>
    <button onClick={() => window.location.reload()}>Reload Page</button>
  </div>
);

// Usage
<ErrorBoundary>
  <App />
</ErrorBoundary>
```

### Form Handling with Validation
```typescript
import React, { useState } from 'react';

interface FormData {
  email: string;
  password: string;
  confirmPassword: string;
}

interface FormErrors {
  email?: string;
  password?: string;
  confirmPassword?: string;
}

const validateForm = (data: FormData): FormErrors => {
  const errors: FormErrors = {};

  if (!data.email) {
    errors.email = 'Email is required';
  } else if (!/\S+@\S+\.\S+/.test(data.email)) {
    errors.email = 'Email is invalid';
  }

  if (!data.password) {
    errors.password = 'Password is required';
  } else if (data.password.length < 8) {
    errors.password = 'Password must be at least 8 characters';
  }

  if (data.password !== data.confirmPassword) {
    errors.confirmPassword = 'Passwords do not match';
  }

  return errors;
};

const RegistrationForm: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    email: '',
    password: '',
    confirmPassword: '',
  });
  const [errors, setErrors] = useState<FormErrors>({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    // Clear error when user starts typing
    if (errors[name as keyof FormErrors]) {
      setErrors(prev => ({ ...prev, [name]: undefined }));
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const validationErrors = validateForm(formData);

    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }

    setIsSubmitting(true);
    try {
      // Submit form data
      await submitRegistration(formData);
      // Handle success
    } catch (error) {
      // Handle error
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="email" className="block text-sm font-medium">
          Email
        </label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          className={`mt-1 block w-full rounded border ${
            errors.email ? 'border-red-500' : 'border-gray-300'
          }`}
        />
        {errors.email && (
          <p className="mt-1 text-sm text-red-600">{errors.email}</p>
        )}
      </div>

      <div>
        <label htmlFor="password" className="block text-sm font-medium">
          Password
        </label>
        <input
          type="password"
          id="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          className={`mt-1 block w-full rounded border ${
            errors.password ? 'border-red-500' : 'border-gray-300'
          }`}
        />
        {errors.password && (
          <p className="mt-1 text-sm text-red-600">{errors.password}</p>
        )}
      </div>

      <div>
        <label htmlFor="confirmPassword" className="block text-sm font-medium">
          Confirm Password
        </label>
        <input
          type="password"
          id="confirmPassword"
          name="confirmPassword"
          value={formData.confirmPassword}
          onChange={handleChange}
          className={`mt-1 block w-full rounded border ${
            errors.confirmPassword ? 'border-red-500' : 'border-gray-300'
          }`}
        />
        {errors.confirmPassword && (
          <p className="mt-1 text-sm text-red-600">{errors.confirmPassword}</p>
        )}
      </div>

      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full rounded bg-blue-500 py-2 px-4 text-white hover:bg-blue-600 disabled:opacity-50"
      >
        {isSubmitting ? 'Registering...' : 'Register'}
      </button>
    </form>
  );
};

export default RegistrationForm;
```

## Best Practices

### Code Organization
- Use a consistent file and folder structure (components, hooks, utils, types)
- Implement barrel exports (index.ts files) for clean imports
- Separate business logic from presentation components
- Use TypeScript for better type safety and developer experience
- Follow naming conventions (PascalCase for components, camelCase for functions)

### Performance Optimization
- Use React.memo for expensive components that re-render frequently
- Implement useMemo and useCallback for expensive computations and functions
- Avoid unnecessary re-renders by optimizing state updates
- Use React.lazy and Suspense for code splitting
- Implement virtualization for large lists with react-window

### State Management
- Start with local state and Context API for simple applications
- Use state management libraries (Redux, Zustand) for complex applications
- Keep state as close to where it's used as possible
- Use custom hooks to encapsulate stateful logic
- Implement proper error handling in state updates

### Testing Strategy
- Write tests for all user-facing features and critical business logic
- Use React Testing Library for component testing over enzyme
- Mock external dependencies and API calls in tests
- Test user interactions and component behavior, not implementation details
- Maintain high test coverage for confidence in deployments

### Accessibility & UX
- Use semantic HTML elements and ARIA attributes
- Ensure keyboard navigation and screen reader support
- Provide proper focus management and visual feedback
- Test with different screen sizes and input methods
- Follow WCAG guidelines for inclusive design

## Troubleshooting

### Common Build Issues
- **Module not found errors**: Check import paths and ensure all dependencies are installed
- **TypeScript compilation errors**: Verify type definitions and interface compatibility
- **Build performance issues**: Implement code splitting and optimize bundle size
- **Environment variable problems**: Ensure proper prefixing (.env files) and restart dev server

### Runtime Performance Problems
- **Excessive re-renders**: Use React DevTools Profiler to identify problematic components
- **Memory leaks**: Clean up event listeners and subscriptions in useEffect cleanup
- **Slow initial load**: Implement lazy loading and optimize bundle splitting
- **UI freezing**: Move heavy computations to web workers or optimize algorithms

### State Management Issues
- **Stale closures**: Use functional updates with setState or useReducer
- **Infinite loops**: Ensure useEffect dependencies are correct and stable
- **Race conditions**: Use proper cleanup in useEffect and handle async operations carefully
- **State not updating**: Check for immutable updates and proper key props in lists

### API Integration Problems
- **CORS errors**: Configure server-side CORS headers or use proxy in development
- **Authentication issues**: Implement proper token storage and refresh logic
- **Loading states**: Handle loading, error, and success states consistently
- **Data synchronization**: Implement proper cache invalidation and optimistic updates

### Deployment Challenges
- **Environment configuration**: Use environment variables and build-time configuration
- **Routing issues**: Configure proper server-side routing for SPAs
- **Asset loading problems**: Ensure correct public path and CDN configuration
- **Service worker conflicts**: Handle caching and update strategies properly

## Integration Points

### Development Tools
- **VS Code**: React extensions, TypeScript support, debugging tools
- **Chrome DevTools**: React Developer Tools, Performance tab, Network monitoring
- **ESLint/Prettier**: Code linting and formatting for consistent style
- **Storybook**: Component development and documentation platform

### State Management Libraries
- **Redux Toolkit**: Simplified Redux with modern patterns
- **Zustand**: Lightweight state management with hooks
- **Recoil**: Facebook's experimental state management library
- **Jotai**: Primitive and flexible state management

### UI Component Libraries
- **Material-UI (MUI)**: Google's Material Design components
- **Ant Design**: Enterprise UI design language and React components
- **Chakra UI**: Simple, modular, and accessible component library
- **Tailwind CSS**: Utility-first CSS framework with React integration

### Backend Integration
- **REST APIs**: Axios, React Query for data fetching
- **GraphQL**: Apollo Client, Relay for GraphQL integration
- **Real-time**: Socket.io, Server-Sent Events for live updates
- **Authentication**: Auth0, Firebase Auth, custom JWT implementation

### Testing Frameworks
- **Jest**: JavaScript testing framework with React Testing Library
- **Cypress**: End-to-end testing for web applications
- **Playwright**: Modern web testing and automation framework
- **Testing Library**: Simple and complete testing utilities

### Build Tools & Deployment
- **Vite**: Fast build tool for modern web projects
- **Webpack**: Highly configurable module bundler
- **Parcel**: Zero-configuration application bundler
- **Vercel/Netlify**: Serverless deployment platforms optimized for React

### Data Visualization
- **D3.js**: Powerful data visualization library
- **Chart.js**: Simple yet flexible JavaScript charting library
- **Recharts**: Composed charting library built on React components
- **Victory**: Modular charting library for React