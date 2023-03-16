import pytest
from src.Resources.resources import Resource

resource = Resource()


def test_drawer_button_action():
    button = resource.resume_button.draw(resource.screen)
    assert button.draw() == False

