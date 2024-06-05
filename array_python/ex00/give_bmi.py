def give_bmi(
            height: list[int | float],
            weight: list[int | float]) -> list[int | float]:
    """
    Return a list of BMI values calculated from the given height and weight.
    The formula to calculate BMI is weight / height^2.
    Control the input values as follows:
    - Length of height and weight should be same.
    - Height and weight should be greater than 0.
    - Height and weight should be of type int or float.
    """
    try:
        assert len(height) == len(weight), \
            "Error: Length of height and weight should be same"
    except AssertionError as e:
        print(e)
        exit(1)
    for i in range(len(height)):
        try:
            assert isinstance(height[i], (int, float)) \
                and isinstance(weight[i], (int, float)), \
                "Error: Height and weight should be of type int or float"
            assert height[i] > 0 and weight[i] > 0, \
                "Error: Height and weight should be greater than 0"
        except AssertionError as e:
            print(e)
            exit(1)
    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / height[i] ** 2)
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of boolean values, where True
    indicates that the BMI is greater than the limit.
    """
    result = []
    for i in range(len(bmi)):
        result.append(bmi[i] > limit)
    return result
