---
name: vue
description: '**WORKFLOW SKILL** — Create, develop, and optimize Vue.js applications. USE FOR: building web applications, implementing Vue components, managing reactive state, integrating APIs, debugging performance issues, and deploying to production. DO NOT USE FOR: non-Vue web development, mobile apps, or backend services. INVOKES: file system tools for project creation/modification, terminal for npm/yarn commands, language analysis for JavaScript/TypeScript optimization.'
---

# Vue.js Development Skill

## Overview

This skill provides comprehensive support for Vue.js application development, covering everything from project setup and component design to reactive state management, API integration, testing, and deployment. It focuses on creating performant, maintainable web applications using Vue.js best practices and modern JavaScript/TypeScript patterns.

## Key Capabilities

### Project Setup & Architecture
- Create new Vue projects with Vue CLI, Vite, or Nuxt.js
- Configure TypeScript and JavaScript project structure
- Set up state management solutions (Pinia, Vuex)
- Implement component architecture patterns (Composition API, Options API)
- Configure routing with Vue Router or Nuxt.js routing

### Component Development
- Build reusable Vue components with Composition API and Options API
- Create custom composables for shared logic and state management
- Implement component composition and slots
- Handle props validation with TypeScript interfaces or prop definitions
- Optimize component rendering with computed properties and watchers

### Reactive State Management & Data Flow
- Implement reactive state with ref, reactive, and computed
- Manage global state with Pinia or Vuex stores
- Handle side effects with watchers and lifecycle hooks
- Integrate with REST APIs and GraphQL endpoints
- Implement data fetching patterns (VueUse, Axios, Apollo)

### Performance & Optimization
- Optimize component re-renders with computed and memoization
- Implement code splitting and lazy loading for better performance
- Use Vue DevTools for performance profiling and debugging
- Optimize bundle size with tree shaking and dynamic imports
- Implement virtualization for large lists and tables

### Testing & Quality Assurance
- Write unit tests with Vitest and Vue Test Utils
- Create integration tests for component interactions
- Implement end-to-end tests with Cypress or Playwright
- Set up testing utilities and custom mount functions
- Configure test coverage and CI/CD integration

### Deployment & DevOps
- Configure build processes for production deployment
- Set up deployment pipelines for Vercel, Netlify, or custom servers
- Implement environment configuration and secrets management
- Configure CDN integration and asset optimization
- Set up monitoring and error tracking

## Usage Examples

### Project Creation
```bash
# Create new Vue project with Vite
npm create vue@latest my-vue-app
cd my-vue-app
npm install
npm run dev

# Create new Nuxt.js project
npx nuxi@latest init my-nuxt-app
cd my-nuxt-app
npm install
npm run dev
```

### Component Development
```vue
<template>
  <div class="user-card">
    <h2>{{ user.name }}</h2>
    <p>{{ user.email }}</p>
    <button @click="updateUser" :disabled="loading">
      {{ loading ? 'Updating...' : 'Update' }}
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

interface User {
  id: number
  name: string
  email: string
}

interface Props {
  user: User
}

const props = defineProps<Props>()
const loading = ref(false)

const displayName = computed(() => props.user.name.toUpperCase())

const emit = defineEmits<{
  update: [user: User]
}>()

const updateUser = async () => {
  loading.value = true
  try {
    // API call logic here
    emit('update', props.user)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.user-card {
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 8px;
}
</style>
```

### State Management with Pinia
```typescript
// stores/user.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  const users = ref<User[]>([])
  const loading = ref(false)

  const activeUsers = computed(() =>
    users.value.filter(user => user.active)
  )

  const fetchUsers = async () => {
    loading.value = true
    try {
      const response = await fetch('/api/users')
      users.value = await response.json()
    } finally {
      loading.value = false
    }
  }

  const addUser = (user: User) => {
    users.value.push(user)
  }

  return {
    users,
    loading,
    activeUsers,
    fetchUsers,
    addUser
  }
})
```

### API Integration
```typescript
// composables/useApi.ts
import { ref } from 'vue'

export function useApi<T>() {
  const data = ref<T | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  const execute = async (url: string, options?: RequestInit) => {
    loading.value = true
    error.value = null

    try {
      const response = await fetch(url, options)
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      data.value = await response.json()
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'An error occurred'
    } finally {
      loading.value = false
    }
  }

  return {
    data: readonly(data),
    loading: readonly(loading),
    error: readonly(error),
    execute
  }
}
```

## Common Patterns

### Composition Function Pattern
```typescript
// composables/useCounter.ts
import { ref, computed } from 'vue'

export function useCounter(initialValue = 0) {
  const count = ref(initialValue)

  const double = computed(() => count.value * 2)

  const increment = () => count.value++
  const decrement = () => count.value--
  const reset = () => count.value = initialValue

  return {
    count,
    double,
    increment,
    decrement,
    reset
  }
}
```

### Component with Slots
```vue
<!-- components/Modal.vue -->
<template>
  <Teleport to="body">
    <div v-if="show" class="modal-overlay" @click="close">
      <div class="modal-content" @click.stop>
        <header>
          <slot name="header">Default Header</slot>
          <button @click="close">&times;</button>
        </header>
        <main>
          <slot>Default content</slot>
        </main>
        <footer>
          <slot name="footer"></slot>
        </footer>
      </div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface Props {
  show: boolean
}

const props = defineProps<Props>()

const emit = defineEmits<{
  close: []
}>()

const close = () => {
  emit('close')
}
</script>
```

### Custom Directive
```typescript
// directives/v-focus.ts
import type { Directive } from 'vue'

export const vFocus: Directive = {
  mounted(el) {
    el.focus()
  }
}

// Usage in component
// <input v-focus />
```

## Best Practices

### Code Organization
- Use Composition API for complex components and Options API for simple ones
- Organize components in feature-based folder structure
- Create reusable composables for shared logic
- Use TypeScript for better type safety and developer experience
- Follow Vue.js style guide conventions

### Performance Optimization
- Use shallowRef for large objects that don't need deep reactivity
- Implement proper key attributes in v-for loops
- Use computed properties instead of methods for derived data
- Lazy load components and routes when possible
- Optimize images and assets for web delivery

### State Management
- Use Pinia for global state management (preferred over Vuex)
- Keep component state local when possible
- Use reactive() for objects and ref() for primitives
- Implement proper error handling in async operations
- Use watchers sparingly and prefer computed properties

### Testing Strategy
- Test components with Vue Test Utils and Vitest
- Mock external dependencies and API calls
- Test user interactions and component behavior
- Use testing-library principles for accessible testing
- Maintain high test coverage for critical business logic

### Security Considerations
- Validate and sanitize user inputs
- Use HTTPS for all API communications
- Implement proper authentication and authorization
- Avoid direct DOM manipulation when possible
- Keep dependencies updated and audit for vulnerabilities

## Troubleshooting

### Build Issues
- **Module not found errors**: Check import paths and ensure all dependencies are installed
- **TypeScript compilation errors**: Verify type definitions and interface declarations
- **Build performance issues**: Implement code splitting and optimize bundle size

### Runtime Problems
- **Reactivity not working**: Ensure using ref() or reactive() for reactive data
- **Component not updating**: Check if props are properly defined and passed
- **Memory leaks**: Properly clean up watchers and event listeners in onUnmounted

### Performance Issues
- **Slow initial load**: Implement code splitting and lazy loading
- **Excessive re-renders**: Use computed properties and proper key attributes
- **Large bundle size**: Analyze bundle with webpack-bundle-analyzer and remove unused code

### API Integration Issues
- **CORS errors**: Configure proper CORS headers on backend or use proxy in development
- **Authentication failures**: Verify token handling and refresh logic
- **Data synchronization**: Implement proper loading states and error handling

### State Management Problems
- **State not persisting**: Check Pinia store configuration and persistence plugins
- **Actions not triggering**: Verify action definitions and proper store usage
- **Race conditions**: Implement proper async handling and loading states

## Integration Points

### Development Tools
- **Vue DevTools**: Browser extension for debugging Vue applications
- **Vite**: Fast build tool and development server
- **Vue CLI**: Command-line interface for Vue project management
- **TypeScript**: Type-safe JavaScript development
- **ESLint + Prettier**: Code linting and formatting

### State Management Libraries
- **Pinia**: Intuitive state management for Vue 3
- **Vuex**: Official state management library (legacy)
- **Zustand**: Small state management library with Vue adapter

### UI Component Libraries
- **Vuetify**: Material Design component library
- **Quasar**: High-performance component library
- **Element Plus**: Vue 3 component library
- **PrimeVue**: Rich component suite

### Backend Integration
- **Axios**: HTTP client for API requests
- **Apollo Client**: GraphQL client for Vue
- **VueUse**: Collection of Vue composition utilities
- **Socket.io**: Real-time communication

### Testing Frameworks
- **Vitest**: Fast unit testing framework
- **Vue Test Utils**: Official testing utilities
- **Cypress**: End-to-end testing framework
- **Playwright**: Cross-browser testing

### Build Tools & Deployment
- **Vite**: Modern build tool with fast HMR
- **Vue CLI**: Project scaffolding and build tools
- **Webpack**: Advanced bundling and optimization
- **Vercel/Netlify**: Serverless deployment platforms

### Data Visualization
- **Chart.js + vue-chartjs**: Chart and graph components
- **D3.js + vue-d3**: Advanced data visualization
- **Highcharts Vue**: Commercial charting library