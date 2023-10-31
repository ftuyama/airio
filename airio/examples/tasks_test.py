# Copyright 2023 The AirIO Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tasks tests."""

import os

from absl.testing import absltest
from airio import feature_converters
from airio import tokenizer
from airio.examples import tasks
from seqio import vocabularies
import tensorflow_datasets as tfds

_SOURCE_NUM_EXAMPLES = 3
_SOURCE_SEQUENCE_LENGTH = 32


class TasksTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.test_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "test_data",
    )
    sentencepiece_vocab = vocabularies.SentencePieceVocabulary(
        os.path.join(self.test_dir, "sentencepiece", "sentencepiece.model")
    )
    self.tokenizer_configs = {
        "inputs": tokenizer.TokenizerConfig(vocab=sentencepiece_vocab),
        "targets": tokenizer.TokenizerConfig(vocab=sentencepiece_vocab),
    }

  def test_wmt_task(self):
    with tfds.testing.mock_data(_SOURCE_NUM_EXAMPLES):
      wmt_task = tasks.get_wmt_19_ende_v003_task(
          tokenizer_configs=self.tokenizer_configs
      )
    sequence_lengths = {
        "inputs": _SOURCE_SEQUENCE_LENGTH,
        "targets": _SOURCE_SEQUENCE_LENGTH,
    }
    ds = wmt_task.get_dataset(
        sequence_lengths,
        "train",
        shuffle=False,
        feature_converter=feature_converters.PyGrainEncDecFeatureConverter(),
        batch_size=2,
    )
    expected_first_batch = {
        "decoder_input_tokens": [
            [
                3,
                2,
                4,
                2,
                13,
                3,
                5,
                20,
                2,
                4,
                2,
                20,
                2,
                4,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                3,
                4,
                20,
                2,
                3,
                5,
                8,
                2,
                13,
                8,
                21,
                13,
                8,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ],
        "decoder_loss_weights": [
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ],
        "decoder_target_tokens": [
            [
                3,
                2,
                4,
                2,
                13,
                3,
                5,
                20,
                2,
                4,
                2,
                20,
                2,
                4,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                3,
                4,
                20,
                2,
                3,
                5,
                8,
                2,
                13,
                8,
                21,
                13,
                8,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ],
        "encoder_input_tokens": [
            [
                3,
                24,
                23,
                5,
                22,
                6,
                9,
                5,
                16,
                3,
                2,
                22,
                2,
                9,
                8,
                6,
                20,
                3,
                24,
                7,
                3,
                2,
                4,
                23,
                14,
                5,
                22,
                12,
                3,
                13,
                20,
                2,
            ],
            [
                3,
                24,
                23,
                5,
                22,
                6,
                9,
                5,
                16,
                3,
                2,
                22,
                2,
                9,
                8,
                6,
                20,
                3,
                24,
                7,
                3,
                2,
                4,
                23,
                14,
                5,
                22,
                12,
                3,
                2,
                3,
                8,
            ],
        ],
    }
    actual_first_batch = {k: v.tolist() for k, v in next(ds).items()}
    self.assertDictEqual(actual_first_batch, expected_first_batch)

  def test_nqo_task(self):
    with tfds.testing.mock_data(_SOURCE_NUM_EXAMPLES):
      nqo_task = tasks.get_nqo_v001_task(
          tokenizer_configs=self.tokenizer_configs
      )
    sequence_lengths = {
        "inputs": _SOURCE_SEQUENCE_LENGTH,
        "targets": _SOURCE_SEQUENCE_LENGTH,
    }
    ds = nqo_task.get_dataset(
        sequence_lengths,
        "train",
        shuffle=False,
        feature_converter=feature_converters.PyGrainEncDecFeatureConverter(),
        batch_size=2,
    )
    expected_first_batch = {
        "decoder_input_tokens": [
            [
                3,
                4,
                2,
                13,
                3,
                5,
                20,
                2,
                4,
                2,
                20,
                2,
                4,
                2,
                3,
                2,
                13,
                20,
                2,
                3,
                21,
                8,
                2,
                3,
                20,
                20,
                8,
                5,
                3,
                8,
                2,
                3,
            ],
            [
                3,
                20,
                2,
                3,
                5,
                8,
                2,
                13,
                8,
                21,
                13,
                8,
                2,
                21,
                2,
                3,
                8,
                20,
                8,
                4,
                20,
                13,
                21,
                20,
                5,
                13,
                5,
                21,
                2,
                3,
                21,
                21,
            ],
        ],
        "decoder_loss_weights": [
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
        ],
        "decoder_target_tokens": [
            [
                3,
                4,
                2,
                13,
                3,
                5,
                20,
                2,
                4,
                2,
                20,
                2,
                4,
                2,
                3,
                2,
                13,
                20,
                2,
                3,
                21,
                8,
                2,
                3,
                20,
                20,
                8,
                5,
                3,
                8,
                2,
                3,
            ],
            [
                3,
                20,
                2,
                3,
                5,
                8,
                2,
                13,
                8,
                21,
                13,
                8,
                2,
                21,
                2,
                3,
                8,
                20,
                8,
                4,
                20,
                13,
                21,
                20,
                5,
                13,
                5,
                21,
                2,
                3,
                21,
                21,
            ],
        ],
        "encoder_input_tokens": [
            [
                3,
                22,
                2,
                3,
                2,
                4,
                6,
                24,
                8,
                7,
                22,
                12,
                3,
                2,
                21,
                2,
                20,
                2,
                13,
                3,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            [
                3,
                22,
                2,
                3,
                2,
                4,
                6,
                24,
                8,
                7,
                22,
                12,
                3,
                4,
                8,
                2,
                3,
                2,
                13,
                2,
                4,
                2,
                5,
                3,
                2,
                20,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ],
    }
    actual_first_batch = {k: v.tolist() for k, v in next(ds).items()}
    self.assertDictEqual(actual_first_batch, expected_first_batch)


if __name__ == "__main__":
  absltest.main()
