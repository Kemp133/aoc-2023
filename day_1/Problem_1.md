# Day 1: Trebuchet?!

## Part `a`

### Problem

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine _("not powerful enough")_ and where they're even sending you _("the sky")_ and why your map looks mostly blank _("you sure ask a lot of questions")_ and hang on did you just say the sky _("of course, where do you think snow comes from")_ when you realize that the Elves are already loading you into a trebuchet _("please hold still, we need to strap you in")_.

As they're making the final adjustments, they discover that their **calibration document** _(your puzzle input)_ has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

### Problem details
The newly-improved calibration document consists of **lines of text;** each line originally contained a **specific calibration value** that the Elves now need to recover. On **each line**, the `calibration value` can be found by **combining** the `first digit` and the `last digit` (in that order) to form a `single two-digit number`.

For example:

- `1abc2`
- `pqr3stu8vwx`
- `a1b2c3d4e5f`
- `treb7uchet`

### Example solution

In this example, the `calibration values` of these four lines are `12`, `38`, `15`, and `77`. Adding these together produces `142`.

Consider your entire calibration document. What is the **sum of all of the calibration values**?

### Solution overview

- Create count value to total up the calibration values, `calibration_value`
- Read the strings in from the file row by row
- Get the length of the string
- initialise a `start` value and an `end` value
- Iterate forwards and backwards on the string at the same time for `len(input) / 2` times (integer divison of the length in half)
- As soon as first value is set, skip checking
- As above, but for the last value
- If the iteration terminates and only one of the values is set, the final value is `value * 2`
- Add parsed value to the global count value
- Finally, output the variable to the console as `f"Calibration value is: ${calibration_value}"`