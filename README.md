# Arithmetic Expression Parser and Evaluator

## Overview
A Python implementation of a recursive descent parser that converts mathematical expressions into abstract syntax trees (AST) and evaluates them. Handles operator precedence, parentheses, and negative numbers.

## Features
- Supports basic arithmetic operators: `+`, `-`, `*`, `/`, `^` (power)
- Operator precedence handling:
  - Power (^): Highest
  - Multiplication/Division: Medium
  - Addition/Subtraction: Lowest
- Parentheses support for explicit precedence
- Negative number handling
- AST validation
- Tree visualization
- Comprehensive error handling:
  - Mismatched parentheses detection
  - Invalid expression structure validation

## Installation
No installation required. Requires Python 3.6+ and standard libraries.

# Parse expression into AST
expression = "3 + (5 * 2^3)"
parse_tree = parse(expression)

# Visualize the AST
printTree(parse_tree)

# Evaluate the expression
result = evaluate(parse_tree)  # Returns 43.0

# Validate AST structure
is_valid = isValid(parse_tree)  # Returns True

## Input Format Requirements
- Space-separated tokens (e.g., "3 + ( 2 * 5 )")
- Power operator: ^
- Parentheses must be space-separated: "( 3 + 2 )"

## Implementation Details
### Key Components
1. **Node Class**: 
   - Represents AST nodes with left/right children
2. **Parser**:
   - Recursive descent parsing
   - Parentheses handling through token grouping
   - Operator precedence via lowest precedence operator selection
3. **Evaluator**:
   - Recursive tree evaluation
   - Floating-point arithmetic
4. **Validator**:
   - Ensures operators have two operands
   - Verifies numbers are leaf nodes
### Algorithm Complexity
- Parsing: O(n) for well-parenthesized expressions
- Evaluation: O(n) tree traversal
- Space: O(n) for AST storage
## Example Test Cases
```
"6 + (3 - 4)/(4^(0 + 3))"   # = 5.9375
"-2 * 3 + 4"                # = -2.0
"(2*3 + 5*4 - 9/6)"         # = 24.5
"3^ (2+1) + (1+2) + (1+1)" # = 32.0
```
