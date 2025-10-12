#!/usr/bin/env python3
"""
Personal Journal Entry Generator
A simple CLI tool to create daily journal entries with optional prompts.
"""

import os
import random
from datetime import datetime

# Self-reflection prompts for journal entries
PROMPTS = [
    "What made you smile today?",
    "What challenge did you overcome today?",
    "What are you grateful for today?",
    "What did you learn today?",
    "What goal did you work toward today?",
    "Who made a positive impact on your day?",
    "What would you like to improve tomorrow?",
    "What moment today made you feel proud?",
    "What emotion dominated your day and why?",
    "What act of kindness did you witness or perform today?",
    "What decision are you facing and what are your thoughts?",
    "What habit are you trying to build or break?",
    "What book, article, or content inspired you today?",
    "What conversation had the biggest impact on you today?",
    "What's one thing you want to remember about today?"
]

DEFAULT_JOURNAL_DIR = "journal_entries"


def ensure_journal_directory(directory):
    """Create journal directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created journal directory: {directory}")


def get_random_prompt():
    """Return a random journal prompt."""
    return random.choice(PROMPTS)


def get_filename():
    """Generate filename based on current date."""
    return datetime.now().strftime("%Y-%m-%d.txt")


def save_entry(directory, content):
    """Save journal entry to file."""
    ensure_journal_directory(directory)
    filename = get_filename()
    filepath = os.path.join(directory, filename)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filepath, 'a') as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"Entry at: {timestamp}\n")
        f.write(f"{'='*60}\n")
        f.write(content)
        f.write("\n")
    
    print(f"\nJournal entry saved to: {filepath}")


def main():
    """Main function to run the journal entry generator."""
    print("\n" + "="*60)
    print("Personal Journal Entry Generator")
    print("="*60)
    
    # Ask if user wants a prompt
    prompt_choice = input("\nWould you like a writing prompt? (y/n): ").lower()
    
    if prompt_choice == 'y':
        prompt = get_random_prompt()
        print(f"\nToday's prompt: {prompt}\n")
    
    # Get journal entry from user
    print("Enter your journal entry (type 'END' on a new line when done):\n")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    
    entry_content = '\n'.join(lines)
    
    if entry_content.strip():
        save_entry(DEFAULT_JOURNAL_DIR, entry_content)
        print("\nThank you for journaling today!")
    else:
        print("\nNo content entered. Journal entry not saved.")


if __name__ == "__main__":
    main()
