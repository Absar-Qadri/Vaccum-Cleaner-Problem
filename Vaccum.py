class VacuumCleaner:
    def __init__(self, location="A"):
        self.location = location

    def move(self):
        if self.location == "A":
            self.location = "B"
        else:
            self.location = "A"

    def clean(self):
        print(f"Vacuum cleaner is cleaning at location {self.location}.")

    def run(self):
        print("Starting vacuum cleaner...")
        for i in range(5):
            self.clean()
            self.move()
        print("Vacuum cleaner has finished cleaning.")


if __name__ == "__main__":
    vacuum = VacuumCleaner()
    vacuum.run()
