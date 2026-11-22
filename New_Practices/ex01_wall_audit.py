raw_walls = [
    {"id": 1001, "type_name": "Exterior - Brick 250mm", "length_ft": 32.8, "height_ft": 10.0, "thickness_mm": "250"},
    {"id": 1002, "type_name": "Interior - Gypsum 100mm", "length_ft": 16.4, "height_ft": 9.8, "thickness_mm": "100"},
    {"id": 1003, "type_name": "Core - Concrete 300mm", "length_ft": 20.0, "height_ft": 11.5, "thickness_mm": "300"},
    {"id": 1004, "type_name": "Interior - Block 150mm", "length_ft": 24.6, "height_ft": 10.0, "thickness_mm": "150"},
    {"id": 1005, "type_name": "Exterior - Concrete 200mm", "length_ft": 40.0, "height_ft": 10.0, "thickness_mm": "200"},
]
Feet_to_meters=0.3048
heavy_wall_ids=[]
total_area_m2=0.0
heavy_walls_count=0

for wall in raw_walls: 
    length=wall["length_ft"]*Feet_to_meters
    height=wall["height_ft"]*Feet_to_meters
    area=round(height*length,2)
    total_area_m2+=area

    thickness=int(wall["thickness_mm"])

    if thickness>200:
        heavy_wall_ids.append(wall["id"])
        heavy_walls_count+=1
        category="Heavy/Structural"
    else:
        category="Light Partition"

    print(f"Wall ID: {wall['id']} | Wall Type: {wall["type_name"]} | Wall Area: {area} | Wall Category: {category}")

print(f"Wall count: {len(raw_walls)}")
print(f"Total Area:{total_area_m2}")
print(f"Heavy Walls Count: {heavy_walls_count}")
print(f"Heavy Walls IDs: {heavy_wall_ids}")