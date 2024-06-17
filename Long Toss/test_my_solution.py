import pytest
import long_toss_chat_gpt4
import long_toss_chat_gpt3
import long_toss_claude3_opus
import long_toss_claude3_sonnet
import long_toss_claude3_haiku
import long_toss_claude_free
import long_toss_github_copilot
import long_toss_gemini
import long_toss_chat_gpt4o

modules_to_test = [
    long_toss_chat_gpt4,
    long_toss_chat_gpt3,
    long_toss_claude3_opus,
    long_toss_claude3_sonnet,
    long_toss_claude3_haiku,
    long_toss_claude_free,
    long_toss_github_copilot,
    long_toss_gemini,
    long_toss_chat_gpt4o,
]

@pytest.mark.parametrize("module, values, expected, msg", [
    (module, (5, 10, 2), False, "The throw was not far enough.") for module in modules_to_test] +
    [(module, (7, 10, 2), True, "The throw made it across the line.") for module in modules_to_test] +
    [(module, (5, 8, 2), True, "The throw made it across the line.") for module in modules_to_test] +
    [(module, (5, 9, 2), True, "The throw just made it to the line.") for module in modules_to_test] +
    [(module, (6, 10, 2), True, "The throw made it across the line.") for module in modules_to_test] +
    [(module, (6, 12, 2), True, "The throw just made it to the line.") for module in modules_to_test] +
    [(module, (6, 14, 2), False, "The throw was not far enough.") for module in modules_to_test] +
    [(module, (2, 10, 2), False, "The throw was not far enough.") for module in modules_to_test] +
    [(module, (5, 1, 2), True, "The throw made it across the line.") for module in modules_to_test] +
    [(module, (5, 10, 3), False, "The throw was not far enough.") for module in modules_to_test]
)
def test_farEnough(module, values, expected, msg):
    testObj = module.LongToss(*values)
    assert testObj.farEnough() == expected, msg

@pytest.mark.parametrize("module, values, expected, msg", [
    (module, (5, 10, 2), 9, "The throw traveled 9 feet.") for module in modules_to_test] +
    [(module, (7, 10, 2), 16, "The throw traveled 16 feet.") for module in modules_to_test] +
    [(module, (5, 8, 2), 9, "The throw traveled 9 feet.") for module in modules_to_test] +
    [(module, (5, 9, 2), 9, "The throw traveled 9 feet.") for module in modules_to_test] +
    [(module, (6, 10, 2), 12, "The throw traveled 12 feet.") for module in modules_to_test] +
    [(module, (6, 12, 2), 12, "The throw traveled 12 feet.") for module in modules_to_test] +
    [(module, (6, 14, 2), 12, "The throw traveled 12 feet.") for module in modules_to_test] +
    [(module, (2, 10, 2), 2, "The throw traveled 2 feet.") for module in modules_to_test] +
    [(module, (5, 1, 2), 9, "The throw traveled 9 feet.") for module in modules_to_test] +
    [(module, (5, 10, 3), 7, "The throw traveled 7 feet.") for module in modules_to_test]
)
def test_totalDistance(module, values, expected, msg):
    testObj = module.LongToss(*values)
    assert testObj.totalDistance() == expected, msg


