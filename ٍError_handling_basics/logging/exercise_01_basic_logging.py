import logging

logging.basicConfig(
    filename="bim_run.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

logging.info("Batch check started")

file_name = "Tower_B.rvt"
logging.info("Checking file: %s", file_name)

missing_fire_rating = 5

if missing_fire_rating > 0:
    logging.warning("Model has %d elements without Fire Rating", missing_fire_rating)

try:
    number = int("abc")
except ValueError:
    logging.exception("Invalid number conversion during BIM check")

logging.info("Batch check finished")
