'''
Test for TDD
@author: Zoe Bingham
'''
import sample_questions

def test_did_i_pass_70():
    # setup
    expected = True
    score = 70

    # invoke
    result = sample_questions.did_i_pass(score)

    # analyze
    assert expected == result

def test_did_i_pass_69():
    # setup
    expected = False
    score = 69

    # invoke
    result = sample_questions.did_i_pass(score)

    # analyze
    assert expected == result

def test_did_i_pass_71():
    # setup
    expected = True
    score = 71

    # invoke
    result = sample_questions.did_i_pass(score)

    # analyze
    assert expected == result