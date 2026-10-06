"""Extended transparent scholarship screening rule.
The two added conditions (GPA and recommendation) are synthetic lab assumptions.
Exactly four core cases are included: pass, each added-condition failure, boundary.
"""

def scholarship_decision(score, documents_complete, gpa, recommendation):
    if not documents_complete:
        return "Hold", "documents incomplete"
    if score < 70:
        return "Hold", "score below synthetic threshold 70"
    if gpa < 3.0:
        return "Hold", "GPA below synthetic threshold 3.0"
    if not recommendation:
        return "Hold", "recommendation missing"
    return "Review", "all transparent conditions satisfied"

cases = [
    {"name":"pass", "score":82, "documents_complete":True, "gpa":3.5, "recommendation":True, "expected":"Review"},
    {"name":"gpa_failure", "score":82, "documents_complete":True, "gpa":2.9, "recommendation":True, "expected":"Hold"},
    {"name":"recommendation_failure", "score":82, "documents_complete":True, "gpa":3.5, "recommendation":False, "expected":"Hold"},
    {"name":"score_boundary", "score":70, "documents_complete":True, "gpa":3.0, "recommendation":True, "expected":"Review"},
]
print("name | input | expected | actual | pass | reason")
for c in cases:
    actual, reason = scholarship_decision(c["score"], c["documents_complete"], c["gpa"], c["recommendation"])
    ok = actual == c["expected"]
    inputs = f"score={c['score']}, complete={c['documents_complete']}, gpa={c['gpa']}, recommendation={c['recommendation']}"
    print(c["name"], inputs, c["expected"], actual, ok, reason, sep=" | ")
