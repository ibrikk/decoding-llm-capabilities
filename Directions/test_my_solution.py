import pytest
import directions_chat_gpt4
import directions_chat_gpt3
import directions_claude3_opus
import directions_claude3_sonnet
import directions_claude3_haiku
import directions_claude_free
import directions_github_copilot
import directions_gemini
import directions_chat_gpt4o

modules_to_test = [
    directions_chat_gpt4,
    directions_chat_gpt3,
    directions_claude3_opus,
    directions_claude3_sonnet,
    directions_claude3_haiku,
    directions_claude_free,
    directions_github_copilot,
    directions_gemini,
    directions_chat_gpt4o,
]


@pytest.fixture
def directions():
    def _directions(module, data):
        return module.Directions(data)
    return _directions

# Now, include the module in the parametrization to test across different implementations
@pytest.mark.parametrize("module, data, expected, msg", 
    [(module, ['U1', 'D2', 'L3', 'R4'], 'R4', "The largest step from the sequence ['U1','D2','L3','R4'] is R4.") for module in modules_to_test] +
    [(module, ['U1', 'D2', 'L3'], 'L3', "The largest step from the sequence ['U1','D2','L3'] is L3.") for module in modules_to_test] +
    [(module, ['U1', 'D2'], 'D2', "The largest step from the sequence ['U1','D2'] is D2.") for module in modules_to_test] +
    [(module, ['U1'], 'U1', "The largest step from the sequence ['U1'] is U1.") for module in modules_to_test] +
    [(module, ['U11', 'D2'], 'U11', "The largest step from the sequence ['U11','D2'] is U11.") for module in modules_to_test] +
    [(module, ['U1', 'D0', 'L0', 'R0'], 'U1', "The largest step from the sequence ['U1','D0','L0','R0'] is U1.") for module in modules_to_test] +
    [(module, ['U1', 'D12', 'L3', 'R4'], 'D12', "The largest step from the sequence ['U1','D12','L3','R4'] is D12.") for module in modules_to_test] +
    [(module, ['U1', 'D2', 'L13', 'R4'], 'L13', "The largest step from the sequence ['U1','D2','L13','R4'] is L13.") for module in modules_to_test] +
    [(module, ['U11', 'D2', 'L3', 'R4'], 'U11', "The largest step from the sequence ['U11','D2','L3','R4'] is U11.") for module in modules_to_test] +
    [(module, ['U0', 'D0', 'L1', 'R0'], 'L1', "The largest step from the sequence ['U0','D0','L1','R0'] is L1.") for module in modules_to_test]
    )
def test_biggestStep(directions, module, data, expected, msg):
    testObj = directions(module, data)
    testObj.biggestStep()
    assert testObj.getBiggest() == expected, msg

# Similarly for finalPosition tests
@pytest.mark.parametrize("module, data, expected, msg", [
    (module, ['U1', 'D2', 'L3', 'R4'], (1, -1), "The final position after sequence ['U1','D2','L3','R4'] is (1,-1).") for module in modules_to_test] +
    [(module, ['U1', 'D2', 'L3'], (-3, -1), "The final position after sequence ['U1','D2','L3'] is (-3,-1).") for module in modules_to_test] +
    [(module, ['U1', 'D2'], (0, -1), "The final position after sequence ['U1','D2'] is (0,-1).") for module in modules_to_test] +
    [(module, ['U1'], (0, 1), "The final position after sequence ['U1'] is (0,1).") for module in modules_to_test] +
    [(module, ['U11', 'D2'], (0, 9), "The final position after sequence ['U11','D2'] is (0,9).") for module in modules_to_test] +
    [(module, ['U1', 'D0', 'L0', 'R0'], (0, 1), "The final position after sequence ['U1','D0','L0','R0'] is (0,1).") for module in modules_to_test] +
    [(module, ['U1', 'D12', 'L3', 'R4'], (1, -11), "The final position after sequence ['U1','D12','L3','R4'] is (1,-11).") for module in modules_to_test] +
    [(module, ['U1', 'D2', 'L13', 'R4'], (-9, -1), "The final position after sequence ['U1','D2','L13','R4'] is (-4,1).") for module in modules_to_test] +
    [(module, ['U11', 'D2', 'L3', 'R4'], (1, 9), "The final position after sequence ['U11','D2','L3','R4'] is (1,9).") for module in modules_to_test] +
    [(module, ['U0', 'D0', 'L1', 'R0'], (-1, 0), "The final position after sequence ['U0','D0','L1','R0'] is (-1,0).") for module in modules_to_test]
    )
def test_finalPosition(directions, module, data, expected, msg):
    testObj = directions(module, data)
    assert testObj.finalPosition() == expected, msg
