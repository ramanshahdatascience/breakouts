# breakouts
Tooling to work up well-mixed breakout sessions

Prerequisites: UNIX-like environment with Python 3 and Pandoc.

The example is a list of 19 (fake) people who haven't met. Say you want to
organize breakout or mixer sessions in your event so attendees get to meet as
many new people as possible in a more intimate setting. Say you want to put
them in groups of 3-4 (you'd need 16 or 20 to have everyone in groups of
exactly 4, so a couple groups will need to be short a person). Say you have the
time for 3 breakout sessions.

Clone this repo, then:

```
chmod +x make_schedule.py
./make_schedule.py example.csv 4 3 | pandoc -o example.pdf
```
