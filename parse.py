""" Runs parser for all logs in ScraperLogs folder """
# --- BUILT IN IMPORT ---
import os
from typing import List

# --- PROJECT IMPORT ---
from DasdecParser import DasdecLogParser


def get_filenames(log_path) -> List[str]:
    """ Gathers file names from directory """
    return os.listdir(log_path)


def read_from_file(filename) -> str:
    """ Given filename load data """
    with open(filename, 'r') as f:
        content = f.read()
    return content


def parse_dasdec_logs():
    eas_log_dir = os.path.join(os.getcwd(), 'ScrapedLogs')
    files = get_filenames(eas_log_dir)
    for file in files:
        print(file + "\n")
        filepath = os.path.join(eas_log_dir, file)
        content = read_from_file(filepath)
        all_tests = DasdecLogParser(content).parse_content()
        print(f"Originated Tests: {len(all_tests.originated_tests)}")
##        [print(test, "\n") for test in all_tests.originated_tests]
        print(f"Forwarded Tests: {len(all_tests.forwarded_tests)}")
##        [print(test, "\n") for test in all_tests.forwarded_tests]
        print(f"Decoded Tests: {len(all_tests.decoded_tests)}")
##        [print(test, "\n") for test in all_tests.decoded_tests]
        print(f"EAS NET Decoded: {len(all_tests.eas_net_decoded_tests)}")
##        [print(test, "\n") for test in all_tests.eas_net_decoded_tests]
        print(f"CAP EAS Decoded: {len(all_tests.cap_eas_decoded_tests)}")
##        [print(test, "\n") for test in all_tests.cap_eas_decoded_tests]
    print('Content parsed')


if __name__ == "__main__":
    parse_dasdec_logs()
