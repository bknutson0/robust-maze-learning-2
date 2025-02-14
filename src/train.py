from src.utils.config import Hyperparameters
from src.utils.training import train


def main() -> None:
    """Train the model for different percolation values."""
    # Define hyperparameters
    hyperparams = Hyperparameters()
    hyperparams.batch_size = 32
    hyperparams.epochs = 10
    hyperparams.pretrained = False

    # Define percolation values for fine-tuning
    # percolations = [0.000, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9]
    percolations = [0.5]

    # Train the model for each percolation value
    for percolation in percolations:
        hyperparams.percolation = percolation
        train(hyperparams)


if __name__ == '__main__':
    main()
