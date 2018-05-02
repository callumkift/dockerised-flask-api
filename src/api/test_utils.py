from .utils import _read_config, _get_pickle_file_path, _get_pipeline_key
import copy
import pytest

config = {
    "model": {
        "directory": "test_resources/pickles",
        "pickled_object": "pickled_object.pk",
        "pipeline_key": "pipeline"
    }
}

config_path = "test_resources/test_config.yaml"
fake_config_path = "test_resources/non_existent.yaml"


class TestReadConfig:

    def test_read_config(self):
        actual = _read_config(config_path)
        expected = config
        assert expected == actual

    def test_read_config_path_does_not_exist(self):
        with pytest.raises(FileNotFoundError):
            _read_config(fake_config_path)


class TestGetPickleFilePath:
    config_one = config

    # duplicating config_one but adding a '/' to the end of the directory path
    config_two = copy.deepcopy(config_one)
    config_two["model"]["directory"] += "/"

    @pytest.mark.parametrize("cfg", [config_one, config_two])
    def test_get_pickle_file_path(self, cfg):
        actual = _get_pickle_file_path(cfg)
        expected = "test_resources/pickles/pickled_object.pk"
        assert expected == actual

    def test_get_pickle_file_path_when_config_wrong(self):
        with pytest.raises(Exception):
            _get_pickle_file_path({})


class TestGetPipelineKey:
    def test_get_pipeline_key(self):
        actual = _get_pipeline_key(config_path)
        expected = "pipeline"
        assert expected == actual

    def test_get_pipeline_key_when_config_wrong(self):
        with pytest.raises(Exception):
            _get_pipeline_key({})


class TestLoadPickle:
    pass


class TestGetPickledObject:
    pass


class TestGetPipeline:
    pass
