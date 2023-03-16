import pygame.mixer
import pytest
import os
from src.Resources.resources import Resource
from src.Loader.loader import Loader
from src.Drawer.drawer import Drawer

# python -m pytest
# only console


@pytest.fixture
def resource():
    return Resource()


@pytest.fixture
def loader():
    return Loader()


@pytest.fixture
def path():
    return os.path.join("Unit_test")


@pytest.fixture
def drawer():
    return Drawer()


def test_drawer_button_action(resource):
    button = resource.resume_button
    assert button.draw(resource.screen) == False


def test_loader_read(loader, path):
    data = loader.readJSONFile(path, "test")
    assert data == {"fps": 240, "volume": 0.0, "sound": "music3.mp3"}


def test_loader_load_sound(loader):
    data = loader.loadSound("yes")
    assert type(data) == pygame.mixer.Sound

