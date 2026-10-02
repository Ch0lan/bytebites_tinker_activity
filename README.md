# ByteBites

Core backend logic for a campus food-ordering app: four Python classes, a Mermaid design, and pytest tests.

```
python3 models.py        # demo scenario
python3 -m pytest        # 18 tests
```

| File | Purpose |
|------|---------|
| `bytebites_spec.md` | Client request + the four candidate classes |
| `ByteBites_Design_Reference.md` | Behavioral instructions for AI assistants (scope, format, rules) |
| `draft_from_copilot.mmd` | Unconstrained first draft (spec only) |
| `bytebites_design.mmd` | Final Mermaid class diagram |
| `models.py` | `Customer`, `MenuItem`, `Menu`, `Order` |
| `test_bytebites.py` | pytest suite |

## Design notes

- **Reference file effect:** the unconstrained draft invented `Restaurant`, `Payment`, `Recommendation`, a
  login/password on `Customer`, made `Order` inherit from `Customer` (`<|--`), and dropped `popularity`.
  With the reference file the diagram has exactly four classes, only `-->` arrows, and `MenuItem.popularity`
  is back. `Menu` and `Order` now clearly hold `MenuItem`s.
- **Assumptions:** "verified" customer = non-empty name and at least one past order. Popularity is any
  non-negative number. Category matching ignores case and whitespace. Sorting returns new lists
  (popularity high to low, price low to high) and never mutates the menu.
- **Removed from AI-style output:** login/register, order status/checkout, payment, recommendations.
- **Most important test:** `test_calculate_total_with_multiple_items` protects the "compute total cost" requirement.
