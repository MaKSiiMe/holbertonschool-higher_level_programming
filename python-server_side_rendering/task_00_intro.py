#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    """
    Generate a list of invitations from a template and a list of attendees.
    """
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return

    if not isinstance(attendees, list) or \
            not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return

    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        try:
            invitation = template
            for key in ["name", "event_title", "event_date", "event_location"]:
                value = attendee.get(key, "N/A")
                placeholder = f"{{{key}}}"
                invitation = invitation.replace(
                    placeholder, value if value else "N/A"
                )

            output_filename = f"output_{index}.txt"

            if os.path.exists(output_filename):
                print(
                    f"Warning: {output_filename} already exists and "
                    "will be overwritten."
                )

            with open(output_filename, "w") as output_file:
                output_file.write(invitation)

            print(f"Generated: {output_filename}")

        except Exception as e:
            print(
                f"Error: Failed to generate invitation for attendee {index}. "
                f"Reason: {e}"
            )
