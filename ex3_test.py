from ex3 import digital_root
import pytest

def test_digital_root():
  assert digital_root(16) == 7
  assert digital_root(942) == 6
  assert digital_root(132189) == 6
  assert digital_root(493193) == 2
  assert digital_root(5) == 5
  assert digital_root(0) == 0
  try:
      digital_root(-123)
      assert False  
  except ValueError as e:
      assert str(e) == "O número deve ser não negativo"