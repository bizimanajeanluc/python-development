# Create a dictionary storing service configuration settings
config = {"host": "localhost", "port": 8080, "debug": True}

# get(): Read "port" safely, returning a fallback (5432) if "db_port" is missing
db_port = config.get("db_port", 5432)
print("Fallback db_port:", db_port)

# setdefault(): Return existing "debug" value, or insert "workers": 4 if "workers" is absent
debug_flag = config.setdefault("debug", False)
workers_count = config.setdefault("workers", 4)
print("debug_flag:", debug_flag, "| workers_count:", workers_count)

# update(): Merge new settings and overwrite existing keys like "port"
config.update({"port": 9000, "env": "staging"})

# pop(): Remove "env" and retrieve its value, using a default if absent
removed_env = config.pop("env", "none")
print("Removed env:", removed_env)

# popitem(): Remove and return the most recently inserted key-value pair
last_pair = config.popitem()
print("Popped last item:", last_pair)

# keys(), values(), items(): Inspect live views of keys, values, and pairs
print("Keys:", list(config.keys()))
print("Values:", list(config.values()))
print("Items:", list(config.items()))

# fromkeys(): Build a new dictionary with shared default values for a list of feature flags
feature_flags = dict.fromkeys(["caching", "metrics", "audit"], False)
print("Feature flags:", feature_flags)

# copy(): Create a shallow copy so changes to config do not alter config_copy
config_copy = config.copy()
print("Config copy:", config_copy)

# clear(): Remove all entries from config when tearing down the session state
config.clear()
print("Config after clear:", config)