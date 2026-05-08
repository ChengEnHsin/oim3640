

# ✈️ Flight Risk & Crosswind Decision Tool

## Overview

This project is a Python based aviation decision support tool that helps evaluate whether flight conditions are safe based on weather inputs and pilot specific minimums.

As a student pilot with experience flying under Part 141 training, I wanted to build something that reflects real world decision making before a flight. This tool combines crosswind calculations with basic weather minimum checks to simulate a “go, caution, or no go” recommendation.

---

## Features

### 1. Crosswind & Wind Component Calculator

* Inputs:

  * Runway heading
  * Wind direction
  * Wind speed
* Outputs:

  * Crosswind component
  * Headwind or tailwind component

This uses trigonometric calculations to break wind into components relative to the runway, similar to real pilot calculations.

---

### 2. Flight Risk Evaluation Tool

* Inputs:

  * Crosswind component
  * Visibility
  * Ceiling

* Compares against pilot defined personal minimums

* Output:

  * **Go** → Conditions within safe limits
  * **Caution** → Marginal conditions, pilot discretion required
  * **No Go** → Conditions exceed safe limits

---

### 3. "Should I Fly Today?" — Story-Driven Decision App

* Inputs: same as above (runway, wind, visibility, ceiling, personal minimums)

* Instead of just outputting a verdict, the app **narrates the decision** from the perspective of a student pilot with ~70 hours of flight time

* The narrative explains:

  * What the crosswind feels like at this stage of training
  * Why visibility and ceiling matter beyond just legality
  * The reasoning and discipline behind a Go, Caution, or No Go call

* Output example (No Go):

  > "The decision is NO GO. I know it's disappointing to scrub a flight, but this is exactly the kind of discipline that keeps pilots alive long enough to keep flying. There will always be another day with better weather."

* Why this matters: aviation decision-making is not just math — it's judgment, experience, and knowing your own limits. This feature translates that human reasoning into code.

---

### 4. PPL Knowledge Check — Practice Questions

After each flight decision, the app offers an optional quiz to practice for the FAA Private Pilot written exam.

* Randomly selects 3 questions from a bank of 10 covering:

  * Airspace classes and requirements
  * Weather interpretation (METARs, SIGMETs)
  * ATC light signals
  * Navigation and course calculations
  * Pilot decision making and FARs

* For each question, the user selects A/B/C/D and receives immediate feedback

* Wrong answers include a plain-English explanation so each miss becomes a learning moment

* Score is shown at the end with a motivational note

* Questions are randomized each session so the quiz stays fresh across repeated use

---

## Example Scenario

Runway: 270
Wind: 210 at 15 knots

The program calculates:

* Crosswind component
* Headwind component

Then evaluates:

* Is crosswind within limits?
* Is visibility acceptable?
* Is ceiling high enough?

Final output provides a clear recommendation.

---

## Why I Built This

As someone pursuing a Private Pilot License with approximately 70 hours of flight time, I have learned that pre flight decision making is one of the most critical skills in aviation.

Rather than memorizing rules, I wanted to translate these decision processes into code. This project allowed me to apply programming concepts like conditionals, functions, and mathematical logic to a real world scenario that I personally care about.

---

## What I Learned

* How to apply trigonometry in Python to solve real problems
* Structuring decision making logic using conditionals
* Translating aviation concepts into computational steps
* Designing a simple tool that mimics real pilot workflows
* Using randomization to create replayable, educational content
* Writing narrative output that communicates reasoning, not just results

---

## Future Improvements

* Integrate real time weather data using an API
* Add different pilot profiles (student, private, instrument rated)
* Build a simple web interface for easier interaction
* Include runway database lookup instead of manual input

---

## Technologies Used

* Python
* `math` module for trigonometric calculations
* `random` module for quiz randomization
* `textwrap` module for formatted narrative output
* Basic input/output and conditional logic

---

## Reflection

This project was built beyond the required coursework as a way to connect my technical learning with my aviation background. It represents how I think about problem solving, not just writing code that works, but building something meaningful and applicable to real life decisions.
