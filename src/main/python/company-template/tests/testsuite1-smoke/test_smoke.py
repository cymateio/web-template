import pytest


@pytest.mark.smoke
def test_smoke_one(logger):
    logger.info("1 SMOKE ONE")
    logger.info("2 SMOKE ONE")
    logger.info("3 SMOKE ONE")
    assert 1 == 1


@pytest.mark.smoke
def test_smoke_two(logger):
    logger.info("1 SMOKE TWO")
    logger.info("2 SMOKE TWO")
    logger.info("3 SMOKE TWO")
    assert 2 == 2
