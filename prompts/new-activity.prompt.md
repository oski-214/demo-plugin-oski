---
mode: agent
description: Add a new extracurricular activity to the school portal.
argument-hint: "[activity name], [schedule], [max participants], [short description]"
---

# New Activity

Add a new extracurricular activity to `app/backend/data/activities.json` in the current workspace.

## Step 1 - Gather information

If any of the following details were not provided as arguments, ask the user for them one question at a time:

1. Activity name - what is the activity called?
2. Schedule - which days and what time does it meet?
3. Max participants - what is the maximum number of students allowed?
4. Description - provide a brief description of the activity.

## Step 2 - Append the new entry

Once all four fields are collected:

1. Open `app/backend/data/activities.json` in the current workspace. If it does not exist, tell the user that this workspace does not contain the expected school activities data file.
2. Append a new top-level key-value pair to the root object using this template:

```json
"<Activity Name>": {
  "description": "<1-2 professional sentences describing the activity>",
  "schedule": "<Days, HH:MM AM/PM - HH:MM AM/PM>",
  "max_participants": <positive integer>,
  "participants": []
}
```

3. Save the file.
4. Confirm to the user which activity was added, including all field values.

Follow the activity data rules in `instructions/activities-data.instructions.md`.