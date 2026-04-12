from pymongo import MongoClient
from datetime import datetime

class Database:
    def __init__(self):
        try:
            self.client = MongoClient(
                "mongodb://localhost:27017/",
                serverSelectionTimeoutMS=2000  
            )

            # Force connection test
            self.client.server_info()

            self.db = self.client["mini_math_app"]
            self.history = self.db["history"]
            self.variables = self.db["variables"]

            self.connected = True

        except Exception:
            print("⚠️ MongoDB not running. Using fallback memory.")
            self.connected = False
            self.memory_vars = {}
            self.memory_history = []

    # ---------- VARIABLES ----------
    def save_variable(self, name, value):
        if self.connected:
            self.variables.update_one(
                {"name": name},
                {"$set": {"value": value}},
                upsert=True
            )
        else:
            self.memory_vars[name] = value

    def get_variable(self, name):
        if self.connected:
            var = self.variables.find_one({"name": name})
            return var["value"] if var else None
        else:
            return self.memory_vars.get(name)

    # ---------- HISTORY ----------
    def save_history(self, expr, result):
        if self.connected:
            self.history.insert_one({
                "expression": expr,
                "result": result,
                "timestamp": datetime.utcnow()
            })
        else:
            self.memory_history.append((expr, result))

    def get_history(self):
        if self.connected:
            return list(self.history.find().sort("timestamp", -1))
        else:
            return [
                {"expression": e, "result": r}
                for e, r in self.memory_history
            ]