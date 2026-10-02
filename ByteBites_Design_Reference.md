# ByteBites Design Reference

Context file for AI assistants. Attach it to a chat so every answer starts from the same ground rules.

## Project Overview

ByteBites is a campus food ordering app. This repo holds only the **backend core logic**:
four Python classes, a Mermaid class diagram, and pytest tests. The source of truth for
requirements is `bytebites_spec.md`.

## Behavioral Instructions

- **Scope: exactly four classes** — `Customer`, `MenuItem`, `Menu`, `Order`. Do not add
  classes (no `Restaurant`, `Payment`, `Recommender`, `Database`, etc.). If you think one is
  needed, say so in a note instead of adding it.
- **Only attributes the spec names.**
  - Customer: name, purchase history.
  - MenuItem: name, price, category, popularity rating.
  - Menu: collection of MenuItems.
  - Order: selected items.
- **Only behaviors the spec names**: verify a customer, filter a menu by category, sort a
  menu, add items to an order, compute an order total. No recommendations, discounts, taxes,
  payments, persistence, or UI.
- **Mermaid format**: `classDiagram`. Use `-->` (association, "has a") for every relationship.
  No inheritance (`--|>`) unless asked. Show attributes with types and key methods.
- **Python**: 3.9+ standard library only. Plain classes, type hints, short docstrings.
  No dataclass magic or third-party packages unless asked.
- **Non-mutating queries**: filter and sort methods return new lists and leave the menu
  untouched.
- **Validate at the boundary**: reject empty names and negative prices with `ValueError`.
- **Tests**: pytest, one behavior per test, named `test_<behavior>`. Cover happy path and
  edge cases (empty order, unknown category, case differences).
- **Verify, don't assume**: when unsure what the spec means, ask or state the assumption.
  Before saying something works, run it.

## Glossary

| Term | Meaning here |
|------|--------------|
| Category | Free-text label such as "Drinks", "Desserts", "Burgers" |
| Popularity rating | Non-negative number; higher is more popular |
| Purchase history | List of a customer's past `Order` objects |
| Verified customer | Has a non-empty name and at least one past order |

## Out of Scope

AI recommendations, pairing logic, payment processing, inventory, user accounts and
passwords, web or mobile UI, databases.
