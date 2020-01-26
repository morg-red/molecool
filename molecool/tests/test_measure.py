"""
Unit tests for measure module
"""

import molecool
import numpy as np
import pytest

def test_calculate_distance():
    """ Test the calculate_distance function to ensure it outputs expected """

    r1 = np.array([0,0,1])
    r2 = np.array([0,0,0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1,r2)

    assert calculated_distance == expected_distance

def test_calculate_distance_typeerror():

    r1 = [0,0,0]
    r2 = [1,0,0]

    with pytest.raises(TypeError):
        calculate_distance = molecool.calculate_distance(r1, r2)

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = molecool.atom_data.atomic_weights['C'] + molecool.atom_data.atomic_weights['H'] +\
         molecool.atom_data.atomic_weights['H'] + molecool.atom_data.atomic_weights['H'] + molecool.atom_data.atomic_weights['H']

    assert actual_mass == calculated_mass


def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])

    assert np.allclose(expected_center, center_of_mass)
