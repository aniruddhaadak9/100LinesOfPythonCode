#!/usr/bin/env python3
"""
Daily Affirmation Generator
A simple CLI tool that displays a random positive affirmation.
"""

import random
import sys

# Collection of positive affirmations
AFFIRMATIONS = [
    "I am capable of achieving great things.",
    "Today is full of possibilities.",
    "I am worthy of love and respect.",
    "I choose to be confident and strong.",
    "Every challenge is an opportunity to grow.",
    "I believe in myself and my abilities.",
    "I am grateful for all the good in my life.",
    "I have the power to create positive change.",
    "I am learning and improving every day.",
    "My potential is limitless.",
    "I embrace my unique qualities.",
    "I am enough just as I am.",
    "Success is within my reach.",
    "I radiate positivity and confidence.",
    "I am making progress toward my goals.",
    "My thoughts create my reality.",
    "I am resilient and can overcome obstacles.",
    "I deserve happiness and success.",
    "I trust the journey of my life.",
    "I am filled with energy and enthusiasm.",
    "My mind is clear and focused.",
    "I attract positive experiences.",
    "I am proud of my accomplishments.",
    "I have everything I need within me.",
    "I am becoming the best version of myself.",
    "Today, I choose joy and peace.",
    "I am open to new opportunities.",
    "My dreams are valid and achievable.",
    "I release what no longer serves me.",
    "I am surrounded by love and support.",
    "I trust in my decisions and choices.",
    "I am patient with myself.",
    "Every day brings new blessings.",
    "I am courageous and face my fears.",
    "I create my own happiness.",
    "I am making a positive difference.",
    "My possibilities are endless.",
    "I welcome abundance into my life.",
    "I am confident in my unique path.",
    "I celebrate my progress, no matter how small."
]


def get_random_affirmation():
    """Return a random affirmation from the collection."""
    return random.choice(AFFIRMATIONS)


def display_affirmation(affirmation):
    """Display the affirmation in a formatted way."""
    border = "=" * (len(affirmation) + 4)
    print(f"\n{border}")
    print(f"  {affirmation}")
    print(f"{border}\n")


def main():
    """Main function to run the Daily Affirmation Generator."""
    try:
        affirmation = get_random_affirmation()
        display_affirmation(affirmation)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
