from src.utils.config import TestParameters
from src.utils.model_loading import get_all_model_names
from src.utils.testing import test


def main() -> None:
    """Perform test according to test parameters."""
    # Filter model names, keeping only those that contain 'best' from most recent training runs
    model_names = get_all_model_names()
    model_names = [name for name in model_names if ('best' in name) and (('20250211' in name) or ('20250210' in name))]

    # Define test parameters
    test_params = TestParameters()
    test_params.model_name = model_names
    test_params.num_mazes = 100

    # Perform test
    test(test_params)


if __name__ == '__main__':
    main()
