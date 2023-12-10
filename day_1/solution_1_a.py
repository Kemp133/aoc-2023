
"""
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
"""


def main():
    calibration_value = 0

    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            line_len = len(line)
            start_value, end_value = None, None

            for i in range(line_len):
                if start_value and end_value:
                    break

                start, end = line[i], line[line_len - 1 - i]

                if not start_value and start.isnumeric():
                    start_value = start
                if not end_value and end.isnumeric():
                    end_value = end

            to_add = int(start_value + end_value)

            print(to_add)

            calibration_value += to_add

        print(f"Calibration value: {calibration_value}")


if __name__ == "__main__":
    main()
