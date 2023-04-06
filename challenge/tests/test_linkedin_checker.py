import pytest
from challenge.linkedin_checker import check_linkedin_feature


def test_correct_custom_url():
    assert check_linkedin_feature('jonathanafernandes', 'custom_url')
    assert check_linkedin_feature('jonfernandes2000', 'custom_url')
    assert check_linkedin_feature('JonathanFernandes', 'custom_url')
    assert check_linkedin_feature('JonathanFernandes2000', 'custom_url')


def test_incorrect_custom_url():
    assert check_linkedin_feature('jonathanafernande$', 'custom_url') is False
    assert check_linkedin_feature('jon-fernandes2000', 'custom_url') is False
    assert check_linkedin_feature('Jonathan_Fernandes', 'custom_url') is False
    assert check_linkedin_feature(
        'JonathanFernandes2000!!', 'custom_url') is False


def test_correct_email():
    assert check_linkedin_feature('jf@gmail.com', 'login')
    assert check_linkedin_feature('jonathanfernandes@gmail.com', 'login')
    assert check_linkedin_feature('jonathan-fernandes@gmail.com', 'login')
    assert check_linkedin_feature('jonathan_fernandes@gmail.com', 'login')
    assert check_linkedin_feature('jonathan.fernandes@gmail.com', 'login')


def test_incorrect_email():
    assert check_linkedin_feature('jonathangmail.com', 'login') is False
    assert check_linkedin_feature(
        'jonathanfernandes@gmail.biz', 'login') is False
    assert check_linkedin_feature(
        'jonathanfernandes@gmail.co.uk', 'login') is False


def test_incorrect_feature():
    with pytest.raises(ValueError):
        assert check_linkedin_feature('jonathanafernandes', 'www')
        assert check_linkedin_feature('jonathanafernandes', 'webpage')
        assert check_linkedin_feature('jonathanafernandes', 'social')
