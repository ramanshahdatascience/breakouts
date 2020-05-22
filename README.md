# Command-line tooling to work up well-mixed breakout sessions

This tool takes advantage of tabulated exact solutions to the "Social Golfer
Problem" from combinatorics to support practical event planning (e.g., for
breakout sessions on Zoom networking events).

At the time of writing, the tabulated SGP solutions support the following
ranges of individuals:

- 5-16 people in groups of 1-2
- 7-27 people in groups of 2-3
- 9-32 people in groups of 3-4

## Quickstart

*System requirements: UNIX-like environment with Python 3 and Pandoc.*

`example.csv` contains a list of 19 (fake) attendees to your event. Say you
want to organize breakout or mixer sessions in your event so attendees get to
meet each other in a more intimate setting. You want to avoid any. Say you want
to put them in groups of 3-4 (you'd need 16 or 20 to have everyone in groups of
exactly 4, so one groups will need to be short a person). Say you have the time
for 3 breakout sessions.

Clone this repo. The first time, you'll need to give permission to execute the
`make_schedule.py` script:

```chmod +x make_schedule.py```

Run the tool like this:

```./make_schedule.py example.csv 4 3 | pandoc -o example.pdf```

Now you can view `example.pdf` with a system viewer, print it out, etc.
