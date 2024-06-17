import pytest
import rational_chat_gpt4
import rational_chat_gpt3
import rational_claude3_opus
import rational_claude3_sonnet
import rational_claude3_haiku
import rational_claude_free
import rational_github_copilot
import rational_gemini
import rational_chat_gpt4o

modules_to_test = [
    rational_chat_gpt4,
    rational_chat_gpt3,
    rational_claude3_opus,
    rational_claude3_sonnet,
    rational_claude3_haiku,
    rational_claude_free,
    rational_github_copilot,
    rational_gemini,
    rational_chat_gpt4o
]
@pytest.fixture
def create_rational():
    def _create_rational(module, numerator, denominator):
        return module.Rational(numerator, denominator)
    return _create_rational

    # Test for getting the numerator
@pytest.mark.parametrize("module", modules_to_test)
def test_getNumerator_one(module, create_rational):
    r = create_rational(module, 1, 4)
    assert r.getNumerator() == 1, "getNumerator() tested on 1/4 should return 1"

# Test for getting the numerator
@pytest.mark.parametrize("module", modules_to_test)
def test_getNumerator_one(module, create_rational):
    r = create_rational(module, 1, 4)
    assert r.getNumerator() == 1, "getNumerator() tested on 1/4 should return 1"

@pytest.mark.parametrize("module", modules_to_test)
def test_getNumerator_two(module, create_rational):
    r = create_rational(module, 2, 16)
    assert r.getNumerator() == 1, "getNumerator() tested on 2/16 should return 1"

@pytest.mark.parametrize("module", modules_to_test)
def test_getNumerator_three(module, create_rational):
    r = create_rational(module, -2, 16)
    assert r.getNumerator() == -1, "getNumerator() tested on -2/16 should return -1"

@pytest.mark.parametrize("module", modules_to_test)
def test_getNumerator_four(module, create_rational):
    r = create_rational(module, 2, -16)
    assert r.getNumerator() == 1, "getNumerator() tested on 2/-16 should return 1"

# Test for getting the denominator
@pytest.mark.parametrize("module", modules_to_test)
def test_getDenominator_one(module, create_rational):
    r = create_rational(module, 1, 4)
    assert r.getDenominator() == 4, "getDenominator() tested on 1/4 should return 4"

@pytest.mark.parametrize("module", modules_to_test)
def test_getDenominator_two(module, create_rational):
    r = create_rational(module, 2, 16)
    assert r.getDenominator() == 8, "getDenominator() tested on 2/16 should return 8" 

@pytest.mark.parametrize("module", modules_to_test)
def test_getDenominator_three(module, create_rational):
    r = create_rational(module, -2, 16)
    assert r.getDenominator() == 8, "getDenominator() tested on -2/16 should return 8"  

@pytest.mark.parametrize("module", modules_to_test)
def test_getDenominator_four(module, create_rational):
    r = create_rational(module, 2, -16)
    assert r.getDenominator() == -8, "getDenominator() tested on 2/-16 should return -8"  


# Test for setting the numerator
@pytest.mark.parametrize("module", modules_to_test)
def test_setNumerator_one(module, create_rational):
    r = create_rational(module, 1, 4)
    r.setNumerator(3)
    assert r.getNumerator() == 3, "setNumerator(3) tested on 1/4 should set the numerator to 3"

@pytest.mark.parametrize("module", modules_to_test)
def test_setNumerator_two(module, create_rational):
    r = create_rational(module, 1, 4)
    r.setNumerator(2)
    assert r.getNumerator() == 1, "setNumerator(2) tested on 1/4 should set the numerator to 1"

@pytest.mark.parametrize("module", modules_to_test)
def test_setNumerator_three(module, create_rational):
    r = create_rational(module, 1, 4)
    r.setNumerator(-2)
    assert r.getNumerator() == -1, "setNumerator(-2) tested on 1/4 should set the numerator to -1"


# Test for setting the denominator
@pytest.mark.parametrize("module", modules_to_test)
def test_setDenominator_one(module, create_rational):
    r = create_rational(module, 1, 4)
    r.setDenominator(3)
    assert r.getDenominator() == 3, "setDenominator(3) tested on 1/4 should set the denominator to 3"

@pytest.mark.parametrize("module", modules_to_test)
def test_setDenominator_two(module, create_rational):
    r = create_rational(module, 2, 7)
    r.setDenominator(4)
    assert r.getDenominator() == 2, "setDenominator(4) tested on 2/7 should set the denominator to 2"

@pytest.mark.parametrize("module", modules_to_test)
def test_setDenominator_three(module, create_rational):
    r = create_rational(module, 2, 7)
    r.setDenominator(-4)
    assert r.getDenominator() == -2, "setDenominator(-4) tested on 2/7 should set the denominator to -2"    

# Test for validating Rational object
@pytest.mark.parametrize("module, numerator, denominator, expected, description", 
    [(module, 1, 4, True,  "1/4 should be a valid Rational") for module in modules_to_test] + 
    [(module, 1, -4, True, "1/-4 should be a valid Rational") for module in modules_to_test] + 
    [(module, 1, 0, False, "1/0 should NOT be a valid Rational") for module in modules_to_test] + 
    [(module, 1, -0, False, "1/-0 should NOT be a valid Rational") for module in modules_to_test]
)
def test_isValid(module, create_rational, numerator, denominator, expected, description):
    r = create_rational(module, numerator, denominator)
    assert r.isValid() == expected, description

# Test for reciprocal of a Rational object
@pytest.mark.parametrize("module", modules_to_test)
def test_reciprocal_4_7(module, create_rational):
    r = create_rational(module, 4, 7)
    r.reciprocal()
    assert (r.getNumerator(), r.getDenominator(), "Reciprocal of 4/7 should be 7/4") == (7, 4)

@pytest.mark.parametrize("module", modules_to_test)
def test_reciprocal_7_4(module, create_rational):
    r = create_rational(module, 4, 7)
    r.reciprocal()
    assert (r.getNumerator(), r.getDenominator(), "Reciprocal of 7/4 should be 4/7") == (7, 4)

# Test for adding two Rational objects
@pytest.mark.parametrize("module", modules_to_test)
def test_add_one(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, 1, 4)
    r1.add(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 + 1/4 = 1/2") == (1, 2)

@pytest.mark.parametrize("module", modules_to_test)
def test_add_two(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, -1, 8)
    r1.add(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 + -1/8 = 1/8") == (1, 8)

@pytest.mark.parametrize("module", modules_to_test)
def test_add_three(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, 1, 8)
    r1.add(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 + 1/8 = 3/8") == (3, 8)

@pytest.mark.parametrize("module", modules_to_test)
def test_add_four(module, create_rational):
    r1 = create_rational(module, 1, 10)
    r2 = create_rational(module, 2, 10)
    r1.add(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/10 + 2/10 = 3/10") == (3, 10)

@pytest.mark.parametrize("module", modules_to_test)
def test_add_five(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, 1, -8)
    r1.add(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 + 1/-8 = 3/8") == (1, 8)

@pytest.mark.parametrize("module", modules_to_test)
def test_add_six(module, create_rational):
    r1 = create_rational(module, 1, 2)
    r2 = create_rational(module, 1, -8)
    r1.add(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/2 + 1/-8 = 3/8") == (3, 8)

# Test for subtracting two Rational objects
@pytest.mark.parametrize("module", modules_to_test)
def test_sub_one(module, create_rational):
    r1 = create_rational(module, 3, 2)
    r2 = create_rational(module, 1, 4)
    r1.sub(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "3/2 - 1/4 = 5/4") == (5, 4)

@pytest.mark.parametrize("module", modules_to_test)
def test_sub_two(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, -1, 8)
    r1.sub(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 - -1/8 = 3/8") == (3, 8)

@pytest.mark.parametrize("module", modules_to_test)
def test_sub_three(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, 1, 8)
    r1.sub(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 - 1/8 = 1/8") == (1, 8)

@pytest.mark.parametrize("module", modules_to_test)
def test_sub_four(module, create_rational):
    r1 = create_rational(module, 1, 10)
    r2 = create_rational(module, 2, 10)
    r1.sub(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/10 - 2/10 = -1/10") == (-1, 10)

@pytest.mark.parametrize("module", modules_to_test)
def test_sub_five(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, 1,-8)
    r1.sub(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 - 1/-8 = 3/8") == (3, 8)

@pytest.mark.parametrize("module", modules_to_test)
def test_sub_six(module, create_rational):
    r1 = create_rational(module, 1, 2)
    r2 = create_rational(module, 1, -8)
    r1.sub(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/2 - 1/-8 = 5/8") == (5, 8)

# Test for multiplying two Rational objects
@pytest.mark.parametrize("module", modules_to_test)
def test_mult_one(module, create_rational):
    r1 = create_rational(module, 3, 2)
    r2 = create_rational(module, 1, 4)
    r1.mult(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "3/2 * 1/4 = 3/8") == (3, 8)

@pytest.mark.parametrize("module", modules_to_test)
def test_mult_two(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, -1, 8)
    r1.mult(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 * -1/8 = -1/32") == (-1, 32)

@pytest.mark.parametrize("module", modules_to_test)
def test_mult_three(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, 1, 8)
    r1.mult(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 * 1/8 = 1/32") == (1, 32)

@pytest.mark.parametrize("module", modules_to_test)
def test_mult_four(module, create_rational):
    r1 = create_rational(module, 1, 10)
    r2 = create_rational(module, 2, 10)
    r1.mult(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/10 * 2/10 = 1/50") == (1, 50)

@pytest.mark.parametrize("module", modules_to_test)
def test_mult_five(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, 1, -8)
    r1.mult(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 * 1/-8 = 1/-32") == (1, -32)

@pytest.mark.parametrize("module", modules_to_test)
def test_mult_six(module, create_rational):
    r1 = create_rational(module, 1, 2)
    r2 = create_rational(module, 1, -8)
    r1.mult(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/2 * 1/-8 = 1/-16") == (1, -16)

# Test for dividing two Rational objects
@pytest.mark.parametrize("module", modules_to_test)
def test_div_one(module, create_rational):
    r1 = create_rational(module, 3, 2)
    r2 = create_rational(module, 1, 4)
    r1.div(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "3/2 / 1/4 = 6/1") == (6, 1)

@pytest.mark.parametrize("module", modules_to_test)
def test_div_two(module, create_rational):
    r1 = create_rational(module, 1, 4)
    r2 = create_rational(module, 1, 8)
    r1.div(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "1/4 / 1/8 = 2/1") == (2, 1)

@pytest.mark.parametrize("module", modules_to_test)
def test_div_three(module, create_rational):
    r1 = create_rational(module, 3, 7)
    r2 = create_rational(module, 1, 3)
    r1.div(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "3/7 / 1/3 = 9/7") == (9, 7)

@pytest.mark.parametrize("module", modules_to_test)
def test_div_four(module, create_rational):
    r1 = create_rational(module, 7, 3)
    r2 = create_rational(module, 1, 3)
    r1.div(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "7/3 / 1/3 = 7/1") == (7, 1)

@pytest.mark.parametrize("module", modules_to_test)
def test_div_five(module, create_rational):
    r1 = create_rational(module, 7, 3)
    r2 = create_rational(module, 1, 5)
    r1.div(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "7/3 / 1/5 = 35/3") == (35, 3)

@pytest.mark.parametrize("module", modules_to_test)
def test_div_six(module, create_rational):
    r1 = create_rational(module, 7, 5)
    r2 = create_rational(module, 1, 3)
    r1.div(r2)
    assert (r1.getNumerator(), r1.getDenominator(), "7/5 / 1/3 = 21/5") == (21, 5)


if __name__ == '__main__':
    pytest.main()
