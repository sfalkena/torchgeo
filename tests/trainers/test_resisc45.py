# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

import pytest
from _pytest.fixtures import SubRequest

from torchgeo.trainers import RESISC45DataModule


@pytest.fixture(scope="module", params=[True, False])
def datamodule(request: SubRequest) -> RESISC45DataModule:
    root = os.path.join("tests", "data", "resisc45")
    batch_size = 2
    num_workers = 0
    unsupervised_mode = request.param
    dm = RESISC45DataModule(
        root,
        batch_size,
        num_workers,
        val_split_pct=0.33,
        test_split_pct=0.33,
        unsupervised_mode=unsupervised_mode,
    )
    dm.prepare_data()
    dm.setup()
    return dm


class TestRESISC45DataModule:
    def test_train_dataloader(self, datamodule: RESISC45DataModule) -> None:
        next(iter(datamodule.train_dataloader()))

    def test_val_dataloader(self, datamodule: RESISC45DataModule) -> None:
        next(iter(datamodule.val_dataloader()))

    def test_test_dataloader(self, datamodule: RESISC45DataModule) -> None:
        next(iter(datamodule.test_dataloader()))
