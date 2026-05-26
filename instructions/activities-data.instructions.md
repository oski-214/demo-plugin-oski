---
applyTo: "app/backend/data/**/*.json"
---

# Activities Data Conventions

These rules apply whenever you read, create, or modify an activity entry in `app/backend/data/activities.json`.

## Activity key (name)

- Must be in Title Case: `"Chess Club"`, `"Gym Class"`, `"Drama Club"`.
- Never lowercase: `"chess club"`.
- Never add suffixes or parenthetical qualifiers: `"Chess Club (JSON)"`.

## Required fields

Every activity object must contain exactly these four fields:

| Field | Type | Description |
| ----- | ---- | ----------- |
| `description` | string | 1-2 professional sentences. No slang, no exclamation marks. |
| `schedule` | string | `"Days, HH:MM AM/PM - HH:MM AM/PM"` |
| `max_participants` | integer | A positive whole number, never a string |
| `participants` | array of strings | Student email addresses |

## Schedule format

```text
"Days, HH:MM AM/PM - HH:MM AM/PM"
```

Examples:

- `"Fridays, 3:30 PM - 5:00 PM"`
- `"Tuesdays and Thursdays, 3:30 PM - 4:30 PM"`
- `"Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM"`

Never use free-form text like `"tuesday afternoons"` or `"after school"`.

## Email addresses

- All emails must use the `@githubcopilot.edu` domain.
- External domains such as `@gmail.com` or `@hotmail.com` are not allowed.
- No duplicate emails within the same activity's `participants` array.

## Example of a valid entry

```json
"Drama Club": {
  "description": "Students rehearse and perform theatrical productions, developing public speaking and collaboration skills.",
  "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
  "max_participants": 15,
  "participants": ["alex@githubcopilot.edu", "jamie@githubcopilot.edu"]
}
```