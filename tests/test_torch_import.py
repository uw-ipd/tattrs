def test_torch_import():
    import torch
    assert torch.cuda.device_count() > 0
