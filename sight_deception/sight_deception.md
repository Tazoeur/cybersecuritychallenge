# Sight deception

In this challenge (which is linked to the ["The blind"](../the_blind/the_blind.md) challenge), we got a script that convert an ascii string into spaces and tabulations.

A quick look at the file (ctrl+a) shows us that the file itself contains spaces and tabluations after the python code.

A quick regex deleting every characters before the end of the line allows us to isolate the information created by the spaces and the tabulations.

At this point it's exactly the same as the "The blind" challenge.
We convert every spaces into '0' and every tabulation into '1'.
This give us some binary words that represent the letters of the flag.
