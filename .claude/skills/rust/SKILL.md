---
name: rust
description: '**WORKFLOW SKILL** — Create, refactor, debug, and optimize Rust applications, libraries, and tooling. USE FOR: writing structs, enums, traits, modules, async services, CLIs, tests, Cargo configuration, dependency management, and fixing ownership or lifetime issues. DO NOT USE FOR: non-Rust languages, runtime-only infrastructure tasks, or language-agnostic architecture advice without implementation. INVOKES: file system tools for code generation/modification, terminal for Cargo commands, and language analysis for borrow-checker diagnostics, refactoring, and performance guidance.'
---

# Rust Development Skill

## Overview

This skill supports Rust development across application code, libraries, services, command-line tools, and test suites. It focuses on idiomatic ownership-aware design, maintainable module structure, reliable Cargo workflows, and practical debugging of compiler and runtime issues.

## Key Capabilities

### Code Generation
- Create Rust crates, modules, structs, enums, traits, and impl blocks from requirements
- Write synchronous and asynchronous functions with clear error handling
- Build CLIs, services, libraries, and data-processing utilities
- Implement common ecosystem patterns with `serde`, `tokio`, `clap`, `reqwest`, `sqlx`, `axum`, and `actix-web`

### Project Setup & Cargo
- Scaffold `cargo` projects for binaries, libraries, and workspaces
- Configure `Cargo.toml`, features, profiles, and dependency versions
- Organize code into modules, crates, and workspace members
- Add examples, benches, and integration test layout when appropriate

### Ownership, Borrowing & Types
- Fix borrow checker, move, mutability, and lifetime issues
- Choose between ownership, borrowing, cloning, and smart pointers intentionally
- Model domain logic with enums, pattern matching, and strong types
- Use `Option`, `Result`, iterators, and traits idiomatically

### Testing & Quality
- Add unit, integration, and async tests
- Write focused regression tests for compiler or runtime bugs
- Apply `cargo test`, `cargo fmt`, `cargo clippy`, and targeted lint cleanup
- Improve code readability without fighting Rust’s safety model

### Performance & Reliability
- Reduce unnecessary allocations and clones
- Optimize iterator usage, error paths, and async boundaries
- Reason about `Send`, `Sync`, concurrency, and shared state
- Apply profiling and release-build best practices when performance matters

## Usage Examples

### Create a CLI tool
```text
Create a Rust CLI that reads a CSV file, filters rows by status, and writes JSON output.
Use `clap` for arguments and `serde` for serialization.
```

### Build an API handler
```text
Add a new Axum endpoint that returns active users only.
Follow the existing router/service/repository pattern and add async tests.
```

### Fix ownership issues
```text
This Rust function fails with borrow-checker errors after iterating over a vector and mutating shared state.
Refactor it to be idiomatic and avoid unnecessary cloning.
```

### Add tests
```text
Write unit tests for a parser that converts log lines into typed events, including malformed input cases.
```

## Common Patterns

### Result-based error handling
```rust
fn parse_port(value: &str) -> Result<u16, String> {
    value
        .parse::<u16>()
        .map_err(|_| format!("Invalid port: {value}"))
}
```

### Enum for domain modeling
```rust
enum JobStatus {
    Pending,
    Running,
    Failed(String),
    Completed,
}
```

### Trait implementation
```rust
trait Render {
    fn render(&self) -> String;
}

impl Render for JobStatus {
    fn render(&self) -> String {
        match self {
            JobStatus::Pending => "pending".to_string(),
            JobStatus::Running => "running".to_string(),
            JobStatus::Failed(reason) => format!("failed: {reason}"),
            JobStatus::Completed => "completed".to_string(),
        }
    }
}
```

### Async function with `tokio`
```rust
async fn fetch_text(url: &str) -> Result<String, reqwest::Error> {
    let response = reqwest::get(url).await?;
    response.text().await
}
```

## Best Practices

- Prefer clear ownership models over fighting the borrow checker
- Use enums and pattern matching to make states explicit
- Keep functions small and focused, especially around I/O boundaries
- Return rich errors where callers need context; avoid `unwrap()` in production paths
- Reuse iterators and standard library utilities before introducing custom abstractions
- Keep `Cargo.toml` dependencies minimal and feature flags deliberate
- Run `cargo fmt` and `cargo clippy` for any non-trivial change
- Add tests for behavior, parsing, and edge cases near the touched logic

## Troubleshooting

### Borrow checker errors
- Check whether references outlive the owned value they point to
- Decide explicitly between borrowing, moving, or cloning
- Reduce overlapping mutable and immutable borrows by narrowing scopes

### Lifetime complexity
- Prefer restructuring data flow before adding explicit lifetime parameters
- Return owned values when borrowed outputs create unnecessary coupling
- Introduce lifetimes only when the borrowing relationship is truly required

### Async or concurrency issues
- Confirm futures and shared state satisfy `Send`/`Sync` requirements where needed
- Use `Arc`, `Mutex`, or channels intentionally, not by default
- Avoid holding locks across `.await` points

### Cargo or build failures
- Check feature mismatches and crate version compatibility
- Re-run focused commands like `cargo check` before full test suites
- Inspect target-specific dependencies and workspace configuration

### Clippy or formatting churn
- Fix substantive lints first and avoid silencing warnings without reason
- Accept idiomatic rewrites when they improve clarity and safety
- Keep style changes scoped to touched code unless the user requested broader cleanup

## Integration Points

- **Web frameworks**: Axum, Actix Web, Rocket, Warp
- **Async runtime**: Tokio, async-std
- **CLI tooling**: clap, argh, structopt
- **Serialization**: serde, serde_json, toml
- **Databases**: sqlx, diesel, tokio-postgres, rusqlite
- **Testing**: built-in test framework, tokio::test, insta, proptest
- **Quality tools**: cargo fmt, cargo clippy, cargo check, cargo bench
- **FFI and systems work**: bindgen, cbindgen, libc
