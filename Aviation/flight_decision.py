import math
import random
import textwrap


PILOT_HOURS = 70
PILOT_STAGE = "student pilot"


def calculate_wind_components(runway_heading, wind_direction, wind_speed):
    angle_diff = math.radians(wind_direction - runway_heading)
    crosswind = abs(wind_speed * math.sin(angle_diff))
    headwind = wind_speed * math.cos(angle_diff)
    return crosswind, headwind


def evaluate_flight_conditions(crosswind, visibility, ceiling, minimums):
    issues = []
    cautions = []

    if crosswind > minimums["max_crosswind"]:
        issues.append(f"Crosswind {crosswind:.1f} kt exceeds limit of {minimums['max_crosswind']} kt")
    elif crosswind > minimums["max_crosswind"] * 0.8:
        cautions.append(f"Crosswind {crosswind:.1f} kt is near limit of {minimums['max_crosswind']} kt")

    if visibility < minimums["min_visibility"]:
        issues.append(f"Visibility {visibility} SM below minimum of {minimums['min_visibility']} SM")
    elif visibility < minimums["min_visibility"] * 1.5:
        cautions.append(f"Visibility {visibility} SM is marginal (minimum {minimums['min_visibility']} SM)")

    if ceiling < minimums["min_ceiling"]:
        issues.append(f"Ceiling {ceiling} ft below minimum of {minimums['min_ceiling']} ft")
    elif ceiling < minimums["min_ceiling"] * 1.5:
        cautions.append(f"Ceiling {ceiling} ft is marginal (minimum {minimums['min_ceiling']} ft)")

    if issues:
        return "NO GO", issues + cautions
    elif cautions:
        return "CAUTION", cautions
    else:
        return "GO", []


def build_narrative(decision, crosswind, headwind, visibility, ceiling, minimums):
    wrap = lambda text: "\n".join(textwrap.wrap(text, width=62))

    intro = (
        f"As a {PILOT_STAGE} with around {PILOT_HOURS} hours of flight time, "
        "I've learned that getting to the airport is the easy part — "
        "deciding whether to actually fly is where real airmanship begins."
    )

    wind_story = (
        f"Today the winds are giving us a crosswind component of {crosswind:.1f} kt "
        f"and a {'headwind' if headwind >= 0 else 'tailwind'} of {abs(headwind):.1f} kt. "
    )
    if crosswind <= minimums["max_crosswind"] * 0.5:
        wind_story += "That crosswind is very manageable — well within comfortable limits."
    elif crosswind <= minimums["max_crosswind"] * 0.8:
        wind_story += "That crosswind is workable, but it will demand my full attention on final and during the flare."
    elif crosswind <= minimums["max_crosswind"]:
        wind_story += (
            "That crosswind is within my personal limits, but just barely. "
            "At this stage of training, being near a limit is a signal to slow down and think."
        )
    else:
        wind_story += (
            f"That crosswind exceeds my personal maximum of {minimums['max_crosswind']} kt. "
            "No matter how tempting the flight is, pushing past my own limits is how accidents start."
        )

    vis_story = f"Visibility is sitting at {visibility} SM. "
    if visibility >= minimums["min_visibility"] * 2:
        vis_story += "Good VFR conditions — no concerns there."
    elif visibility >= minimums["min_visibility"]:
        vis_story += (
            "That's legal, but marginal visibility means less time to spot traffic "
            "and react to the unexpected."
        )
    else:
        vis_story += (
            f"At {visibility} SM, visibility falls below my {minimums['min_visibility']} SM minimum. "
            "Flying into reduced visibility without an instrument rating is a risk I won't take."
        )

    ceil_story = f"The ceiling is at {ceiling} ft. "
    if ceiling >= minimums["min_ceiling"] * 2:
        ceil_story += "Plenty of sky to work with."
    elif ceiling >= minimums["min_ceiling"]:
        ceil_story += (
            "That's within limits, but a low ceiling shrinks my options fast if something goes wrong."
        )
    else:
        ceil_story += (
            f"A ceiling of {ceiling} ft is below my {minimums['min_ceiling']} ft minimum. "
            "Scud-running is one of the deadliest traps in VFR flying."
        )

    if decision == "GO":
        closing = (
            "All conditions are within my personal minimums. "
            "The data says go — and just as importantly, my gut agrees. "
            "I'll conduct a thorough preflight, file my plan, and fly. "
            "Every good flight starts with an honest weather check like this one."
        )
    elif decision == "CAUTION":
        closing = (
            "Conditions are technically within limits, but marginal. "
            "My instructors always said: 'When in doubt, don't.' "
            "I'll take a closer look at the trend — is the weather improving or deteriorating? "
            "If I do fly, I'll set a personal weather turnaround point before I even start the engine."
        )
    else:
        closing = (
            "The decision is NO GO. "
            "I know it's disappointing to scrub a flight, but this is exactly the kind of "
            "discipline that keeps pilots alive long enough to keep flying. "
            "There will always be another day with better weather. "
            "The plane will still be there. I plan to be, too."
        )

    lines = [intro, wind_story, vis_story, ceil_story, closing]
    return "\n\n".join(wrap(line) for line in lines)


PPL_QUESTIONS = [
    {
        "q": "What is the minimum visibility required for VFR flight in Class G airspace below 1,200 ft AGL during the day?",
        "options": ["A) 1 SM", "B) 3 SM", "C) 5 SM", "D) 1/2 SM"],
        "answer": "A",
        "explanation": "FAR 91.155: Class G airspace below 1,200 ft AGL day VFR minimum is 1 SM with clear of clouds.",
    },
    {
        "q": "What does a steady red light signal from the tower mean to an aircraft in flight?",
        "options": ["A) Return for landing", "B) Give way and continue circling", "C) Airport unsafe, do not land", "D) Cleared to land"],
        "answer": "B",
        "explanation": "A steady red light to an aircraft in flight means 'Give way to other aircraft and continue circling.'",
    },
    {
        "q": "How is magnetic course determined?",
        "options": [
            "A) True course corrected for wind",
            "B) True course adjusted for magnetic variation",
            "C) Compass heading adjusted for deviation",
            "D) True heading adjusted for wind and variation",
        ],
        "answer": "B",
        "explanation": "Magnetic course = True course ± magnetic variation (East variation subtracts, West adds).",
    },
    {
        "q": "What is the maximum altitude for Class D airspace unless otherwise charted?",
        "options": ["A) 2,500 ft AGL", "B) 4,000 ft MSL", "C) 2,500 ft MSL", "D) 2,000 ft AGL"],
        "answer": "A",
        "explanation": "Class D airspace typically extends from the surface up to 2,500 ft AGL around airports with an operating control tower.",
    },
    {
        "q": "What does METAR code 'OVC010' mean?",
        "options": ["A) Overcast at 10,000 ft", "B) Overcast at 1,000 ft", "C) Overcast at 100 ft", "D) Obscured at 1,000 ft"],
        "answer": "B",
        "explanation": "In METARs, cloud heights are reported in hundreds of feet. OVC010 = overcast at 1,000 ft AGL.",
    },
    {
        "q": "During a cross-country flight, you notice your fuel is lower than expected. What should you do first?",
        "options": [
            "A) Continue to destination — you probably have enough",
            "B) Declare an emergency immediately",
            "C) Land at the nearest suitable airport and refuel",
            "D) Switch tanks and hope for the best",
        ],
        "answer": "C",
        "explanation": "Running out of fuel is entirely preventable. The safe and correct action is to divert and refuel rather than press on.",
    },
    {
        "q": "What is the runway visual range (RVR) threshold that defines a 'low visibility' takeoff?",
        "options": ["A) RVR 1,600 ft", "B) RVR 2,400 ft", "C) RVR 800 ft", "D) RVR 6,000 ft"],
        "answer": "A",
        "explanation": "Low visibility operations are generally defined as RVR below 1,600 ft under FAA standards.",
    },
    {
        "q": "Which flight condition is most likely to cause spatial disorientation?",
        "options": [
            "A) Flying in VMC with a visible horizon",
            "B) Flying in IMC without instrument training",
            "C) Flying at high altitude in clear air",
            "D) Flying over open water in daylight",
        ],
        "answer": "B",
        "explanation": "Spatial disorientation is most dangerous in IMC when a VFR pilot loses outside visual references and relies on faulty senses.",
    },
    {
        "q": "What does a SIGMET warn pilots about?",
        "options": [
            "A) Light turbulence along airways",
            "B) Significant meteorological conditions hazardous to all aircraft",
            "C) Surface winds above 20 knots",
            "D) Temporary flight restrictions",
        ],
        "answer": "B",
        "explanation": "SIGMETs (Significant Meteorological Information) advise of weather conditions hazardous to all aircraft, such as severe turbulence, icing, or volcanic ash.",
    },
    {
        "q": "When must a pilot report a deviation from an ATC clearance?",
        "options": [
            "A) Only if the deviation caused an incident",
            "B) As soon as possible after the deviation",
            "C) Within 24 hours by written report",
            "D) Never — deviations in emergencies are automatically excused",
        ],
        "answer": "B",
        "explanation": "FAR 91.123: A pilot must notify ATC as soon as possible after deviating from a clearance, even in an emergency.",
    },
]


def run_practice_quiz(num_questions=3):
    print(f"\n{'=' * 62}")
    print("  📚  PPL Knowledge Check — Practice Questions")
    print(f"{'=' * 62}")
    print(f"  Let's sharpen those written-test skills. {num_questions} random questions.\n")

    selected = random.sample(PPL_QUESTIONS, min(num_questions, len(PPL_QUESTIONS)))
    score = 0

    for i, item in enumerate(selected, 1):
        print(f"Q{i}: {item['q']}")
        for opt in item["options"]:
            print(f"     {opt}")
        answer = input("  Your answer (A/B/C/D): ").strip().upper()
        if answer == item["answer"]:
            print("  ✅ Correct!\n")
            score += 1
        else:
            print(f"  ❌ Incorrect. The answer is {item['answer']}.")
            print(f"     {item['explanation']}\n")

    print(f"  Result: {score}/{num_questions} correct")
    if score == num_questions:
        print("  Perfect score — you're ready for that checkride.")
    elif score >= num_questions // 2:
        print("  Good effort. Review the ones you missed and try again.")
    else:
        print("  Keep studying — the written test is passable with practice.")
    print(f"{'=' * 62}")


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("=" * 62)
    print("  ✈️  Should I Fly Today?  —  A Pilot Decision Simulator")
    print("=" * 62)
    print(f"\n  Pilot profile: {PILOT_STAGE}, ~{PILOT_HOURS} hours total time\n")

    print("--- Personal Minimums ---")
    print("(Press Enter to use defaults: 12 kt crosswind, 3 SM visibility, 1000 ft ceiling)\n")

    raw = input("Max crosswind (kt) [12]: ").strip()
    max_crosswind = float(raw) if raw else 12.0

    raw = input("Min visibility (SM) [3]: ").strip()
    min_visibility = float(raw) if raw else 3.0

    raw = input("Min ceiling (ft) [1000]: ").strip()
    min_ceiling = float(raw) if raw else 1000.0

    minimums = {
        "max_crosswind": max_crosswind,
        "min_visibility": min_visibility,
        "min_ceiling": min_ceiling,
    }

    print("\n--- Runway & Wind ---")
    runway_heading = get_float_input("Runway heading (e.g. 270): ")
    wind_direction = get_float_input("Wind direction (e.g. 210): ")
    wind_speed = get_float_input("Wind speed (kt): ")

    print("\n--- Current Weather ---")
    visibility = get_float_input("Visibility (SM): ")
    ceiling = get_float_input("Ceiling (ft): ")

    crosswind, headwind = calculate_wind_components(runway_heading, wind_direction, wind_speed)

    print(f"\n--- Wind Components ---")
    print(f"  Crosswind : {crosswind:.1f} kt")
    component_label = "Headwind" if headwind >= 0 else "Tailwind"
    print(f"  {component_label} : {abs(headwind):.1f} kt")

    decision, notes = evaluate_flight_conditions(crosswind, visibility, ceiling, minimums)

    VERDICT = {"GO": "✅  GO", "CAUTION": "⚠️   CAUTION", "NO GO": "🛑  NO GO"}
    print(f"\n{'=' * 62}")
    print(f"  VERDICT: {VERDICT[decision]}")
    print(f"{'=' * 62}")

    if notes:
        print("\n  Flagged conditions:")
        for note in notes:
            print(f"    • {note}")

    print(f"\n--- Pilot's Reasoning ---\n")
    print(build_narrative(decision, crosswind, headwind, visibility, ceiling, minimums))
    print(f"\n{'=' * 62}")

    again = input("\nWant to test your PPL knowledge? (y/n): ").strip().lower()
    if again == "y":
        run_practice_quiz()


if __name__ == "__main__":
    main()
