---
name: ebcdic
description: '**WORKFLOW SKILL** — Analyze, convert, validate, and troubleshoot EBCDIC data from IBM mainframe and IBM i systems. USE FOR: EBCDIC-to-ASCII/UTF-8 conversion, code page identification, fixed-width record layouts, COBOL copybooks, RPG/DDS fields, packed decimal, zoned decimal, signed numeric fields, hex dump analysis, and migration validation. DO NOT USE FOR: generic text encoding issues unrelated to EBCDIC, relational SQL design, or destructive data conversion without verified backups and human approval. INVOKES: file system tools for sample files and layouts, terminal tools for read-only hex/encoding inspection, and scripts only when conversion behavior is explicit and testable.'
---

# EBCDIC Conversion Skill

## Overview

This skill supports legacy data modernization where records are encoded in EBCDIC or contain IBM-specific numeric formats. It focuses on preserving byte-level meaning while converting files into ASCII, UTF-8, CSV, JSON, database rows, or application DTOs.

## Key Capabilities

### Encoding Analysis
- Identify likely EBCDIC code pages such as IBM037, IBM500, IBM1047, and IBM273 from context and samples.
- Compare decoded output across candidate code pages before recommending one.
- Inspect hex dumps and byte distributions for control characters, record separators, and field boundaries.
- Document assumptions when the source code page is not confirmed.

### Record Layout Mapping
- Interpret COBOL copybooks, RPG field definitions, DDS layouts, and fixed-width field maps.
- Split records by byte offsets, lengths, occurrence groups, redefines, and filler fields.
- Distinguish display text fields from binary, packed decimal, zoned decimal, and signed numeric fields.
- Preserve field-level metadata for downstream Java, Kotlin, Python, SQL, or ETL code.

### Numeric Conversion
- Decode packed decimal / COMP-3 fields with correct scale and sign nibble handling.
- Decode zoned decimal fields and trailing or leading sign conventions.
- Flag ambiguous binary fields such as COMP, COMP-4, integer, float, or platform-endian values.
- Generate validation examples for positive, negative, zero, and blank numeric values.

### Migration Validation
- Create byte-preserving characterization tests from sample records.
- Compare source and converted totals, counts, keys, dates, signs, and field lengths.
- Recommend round-trip checks when conversion must be reversible.
- Produce exception handling rules for invalid bytes, malformed numerics, short records, and unknown layouts.

## Usage Examples

### Decode a Fixed-Width Customer File
```text
Analyze this EBCDIC file layout:
- code page: IBM037
- record length: 128 bytes
- fields: customer number 1-10, name 11-50, balance packed decimal 51-56 scale 2
Generate a conversion plan and validation checks.
```

### Review a Copybook Conversion
```text
Review this COBOL copybook and identify which fields are safe text conversion,
which require packed/zoned decimal decoding, and which need sample bytes before conversion.
```

### Hex Dump Investigation
```text
Given these sample bytes and expected business values, identify whether the record
uses IBM037 or IBM500 and explain any characters that differ.
```

## Common Patterns

### Safe Conversion Workflow
1. Confirm source system, code page, record length, and file transfer mode.
2. Gather sample records plus expected decoded values from a business owner or legacy report.
3. Map each field by byte offset and type before converting entire records.
4. Convert text fields using the confirmed EBCDIC code page.
5. Decode numeric fields with explicit packed/zoned/binary rules.
6. Validate counts, totals, keys, date ranges, and error rows.
7. Keep original bytes available until acceptance checks pass.

### Python Text Decode Example
```python
raw = b"\xc8\xc5\xd3\xd3\xd6"
text = raw.decode("cp037")
assert text == "HELLO"
```

### Packed Decimal Reminder
```text
Packed decimal stores two digits per byte, with the final low nibble carrying the sign.
Common positive signs include C and F; common negative sign is D.
Always confirm local convention before bulk conversion.
```

## Best Practices

- Never decode an entire record as text when it contains packed, zoned, binary, or date fields.
- Avoid guessing the code page from English-looking output alone; punctuation and currency symbols often reveal mismatches.
- Treat FTP transfer mode as part of the evidence: ASCII mode may already have changed bytes.
- Preserve original byte offsets in conversion notes and generated schemas.
- Build tests from known records, not only synthetic examples.
- Keep malformed rows in an error file or quarantine table for review.
- Do not write converted data into production destinations without explicit approval.

## Troubleshooting

### Garbled Text
- Compare IBM037, IBM500, and IBM1047 on the same byte sample.
- Check whether the file was already converted during transfer.
- Verify that packed/binary fields were not decoded as text.

### Wrong Numeric Values
- Confirm packed decimal length, precision, scale, and sign nibble.
- Check for zoned decimal signs in the first or last byte.
- Validate blank numeric fields and local null conventions.

### Record Alignment Problems
- Confirm fixed record length and line-ending handling.
- Check for variable-length records, block descriptors, or headers/trailers.
- Use byte offsets rather than character offsets after decoding.

## Integration Points

- **COBOL**: copybooks, PIC clauses, COMP-3, zoned decimals, redefines.
- **RPG / IBM i**: DDS fields, physical files, display numerics, packed fields.
- **ETL**: staging tables, quarantine files, reconciliation reports.
- **Modern Apps**: Java/Kotlin/Python parsers, DTOs, CSV/JSON exports, database loaders.
