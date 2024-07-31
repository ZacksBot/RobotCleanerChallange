# Testing

[![Pytest](https://github.com/ZacksBot/Robot-Cleaner/actions/workflows/AppTest.yml/badge.svg)](https://github.com/ZacksBot/Robot-Cleaner/actions/workflows/AppTest.yml)

# Robot Cleaning

This Python script simulates the movements of an automatic cleaning robot. The robot receives a set of movement commands which can be found in the .txt files in the tests folder. The script then calculates the number of unique places the robot has cleaned.

## How to Use Without Docker

1. **Clone the Repository**

```
 git clone https://github.com/ZacksBot/Robot-Cleaner.git
 cd robot-cleaner
```

2. **Create and Activate a Virtual Environmenty**

```
python3 -m venv myenv
source myenv/bin/activate
```

3. **Install Dependencies**

```
pip install -r requirements.txt
```

4. **Run the Script**

```
python cleaner_robot.py <input_file>
Replace <input_file> with the path to your input file.
```

## How to Use With Docker

1. **Build the image**

```
docker build -t robot-cleaner .
```

2. **Run the image**

```
docker run --rm robot-cleaner
```

## Thought Process

### Initial Approach

When I started working on this task, my initial thought was to break down the problem into smaller, manageable parts. I focused on understanding the input format and how the robot's movements translate actions.

### Handling Large Data

I noticed that when I run files containing over 10000 lines of code, my computer crashes frequently. It was unable to handle that much data. At first, I thought it might be due to my PC's limitations. However, even when I tried running the files on a more powerful PC, the issue persisted. I assumed it might be due to memory overload or a similar problem causing the application to crash.
To solve the issue, I implemented a technique that I like to call "Divide and Conquer." I divided the code into chunks of 1000 lines, processed each chunk, cleaned the set, and then proceeded to the next 1000 lines. This approach prevented my PC from experiencing memory leaks and ensured that the application did not crash.

### Final Adjustments

In the final stages, I added logging and error handling to make the script more robust and user-friendly. I made sure that all the test cases given to me worked; however, I encountered different results for two test cases. It's possible that I might have made a mistake or overlooked a crucial typo error in the .txt file.
