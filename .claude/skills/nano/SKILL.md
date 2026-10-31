---
name: nano
description: '**WORKFLOW SKILL** — Master GNU Nano terminal text editing. USE FOR: teaching Nano keyboard shortcuts, buffer and file management, search/replace, configuration, syntax highlighting, and efficient terminal editing workflows. DO NOT USE FOR: generic GUI editor advice or non-terminal editors. INVOKES: command reference examples, keybinding guidance, and Nano configuration tips.'
---

# GNU Nano Mastery Skill

## Overview

This skill helps users learn and master the GNU Nano terminal text editor. It covers keybindings, editing workflows, search and replace, file management, configuration, syntax highlighting, and efficient usage in shell-based development environments.

## Key Capabilities

### Editor Basics
- Open, save, and close files inside Nano.
- Move the cursor quickly with keyboard shortcuts.
- Cut, copy, and paste text using Nano's buffer commands.
- Undo and redo edits.

### Navigation and Search
- Use `Ctrl+W` to search text and `Ctrl+\` to replace.
- Search forward and backward, and repeat searches.
- Jump to specific line numbers with `Ctrl+_`.
- Navigate by word, paragraph, and screen.

### File and Buffer Management
- Open multiple files in one Nano session.
- Switch between open buffers and manage unsaved changes.
- Use `Ctrl+R` to read files or insert content from other files.
- Save current file or save as a new file.

### Configuration and Customization
- Configure Nano with `~/.nanorc`.
- Enable syntax highlighting for common languages.
- Set line numbers, auto-indent, soft wrapping, and tab behavior.
- Customize keybindings and external tool integration.

### Advanced Editing Patterns
- Use `Alt+A` to set mark and select text regions.
- Run spell check and execute external commands from Nano.
- Use `Ctrl+K` and `Ctrl+U` for cut and uncut operations.
- Manage indentation, comment blocks, and case conversion.

## Usage Examples

### Learn Nano Quick Commands
- `Ctrl+O` to save the current file.
- `Ctrl+X` to exit Nano.
- `Ctrl+G` to view help.
- `Ctrl+K` to cut a line and `Ctrl+U` to paste it.

### Search and Replace
- Search for `TODO` with `Ctrl+W TODO Enter`.
- Replace using `Ctrl+\` and provide the existing and replacement text.
- Use `Ctrl+T` within replace mode to access spell check or external filter tools.

### Configure Nano for Coding
- Add `set linenumbers` to `~/.nanorc`.
- Enable syntax highlighting for Python, Bash, or HTML.
- Set `set tabsize 4` and `set autoindent` for cleaner code editing.

### Edit Multiple Files
- Start Nano with `nano file1.txt file2.txt`.
- Switch between buffers with `Alt+N` and `Alt+P`.
- Save all open files as needed before exiting.

## Best Practices

- Keep your hands on the keyboard; Nano is designed for quick terminal editing without a mouse.
- Use `Ctrl+G` anytime you forget a keybinding.
- Save frequently with `Ctrl+O` and verify the filename before pressing Enter.
- Use `.nanorc` to persist preferred editor settings.
- Prefer `Ctrl+W` for targeted searches instead of manual scanning.

## Troubleshooting

- If Nano does not show syntax highlighting, verify `syntax` definitions are loaded in `~/.nanorc`.
- If the cursor behaves oddly, set `set nowrap` or `set softwrap` depending on preference.
- If paste doesn't work, use Nano's own cut/uncut buffer keys instead of terminal clipboard.

## Examples of Useful `.nanorc` Settings

```text
set autoindent
set linenumbers
set softwrap
set tabsize 4
include /usr/share/nano/*.nanorc
```

## When to Use This Skill

- Teaching someone how to edit files directly in a terminal environment.
- Helping developers become efficient with Nano while working on shell-based workflows.
- Advising on Nano configuration and syntax highlighting for code editing.
- Explaining Nano commands and solving common Nano editing problems.
