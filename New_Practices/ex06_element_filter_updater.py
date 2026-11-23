# Exercise 06: Revit Multi-Category Filter, Batch Parameter Updater & Cost Ranker

from typing import Any, Dict, List

raw_elements: List[Dict[str, Any]] = [
    {"id": 4001, "category": "Walls", "level": "L01", "cost": 4500.0, "parameters": {"Phase": "New", "Comments": ""}},
    {"id": 4002, "category": "Doors", "level": "L01", "cost": 1200.0, "parameters": {"Phase": "New", "Comments": ""}},
    {"id": 4003, "category": "Windows", "level": "L02", "cost": 2800.0, "parameters": {"Phase": "Existing", "Comments": "Old"}},
    {"id": 4004, "category": "Columns", "level": "L01", "cost": 6200.0, "parameters": {"Phase": "New", "Comments": ""}},
    {"id": 4005, "category": "Walls", "level": "L02", "cost": 3100.0, "parameters": {"Phase": "New", "Comments": ""}},
    {"id": 4006, "category": "Doors", "level": "L02", "cost": 950.0, "parameters": {"Phase": "Existing", "Comments": ""}},
]


def filter_by_categories(
    elements: List[Dict[str, Any]],
    *categories: str,
) -> List[Dict[str, Any]]:
    """Filter Revit elements matching any of the given category names."""
    if not categories:
        return []

    return [elem for elem in elements if elem["category"] in categories]


def batch_update_parameters(
    elements: List[Dict[str, Any]],
    **param_updates: Any,
) -> int:
    """Batch-update Revit parameters on a list of elements and return updated count."""
    if not elements or not param_updates:
        return 0

    updated_count = 0
    for elem in elements:
        for param_name, param_value in param_updates.items():
            elem["parameters"][param_name] = param_value
        updated_count += 1

    return updated_count


def sort_elements_by_cost(
    elements: List[Dict[str, Any]],
    descending: bool = True,
) -> List[Dict[str, Any]]:
    """Return a new list of Revit elements sorted by cost."""
    return sorted(elements, key=lambda elem: elem["cost"], reverse=descending)


# Pipeline Step 1: Filter target categories
filtered_elements = filter_by_categories(raw_elements, "Walls", "Doors")

# Pipeline Step 2: Batch-update Revit parameters
updated_count = batch_update_parameters(
    filtered_elements,
    Phase="Construction",
    Approved=True,
    ReviewedBy="BIM_Team",
)

# Pipeline Step 3: Sort filtered elements from most expensive to cheapest
ranked_elements = sort_elements_by_cost(filtered_elements, descending=True)

print("--- REVIT FILTERED & UPDATED ELEMENTS (RANKED BY COST) ---")
for rank, elem in enumerate(ranked_elements, start=1):
    print(
        f"[{rank}] ID: {elem['id']} | {elem['category']} | Level: {elem['level']} | "
        f"Cost: ${elem['cost']} | Params: {elem['parameters']}"
    )

total_filtered_cost = round(sum(elem["cost"] for elem in ranked_elements), 2)

print("\n--- BATCH OPERATION SUMMARY ---")
print(f"Total Elements in Model: {len(raw_elements)}")
print(f"Filtered & Updated Elements: {updated_count}")
print(f"Total Cost of Filtered Elements: ${total_filtered_cost}")

if ranked_elements:
    top_elem = ranked_elements[0]
    print(f"Most Expensive Filtered Element: ID {top_elem['id']} (${top_elem['cost']})")