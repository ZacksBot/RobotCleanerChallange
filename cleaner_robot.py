import sys
import logging

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    if len(sys.argv) != 2:
        logging.error("Usage: python cleaner_robot.py <input_file>")
        return

    input_file = sys.argv[1]

    directions = {
        'E': (1, 0),
        'W': (-1, 0),
        'N': (0, 1),
        'S': (0, -1)
    }

    cleaned_places = set()

    try:
        with open(input_file, 'r') as file:
            n = int(file.readline().strip())
            x, y = map(int, file.readline().strip().split())

            logging.info(f"Starting position: ({x}, {y})")
            cleaned_places.add((x, y))

            last_position = (x, y)
            unique_cleaned = 1  # starting position

            for i in range(n):
                if i % 1000 == 0: # Log every 1000 commands, change it based on power of your pc
                    logging.info(f"Processing command {i+1}/{n}")

                line = file.readline().strip()
                if not line:
                    logging.warning(f"Missing command at line {i + 3}")
                    continue

                direction, steps = line.split()
                steps = int(steps)
                dx, dy = directions[direction]

                for _ in range(steps):
                    x += dx
                    y += dy
                    if (x, y) != last_position and (x, y) not in cleaned_places:
                        unique_cleaned += 1
                        cleaned_places.add((x, y))
                    last_position = (x, y)

                if len(cleaned_places) > 1000000:
                    cleaned_places = set()  # Clear the set periodically to save memory

            logging.info("Finished processing all commands.")
            print(f"=> Cleaned: {unique_cleaned}")

    except FileNotFoundError:
        logging.error(f"File not found: {input_file}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
