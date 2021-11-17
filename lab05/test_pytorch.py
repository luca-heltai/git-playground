import torch


def test_version():
    assert torch.__version__[0] >= '1'
