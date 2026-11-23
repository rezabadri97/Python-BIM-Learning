from typing import Any, Dict, List

raw_elements: List[Dict[str, Any]] = [
    {"id": 4001, "category": "Walls", "level": "L01", "cost": 4500.0, "parameters": {"Phase": "New", "Comments": ""}},
    {"id": 4002, "category": "Doors", "level": "L01", "cost": 1200.0, "parameters": {"Phase": "New", "Comments": ""}},
    {"id": 4003, "category": "Windows", "level": "L02", "cost": 2800.0, "parameters": {"Phase": "Existing", "Comments": "Old"}},
    {"id": 4004, "category": "Columns", "level": "L01", "cost": 6200.0, "parameters": {"Phase": "New", "Comments": ""}},
    {"id": 4005, "category": "Walls", "level": "L02", "cost": 3100.0, "parameters": {"Phase": "New", "Comments": ""}},
    {"id": 4006, "category": "Doors", "level": "L02", "cost": 950.0, "parameters": {"Phase": "Existing", "Comments": ""}},
]

def filtered_by_categories(elements: List[Dict[str,Any]], *categories: str) -> List[Dict[str,any]]: 
    """Filter Revit elements matching any of the given category names."""
    
    if not categories:
        return []

    return [elem for elem in elements if elem["categories"] in categories]

def batch_update_parameters(elements: List[Dict[str, Any]], **param_updates: Any) -> int:
    if not elements or not param_updates:
        return 0
    updated_count = 0
    for element in elements:
        for param_name, param_value in param_updates.items():
            element["paramiters"][param_name]=param_value
        updated_count +=1
    return updated_count

