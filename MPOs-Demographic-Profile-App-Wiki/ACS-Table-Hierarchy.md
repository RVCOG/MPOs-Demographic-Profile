## ACS Table Hierarchy: Main Categories and Sub-Categories

### Overview

American Community Survey (ACS) tables utilize a hierarchical variable structure that can be difficult to interpret during data extraction, transformation, aggregation, and statistical analysis. The distinction between a table's main categories and sub-categories is not always immediately apparent from the column headers, particularly when working with downloaded ACS datasets or Census API outputs.

Understanding these hierarchical relationships is essential for ensuring analytical accuracy and preventing aggregation errors.

---

## ACS Header Structure

Most ACS tables contain one or more top-level variables that represent the total universe for a given geography. A common example is:

```text
Estimate!!Total:
```

In most ACS tables, this variable represents the total population, total households, total housing units, or another overall count associated with the table universe.

Additional variables may appear beneath the total category and provide breakdowns of that overall estimate. For example:

```text
Estimate!!Total:
Estimate!!Total:!!Income in the past 12 months below poverty level:
Estimate!!Total:!!Income in the past 12 months at or above poverty level:
```

In this example:

- `Estimate!!Total:` is the parent (main) category.
- `Estimate!!Total:!!Income in the past 12 months below poverty level:` is a child category.
- `Estimate!!Total:!!Income in the past 12 months at or above poverty level:` is a child category.

The two poverty-status variables represent subdivisions of the total population and should be interpreted as component categories rather than independent totals.

---

## Understanding the ACS Hierarchy

ACS variables are organized as a hierarchical tree structure. Each level in the hierarchy provides additional detail about the category above it.

Example:

```text
Estimate!!Total:
Estimate!!Total:!!Male:
Estimate!!Total:!!Male:!!Under 5 years
Estimate!!Total:!!Male:!!5 to 9 years
Estimate!!Total:!!Female:
Estimate!!Total:!!Female:!!Under 5 years
Estimate!!Total:!!Female:!!5 to 9 years
```

Hierarchy representation:

```text
Total
├── Male
│   ├── Under 5 years
│   └── 5 to 9 years
└── Female
    ├── Under 5 years
    └── 5 to 9 years
```

---

## How to Identify Main Categories and Sub-Categories

ACS headers use the delimiter `!!` to indicate hierarchical relationships.

Each additional occurrence of `!!` typically represents a deeper level within the hierarchy.

### Level Identification Example

| Variable Header | Hierarchy Level | Category Type |
|----------------|----------------|---------------|
| `Estimate!!Total:` | Level 1 | Main Category |
| `Estimate!!Total:!!Male:` | Level 2 | First-Level Sub-Category |
| `Estimate!!Total:!!Male:!!Under 5 years` | Level 3 | Second-Level Sub-Category |
| `Estimate!!Total:!!Male:!!5 to 9 years` | Level 3 | Second-Level Sub-Category |

### General Identification Rule

A variable should be considered a child (sub-category) when:

- Its header begins with the complete text of another variable.
- Additional segments are appended after a `!!` delimiter.

For example:

```text
Estimate!!Total:
Estimate!!Total:!!Male:
Estimate!!Total:!!Male:!!Under 5 years
```

The second variable is a child of the first, and the third variable is a child of the second.

---

## Why This Matters for Analysis

When calculating summary statistics, creating custom indicators, or aggregating ACS estimates, analysts must explicitly account for parent-child relationships within the table hierarchy.

Failure to do so may result in:

- Double counting observations.
- Inflated population, household, or housing unit totals.
- Invalid percentages and rates.
- Incorrect denominators.
- Misleading comparative analyses.
- Statistical inconsistencies across geographies.
- Errors in dashboards, reports, and derived metrics.

---

## Common Aggregation Error

Consider the following variables:

```text
Estimate!!Total:
Estimate!!Total:!!Income below poverty level:
Estimate!!Total:!!Income at or above poverty level:
```

The following calculation is incorrect:

```text
Estimate!!Total:
+ Estimate!!Total:!!Income below poverty level:
+ Estimate!!Total:!!Income at or above poverty level:
```

This operation results in double counting because the two poverty-status categories are already components of the total population represented by `Estimate!!Total:`.

---

## Parent Categories vs. Sibling Categories

When aggregating ACS estimates, analysts should understand the distinction between parent-child relationships and sibling relationships.

### Valid Aggregation

Siblings can often be aggregated when constructing broader categories:

```text
Estimate!!Total:!!Male:
+ Estimate!!Total:!!Female:
```

Because both categories partition the same parent universe.

### Invalid Aggregation

A parent category should never be added to any of its descendants:

```text
Estimate!!Total:
+ Estimate!!Total:!!Male:
```

Because the male population is already included within the total population.

---

## Recommended Validation Process

Before performing calculations or aggregations:

1. Identify the root-level (`Total`) variable.
2. Parse all variable labels using the `!!` delimiter.
3. Construct a parent-child hierarchy for the table.
4. Identify which variables are:
   - Parent categories.
   - First-level sub-categories.
   - Nested sub-categories.
5. Determine whether child categories are:
   - Mutually exclusive.
   - Collectively exhaustive.
   - Nested subsets of another category.
6. Verify aggregation logic before producing derived metrics.

---

## Using ACS Metadata to Validate Hierarchy

Analysts should not rely solely on variable names when determining relationships between ACS variables.

Whenever possible, review:

- ACS table metadata.
- ACS table shells.
- Census API variable definitions.
- ACS technical documentation.
- Data dictionary files associated with ACS releases.

These resources provide the authoritative hierarchy and should be used to validate parent-child relationships before performing calculations.

---

## Best Practice

> ACS tables should be treated as hierarchical data structures rather than flat datasets. Prior to aggregation, analysts must identify parent categories, child categories, and sibling categories to ensure that estimates are combined appropriately. Understanding these hierarchical relationships is critical for avoiding double counting, maintaining statistical validity, and producing accurate ACS-derived metrics and indicators.