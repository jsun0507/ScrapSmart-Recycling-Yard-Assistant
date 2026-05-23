from datetime import datetime

class RecyclingRecord:

    def __init__(self, record_id, material, weight, price_per_kg, record_time=None):
        self.record_id = record_id
        self.material = material
        self.weight = float(weight)
        self.price_per_kg = float(price_per_kg)
        self.income = round(self.weight * self.price_per_kg, 2)

        if record_time is None:
            self.record_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        else:
            self.record_time = record_time
    
    def to_dict(self):
        return {
            "record_id": self.record_id,
            "material": self.material,
            "weight": self.weight,
            "price_per_kg": self.price_per_kg,
            "income": round(self.income, 2),
            "record_time": self.record_time
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("record_id", "R000"),
            data["material"],
            data["weight"],
            data["price_per_kg"],
            data.get("record_time", "No time recorded")
        )

    def __str__(self):
        return (
            f"{self.record_id} | "
            f"{self.record_time} | "
            f"Material: {self.material.title()} | "
            f"Weight: {self.weight:.2f} kg | "
            f"Price: {self.price_per_kg:.2f}/kg | "
            f"Income: ${self.income:.2f}"
        )

