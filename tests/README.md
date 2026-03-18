# Architectural Constraints & Tests

This directory contains the automated and manual textual tests used to validate the garden room plans against the core project requirements.

## How it works

I am the **Garden Room Strategist**, the automated quality gatekeeper for this project. My primary responsibility is to act as the "Test Runner."

1. Every time the `Master Plan` or blueprint is updated, I read all the tests in this folder.
2. I cross-reference these tests against the proposed architectural plans.
3. If any plan fails a test, or lacks the necessary detail to prove compliance, I will flag it and generate a "Gap Report" in the `thoughts/validation_results.md` file.

## Test Format

Each test in this directory represents a distinct, measurable requirement derived from the `decisions_log.md` and ongoing research. They ensure the building meets the user's specific acoustic, thermal, and functional goals.