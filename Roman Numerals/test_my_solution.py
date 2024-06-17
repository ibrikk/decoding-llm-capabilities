import pytest
import roman_chat_gpt4
import roman_chat_gpt3
import roman_claude3_opus
import roman_claude3_sonnet
import roman_claude3_haiku
import roman_claude_free
import roman_github_copilot
import roman_gemini
import roman_chat_gpt4o

modules_to_test = [roman_chat_gpt4, roman_chat_gpt3, roman_claude3_opus, roman_claude3_sonnet, roman_claude3_haiku, roman_claude_free, roman_github_copilot, roman_gemini, roman_chat_gpt4o]

@pytest.mark.parametrize("module", modules_to_test)
def test_XVIII(module):
    assert module.valid_numeral("XVIII") == True, "XVIII should be True"

@pytest.mark.parametrize("module", modules_to_test)
def test_MCXIV(module):
    assert module.valid_numeral("MCXIV") == True, "MCXIV should be True"

@pytest.mark.parametrize("module", modules_to_test)
def test_CCCC(module):
    assert module.valid_numeral("CCCC") == False, "CCCC should be False (4 straight identical symbols)"

@pytest.mark.parametrize("module", modules_to_test)
def test_CIL(module):
    assert module.valid_numeral("CIL") == False, "CIL should be False (I can't precede L)"

@pytest.mark.parametrize("module", modules_to_test)
def test_I(module):
    assert module.valid_numeral("I") == True, "I should be True"

@pytest.mark.parametrize("module", modules_to_test)
def test_III(module):
    assert module.valid_numeral("III") == True, "III should be True"

@pytest.mark.parametrize("module", modules_to_test)
def test_LLL(module):
    assert module.valid_numeral("LLL") == False, "LLL should be False (three straight 5*10^n symbols)"

@pytest.mark.parametrize("module", modules_to_test)
def test_empty(module):
    assert module.valid_numeral("") == False, "Empty string should be False (no empty string permitted)"

@pytest.mark.parametrize("module", modules_to_test)
def test_3999(module):
    assert module.valid_numeral("MMMCMXCIX") == True, "MMMCMXCIX should be True"

@pytest.mark.parametrize("module", modules_to_test)
def test_MDCLXVI(module):
    assert module.valid_numeral("MDCLXVI") == True, "MDCLXVI should be True"

@pytest.mark.parametrize("module", modules_to_test)
def test_mdclxvi(module):
    assert module.valid_numeral("mdclxvi") == False, "mdclxvi should be False (capital letters needed)"

@pytest.mark.parametrize("module", modules_to_test)
def test_X1II(module):
    assert module.valid_numeral("X1II") == False, "X1II should be False (no numbers permitted)"

@pytest.mark.parametrize("module", modules_to_test)
def test_XiV(module):
    assert module.valid_numeral("XiV") == False, "XiV should be False (all caps needed)"

@pytest.mark.parametrize("module", modules_to_test)
def test_XD(module):
    assert module.valid_numeral("XD") == False, "XD should be False (X can't precede D)"

@pytest.mark.parametrize("module", modules_to_test)
def test_VX(module):
    assert module.valid_numeral("VX") == False, "VX should be False (V can't precede X)"
