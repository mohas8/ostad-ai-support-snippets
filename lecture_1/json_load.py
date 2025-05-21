import json

# Step 1: Load JSON data from file
with open("output.json", "r", encoding="utf-8") as f:
    data = json.load(f)


# Step 2: Access specific values
print("msg:", data["message"])
print("obj:", data["object"])

# # # Step 3: Update some values
# data["boolean"] = False
# data["number"] = data["number"] - 2  # birthday!
#
# #
# # # Step 4: Add new entries
# data["a"] =  "b"
#
#
# # # Step 5: Remove a key (if it exists)
# data.pop("new", None)  # safely remove without error
#
# # # Step 6: Loop through all key-value pairs
# for key, value in data.items():
#     print(f"{key}: {value}")
#
# print(data)
# # # Optional: Save the updated data back to file
# with open("output.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=2)