"""Public educational PM capability self-assessment; no external dependencies."""
import json
import sys
from pathlib import Path

DOMAINS=("Outcomes","Ownership","Planning","Capacity","Risk","Communications","Governance","Transition")
RECOMMENDATIONS={
 "Outcomes":"Create explicit measures of success before selecting solutions.",
 "Ownership":"Name an accountable sponsor and decision-maker.",
 "Planning":"Define deliverables, milestones and dependency owners.",
 "Capacity":"Review competing demand with actual role availability.",
 "Risk":"Track risks and issues separately and review mitigation owners.",
 "Communications":"Map audiences and agree communication triggers.",
 "Governance":"Establish proportionate approval and change control.",
 "Transition":"Define operations acceptance and benefits review."
}

def evaluate(scores):
    if set(scores)!=set(DOMAINS):
        raise ValueError("Provide exactly eight required domains")
    if any(type(v) is not int or not 1<=v<=5 for v in scores.values()):
        raise ValueError("Scores must be integers from 1 to 5")
    average=sum(scores.values())/len(DOMAINS)
    stage="Foundational" if average<2.5 else "Developing" if average<3.75 else "Established"
    weakest=sorted(DOMAINS,key=lambda x:(scores[x],x))[:3]
    return {"average":round(average,2),"stage":stage,
            "focus":[{"domain":d,"score":scores[d],"recommendation":RECOMMENDATIONS[d]} for d in weakest]}

def main(path):
    data=json.loads(Path(path).read_text(encoding="utf-8"))
    print(json.dumps(evaluate(data),indent=2))

if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("Usage: python assess.py examples/team-assessment.json")
    main(sys.argv[1])
