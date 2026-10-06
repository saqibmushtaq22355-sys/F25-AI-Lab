"""Small reflex/stateful comparison for the classroom agent."""
from lab2_percepts import ClassroomAgent

def reflex(temp, occupied):
    return ClassroomAgent.target_mode(temp, occupied)

if __name__ == "__main__":
    sequence = [(29, True), (29, True), (26, True), (26, True), (19, True), (29, False)]
    agent = ClassroomAgent()
    print("percept | reflex | stateful_target | command")
    for percept in sequence:
        previous, target, send = agent.act(*percept)
        print(percept, reflex(*percept), target, "SEND" if send else "NO_COMMAND", sep=" | ")
