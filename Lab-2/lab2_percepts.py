"""Stateful smart-classroom controller.
Temperature is Celsius. No hardware is controlled; modes are labels only.
"""
class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    @staticmethod
    def target_mode(temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"

    def act(self, temp, occupied):
        target = self.target_mode(temp, occupied)
        send_command = target != self.previous_mode
        previous = self.previous_mode
        self.previous_mode = target
        return previous, target, send_command

percepts = [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)]
agent = ClassroomAgent()
print("step | previous | temp | occupied | target | command")
for step, (temp, occupied) in enumerate(percepts, 1):
    previous, target, command = agent.act(temp, occupied)
    print(step, previous, temp, occupied, target, "SEND" if command else "NO_COMMAND", sep=" | ")
