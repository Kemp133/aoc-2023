

def main():
    calibration_value = 0

    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            line_len = len(line)
            start_value, end_value = None, None
            ltr, rtl = "", ""

            for i in range(line_len):
                # If both values set, return early
                if start_value and end_value:
                    break

                # Get current start and end index
                start, end = line[i], line[line_len - 1 - i]

                # Append characters to the left-to-right and right-to-left strings
                ltr = ltr + start
                rtl = rtl + end

                # Scan the ltr and rtl strings for text based values
                ltr_res, rtl_res = check_for_text_nums(ltr, rtl)

                if not start_value:
                    if start.isnumeric():
                        start_value = start
                    elif ltr_res:
                        start_value = str(ltr_res)

                if not end_value:
                    if end.isnumeric():
                        end_value = end
                    elif rtl_res:
                        end_value = str(rtl_res)

            to_add = int(start_value + end_value)

            print(to_add)

            calibration_value += to_add

        print(f"Calibration value: {calibration_value}")


def check_for_text_nums(ltr: str, rtl: str):
    vals = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    ltr_res, rtl_res = None, None

    rtl_rev = rtl[::-1]

    for key in vals:
        if not ltr_res and key in ltr:
            ltr_res = vals[key]
        if not rtl_res and key in rtl_rev:
            rtl_res = vals[key]

    return ltr_res, rtl_res


if __name__ == "__main__":
    main()
