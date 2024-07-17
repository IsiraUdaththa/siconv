import multiprocessing
from tqdm import tqdm
from siconv import sinhala_to_singlish


# Function to read data from file
def read_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                sinhala_word, singlish_word = line.strip().split(',')
                data.append((sinhala_word.strip(), singlish_word.strip()))
    return data


# Test function for Sinhala to Singlish conversion
def test_sinhala_to_singlish_single(word_pair):
    sinhala_word, expected_singlish = word_pair
    converted_singlish = sinhala_to_singlish(sinhala_word)
    if converted_singlish == expected_singlish:
        return True
    else:
        # print(
        #     f"FAIL: Sinhala to Singlish conversion failed for '{sinhala_word}'. Expected '{expected_singlish}', but got '{converted_singlish}'")
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

    # Multiprocessing Sinhala to Singlish conversion tests
    sinhala_to_singlish_pass, sinhala_to_singlish_fail = run_tests(test_sinhala_to_singlish_single, data)

    print("\n--- Test Results ---")
    print(f"Passed   : {sinhala_to_singlish_pass}")
    print(f"Failed   : {sinhala_to_singlish_fail}")
    print(f"Accuracy : {round(sinhala_to_singlish_pass / len(data),3)}")

