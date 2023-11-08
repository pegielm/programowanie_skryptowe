import skrypt1
def test_display(capsys):
    args = ["a","b","c"]
    skrypt1.display(args,False)
    #capture from stdout
    captured = capsys.readouterr()
    assert captured.out == "a\nb\nc\n"

def test_run(capsys):
    args = ["f","b","l","r","x","d"]
    skrypt1.run(args,skrypt1.move_descriptions)
    captured = capsys.readouterr()
    assert captured.out == "Zwierzak idzie do przodu\nZwierzak idzie do tyłu\nZwierzak skręca w lewo\nZwierzak skręca w prawo\n"

# pytest .\test_skrypt1_pytest.py

