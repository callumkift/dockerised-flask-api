from typing import Any, Dict
import yaml
import pickle
import os

MODEL_KEY = "model"
MODEL_DIRECTORY = "directory"
MODEL_PICKLED_OBJECT = "pickled_object"
MODEL_PIPELINE_KEY = "pipeline_key"


def _read_config(config_path: str) -> Dict[str, Any]:
    """
    Reads the config yaml file, parses it, and returns a dict
    :param config_path: path to config yaml
    :return: dictionary of the config
    """
    with open(config_path, "r") as y:
        cfg = yaml.load(y)
    return cfg


def _get_pickle_file_path(cfg: Dict[str, Any]) -> str:
    """
    This gets the full path to the pickled object from the config
    :param cfg: parsed version of the config yaml
    :return: path to the pickle object
    """
    try:
        model_information: Dict[str, str] = cfg[MODEL_KEY]
        return os.path.join(model_information[MODEL_DIRECTORY], model_information[MODEL_PICKLED_OBJECT])
    except KeyError:
        exception_string = "Expecting a config with the following structure: ({}: ({}: foo, {}: bar, ...))"
        raise Exception(exception_string.format(MODEL_KEY, MODEL_DIRECTORY, MODEL_PICKLED_OBJECT))


def _get_pipeline_key(config_path: str) -> str:
    """
    This gets the key in which to extract the pipeline form the pickled object
    :param config_path: path to config yaml
    :return: key for the pipleine model
    """
    try:
        cfg = _read_config(config_path)
        return cfg[MODEL_KEY][MODEL_PIPELINE_KEY]
    except KeyError:
        exception_string = "Expecting a config with the following structure: ({}: ({}: foo, ...))"
        raise Exception(exception_string.format((MODEL_KEY, MODEL_PIPELINE_KEY)))


def _load_pickle(pickled_object_path: str) -> Dict[str, Any]:
    """
    Loads the pickle object from the given path
    :param pickled_object_path: path to the pickle object
    :return:
    """
    with open(pickled_object_path, "rb") as f:
        obj = pickle.load(f)
    return obj


def get_pickled_object(config_path: str) -> Dict[str, Any]:
    """
    This un-pickles the pickled object defined in the config
    :param config_path: path to the config yaml
    :return: the object that was pickled
    """
    cfg: Dict[str, Any] = _read_config(config_path)
    pickled_object_path: str = _get_pickle_file_path(cfg)
    obj: Dict[str, Any] = _load_pickle(pickled_object_path)
    return obj


def get_pipeline(config_path: str):
    """
    Gets the pipeline model
    :param config_path: path to the config yaml
    :return: pipeline model
    """
    pickled_object: Dict[str, Any] = get_pickled_object(config_path)
    pipeline_key: str = _get_pipeline_key(config_path)
    return pickled_object[pipeline_key]
