from algo.read_csv import read_2_col_odd_rows


def test_read_csv():
    test_file = "test.csv"
    with open(test_file,  "w") as output:
        output.writelines(['"First","Second","Third"\n', '1,2,3\n', '3,4,5\n'])

    lines = read_2_col_odd_rows(test_file)
    assert lines == ['2']
    import shutil
    shutil.os.unlink(test_file)
