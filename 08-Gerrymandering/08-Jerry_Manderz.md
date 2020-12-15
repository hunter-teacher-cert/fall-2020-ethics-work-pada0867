# Mr. Jerry Manderz (Gerrymandering algorithm)
by Jack Padalino and Daniel Moscoe

-----

## Replit link to algorithm ##

https://repl.it/@JPads0867/Mr-Jerry-Manderz#main.py

---

The methods we put in main.py try to respond to the question, which arrangements of voters are most/least gerrymanderable? we thought, for a given arrangement of voters, a histogram would be helpful. The histogram shows how much power a voter arrangement would have in different states. Let's say a voter arrangement has the histogram [170,0,0,0]. That means that in all 170 states, that voter arrangement controls zero districts. That arrangement of voters is not gerrymanderable. If the histogram is [10,30,50,80], then in 10 states this arrangement of voters controls 0 districts. In 30 states they control 1 district. In 50 states they control 2 districts. In 80 states they control 3 districts. (It's impossible for an arrangement of 6 voters on 18 squares to control more than 3 districts.) So this arrangement of voters is highly gerrymanderable: depending on how the state is designed, they can control 0, 1, 2, or 3 districts.

But, we still need to know exactly which states give which results. So StatesWithNDistrictsWon tells us exactly which states are part of each entry in the histogram.

One thing we have not figured out yet is how to use the contents of a file as input to a method. we have the files, and when we copy and paste them into the code, everything seems to work. But we don't know how to keep the input hidden in the file. That's why there's no testing here yet.