import multiprocessing
from tqdm import tqdm
from siconv import singlish_to_sinhala


# Function to read data from file
def read_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                sinhala_word, singlish_word = line.strip().split(',')
                data.append((sinhala_word.strip(), singlish_word.strip()))
    return data


# Test function for Singlish to Sinhala conversion
def test_singlish_to_sinhala_single(word_pair):
    sinhala_word, expected_singlish = word_pair
    converted_sinhala = singlish_to_sinhala(expected_singlish)
    if converted_sinhala == sinhala_word:
        return True
    else:
        # print(
        #     f"FAIL: Singlish to Sinhala conversion failed for '{expected_singlish}'. Expected '{sinhala_word}', but got '{converted_sinhala}'")
        return False


# Multiprocessing test function
def run_tests(test_func, data):
    with multiprocessing.Pool() as pool:
        results = list(tqdm(pool.imap(test_func, data), total=len(data)))
    pass_count = sum(results)
    fail_count = len(data) - pass_count
    return pass_count, fail_count


# Run the tests
if __name__ == "__main__":
    data = read_data('test_data.txt')


    # Multiprocessing Singlish to Sinhala conversion tests
    singlish_to_sinhala_pass, singlish_to_sinhala_fail = run_tests(test_singlish_to_sinhala_single, data)

    print("\n--- Test Results ---")
    print(f"Singlish to Sinhala: Passed {singlish_to_sinhala_pass}, Failed {singlish_to_sinhala_fail}, Accuracy {round(singlish_to_sinhala_pass/len(data),3)}%")


