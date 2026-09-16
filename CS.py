import time
import sys

print("\n\n")

lyrics = [
    ("Wake up the dawn and ask her why", 0.00, 0.09),
    ("A dreamer dreams she never dies", 2.94, 0.09),
    ("Wipe that tear away now from your eye", 6.31, 0.09),
    ("Slowly walkin' down the hall", 13.12, 0.09),
    ("Faster than a cannonball", 15.91, 0.09),
    ("Where were you while we were gettin' high?", 19.01, 0.09),
]


def type_out(text, char_delay=0.09):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)

    sys.stdout.write("\n")
    sys.stdout.flush()


def play_lyrics(lyrics):
    start_time = time.time()

    for line, timestamp, char_delay in lyrics:

        # Wait until the exact timestamp
        while time.time() - start_time < timestamp:
            time.sleep(0.001)

        type_out(line, char_delay)


if __name__ == "__main__":
    play_lyrics(lyrics)