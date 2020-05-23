# Command-line tooling to work up well-mixed breakout sessions

Sometimes you want to "mix people up" using small-group activities or "breakout
sessions." To give everyone maximum exposure to the others in an intimate
setting, you schedule multiple rounds of breakouts where no two people land in
multiple breakouts together. In other words, every participant meets all new
people in every breakout. The desire for well-mixed breakouts comes up in
networking events, seminars, corporate team-building efforts, and the
classroom.

This tool takes advantage of tabulated exact solutions to the "Social Golfer
Problem" (SGP) from combinatorics to schedule these breakouts. You put in a
list of people and get out a PDF schedule of the breakouts.

The tabulated SGP solutions support the following ranges of individuals:

- 5-16 people in groups of 2
- 7-27 people in groups of 3
- 9-32 people in groups of 4

If the number of people isn't a multiple of the group size, some groups will be
smaller. For example, breaking an odd number of people into pairs means that
someone is going to be alone in each round. This tool handles this issue
automatically.

The system requirements are a UNIX-like environment with Python 3 and Pandoc.

## Quickstart

Your event has the 19 attendees (these are fake names) listed in `example.csv`.
You want to organize breakouts of up to 4 people (you'd need 16 or 20 to have
everyone in groups of exactly 4, so one group will need to be short a person).
You have the time for 3 breakouts.

Clone this repo. Then run the tool like this:

```./make_schedule.py example.csv 4 3 | pandoc -o example.pdf```

`example.pdf` contains the schedule. You can view with a system viewer or print
it out for your event plans.
