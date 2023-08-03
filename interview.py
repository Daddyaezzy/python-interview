from collections import Counter
import re
import random

# HTML data containing colors of dresses
html_data = '''
<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">
	
	body{
		width:1000px;
		margin: auto;
	}
	table,tr,td{
		border:solid;
		padding: 5px;
	}
	table{
		border-collapse: collapse;
		width:100%;
	}
	h3{
		font-size: 25px;
		color:green;
		text-align: center;
		margin-top: 100px;
	}
	p{
		font-size: 18px;
		font-weight: bold;
	}
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
	
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>
'''




# Function to extract colors from the HTML data using regular expression
def extract_colors(html_data):
    colors = re.findall(r'\b\w+\b', html_data)
    return colors

# Function to calculate mean color
def calculate_mean_color(colors):
    total_colors = len(colors)
    color_counter = Counter(colors)
    mean_color = color_counter.most_common(1)[0][0]
    return mean_color

# Function to calculate mode color (most frequently worn color)
def calculate_mode_color(colors):
    color_counter = Counter(colors)
    mode_color = color_counter.most_common(1)[0][0]
    return mode_color

# Function to calculate median color
def calculate_median_color(colors):
    sorted_colors = sorted(colors)
    mid = len(sorted_colors) // 2
    median_color = sorted_colors[mid] if len(sorted_colors) % 2 == 1 else sorted_colors[mid-1]
    return median_color

# Main function to analyze colors and answer questions
def analyze_colors(html_data):
    colors = extract_colors(html_data)

    # Question 1
    mean_color = calculate_mean_color(colors)
    print("Mean Color:", mean_color)

    # Question 2
    mode_color = calculate_mode_color(colors)
    print("Most Frequent Color:", mode_color)

    # Question 3
    median_color = calculate_median_color(colors)
    print("Median Color:", median_color)

    # BONUS: Question 4 - Variance of colors
    variance = len(colors) - len(set(colors))
    print("Variance of Colors:", variance)

    # BONUS: Question 5 - Probability of red color
    red_count = colors.count('RED')
    total_colors = len(colors)
    probability_red = red_count / total_colors
    print("Probability of Red Color:", probability_red)

    # Question 7
    

    def generate_random_binary():
        # Generate a random 4-digit binary number using 0s and 1s
        binary_digits = [random.choice(['0', '1']) for _ in range(4)]
        binary_number = ''.join(binary_digits)
        return binary_number

    def binary_to_decimal(binary_number):
        # Convert the binary number to base 10 (decimal)
        decimal_number = int(binary_number, 2)
        return decimal_number

    def main():
        # Generate a random 4-digit binary number
        binary_number = generate_random_binary()
        print("Random 4-digit Binary Number:", binary_number)

        # Convert binary number to base 10 (decimal)
        decimal_number = binary_to_decimal(binary_number)
        print("Decimal Equivalent:", decimal_number)

    if __name__ == "__main__":
        main()


    # Question 8
    def fibonacci(n):
    # Function to calculate the nth Fibonacci number
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def sum_first_50_fibonacci():
        # Calculate the sum of the first 50 Fibonacci numbers
        fib_sum = 0
        for i in range(1, 51):
            fib_sum += fibonacci(i)
        return fib_sum

    def main():
        # Calculate the sum of the first 50 Fibonacci numbers
        fib_sum = sum_first_50_fibonacci()
        print("Sum of the first 50 Fibonacci numbers:", fib_sum)

    if __name__ == "__main__":
        main()

# Call the main function
analyze_colors(html_data)

