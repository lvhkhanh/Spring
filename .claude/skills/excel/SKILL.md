---
name: excel
description: '**WORKFLOW SKILL** — Create, refactor, and automate Excel-related solutions in Python, VBA, and integration tools. USE FOR: reading/writing spreadsheets, formulas, pivot tables, charts, data cleanup, and Office automation. DO NOT USE FOR: non-spreadsheet data workflows, complex OLAP cube modeling. INVOKES: file system tools for creating/editing script files, terminal for dependency installation, platform APIs for Excel automation guidance.'
---

# Excel Spreadsheet Automation Skill

## Overview

This skill provides guidance across Excel automation tasks including reading/writing XLSX and CSV files, data transformation, formula creation, charting, VBA macros, and Office integration. It is designed for both rapid scripting and robust process automation.

## Key Capabilities

### Data I/O
- Read/write XLSX and CSV with `openpyxl`, `pandas`, `xlrd`, `xlwt`, `xlsxwriter`
- Handle multi-sheet workbooks, named ranges, and table data
- Stream large sheets effectively using row iterators or chunked processing

### Transformations
- Normalize columns, cast types, fill missing values, deduplicate rows
- Generate pivot tables and summary tables programmatically
- Add computed columns with complex formula logic

### Presentation & charts
- Apply cell styling, formatting (dates, currency, percentages)
- Create charts (line, bar, scatter, pie) via `openpyxl` or Excel COM
- Freeze panes, auto-fit columns, conditional formatting

### Excel Automation
- Generate VBA macro scripts, modules, subroutines
- Automate task sequences (import, clean, analyze, report) with macros
- Use COM/Win32 interface on Windows (`pywin32`) and cross-platform alternatives

### Integration
- Export data for BI tools (Power BI, Tableau) via Excel/CSV
- Load workbook data into databases (PostgreSQL, MySQL, SQLite)
- Call REST APIs for data enrichment before writing to sheets

## Usage Examples

### 1. Read and clean sheet
```
Load workbook `sales.xlsx`, normalize headers, remove blank rows, format date columns, and write cleaned output to `sales_clean.xlsx`.
```

### 2. Generate pivot summary
```
From `financials.xlsx` sheet `transactions`, create a pivot by `region` and `category`, sum `amount`, and write to a new sheet `pivot_summary`.
```

### 3. VBA macro generation
```
Create a VBA module that loops through every worksheet, applies a standard report style and adds a company logo to top-left corner.
```

### 4. Batch export
```
Read multiple CSV files from `input/`, combine into one DataFrame, compute monthly totals, and export to `dashboard.xlsx` with a pivot and chart.
```

## Common Patterns

### Pandas read/write
```python
import pandas as pd

df = pd.read_excel('input.xlsx', sheet_name='Sheet1')
# transform
pd.to_datetime(df['date'], errors='coerce')
df.to_excel('output.xlsx', index=False, sheet_name='Cleaned')
```

### Using openpyxl for formatting
```python
from openpyxl import load_workbook
wb = load_workbook('output.xlsx')
ws = wb['Cleaned']
for cell in ws['A']:
    cell.number_format = 'YYYY-MM-DD'
wb.save('styled.xlsx')
```

### VBA macro snippet
```
Sub ApplyReportStyle()
  Dim ws As Worksheet
  For Each ws In ThisWorkbook.Worksheets
    ws.Cells.Interior.Color = RGB(255, 255, 255)
    ws.Range("A1:Z1").Font.Bold = True
  Next ws
End Sub
```

## Best Practices

- Use `pandas` for data-heavy operations; use `openpyxl` for precise formatting and charting
- Avoid editing the original file in-place; save to a new workbook for safety
- Validate workbook schema (expected sheets/columns) before processing
- Lock row/column indices in macros to avoid brittle references
- Use named ranges where possible for robustness in formulas
- Keep formulas readable and test with sample data before production deployment

## Troubleshooting

### File not found / permission errors
- Ensure Excel file paths are correct and not open in write-locked mode
- On Windows, close Excel applications or use `with` context for handles

### Data type issues
- Convert text dates by `pd.to_datetime`; remove non-numeric characters for numeric columns
- Use `errors='coerce'` for robust type coercion and inspect NaN values

### Performance bottlenecks
- Use vectorized operations in pandas instead of Python loops
- For large sheets, avoid `openpyxl` cell-by-cell writes and use `DataFrame.to_excel` when possible

## Integration Points

- **BI**: Power BI, Tableau via CSV/Excel exports
- **Database**: Bulk insert via SQLAlchemy from Pandas
- **Cloud**: Google Sheets API and Office 365 Graph API for sheet management
- **CI/CD**: validate Excel outputs in automated tests (compare datasets, schema)
