"""
unit test for measure module
"""

import molecool
import numpy as np
import pytest

def test_calculate_angle():
    """Test the calculate_angle function to get proper results"""

    rA = np.array([0,0,-1])
    rB = np.array([0,0,0])
    rC = np.array([1,0,0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(rA,rB,rC, degrees=True)

    assert calculated_angle == expected_angle

#@pytest.mark.parametrize("variable_name1, variable_name2, ...., variable_nameN, expected_answer", [
#    (variable_value1, variable_value2, ...., variable_valueN, expected_answer1),
#    (variable_value1, variable_value2, ...., variable_valueN, expected_answer1)
#])

#def test_calculate_angle_many():

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]),np.array([0,0,0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60)
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):

    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)

    assert expected_angle == pytest.approx(calculated_angle)
